
def is_flag(flag, flags):
    return flag in flags

def load_flags():
    global flags
    with open("/app/flag.txt", "r") as flag:
        return list(map(lambda line: line[:-1], flag.readlines()))

prompt = "enter flag ('q' to exit): "
def read_entry():
    return input(prompt)

def show_message(message):
    print(message)


def main_loop():
    flags = load_flags()
    supplied = []
    print("Enter the flag for each tree, you don't have to follow a specific order: ")
    while len(flags) > 0:
        entry = read_entry()
        if entry.lower() == 'q':
            show_message("quitting...")
            return
        if entry in supplied:
            show_message("flag already supplied.")
            continue
        if not is_flag(entry, flags):
            show_message("invalid input.")
            exit(1)
        flags.remove(entry)
        supplied.append(entry)
        show_message(f"flag found, {len(flags)} remains")
    show_message("the flag is ingeneer{C4n_Zom8Iez_clImB_TR33s}")

main_loop()

