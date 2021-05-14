try:
    from colorama import Fore, init
    from cryptography.fernet import Fernet
    import keyboard
    from os import system
    import pyperclip as pc
except ImportError:
    input("Press enter to start installing... ")
    system("py -m pip install -r requirements.txt")
    system("python -m pip install -r requirements.txt")
    system("python3 -m pip install -r requirements.txt")
    input("\n\nDone installing modules! Please restart the script now. Press enter to continue... ")
    quit()

init()

title = f"""                                                    
┌───────────────────────────────────────────────────────────────┐
{Fore.RESET}│{Fore.BLUE}  ██████╗██████╗ ██╗   ██╗██████╗ ████████╗   {Fore.LIGHTYELLOW_EX}██████╗ ██╗   ██╗{Fore.RESET}│
{Fore.RESET}│{Fore.BLUE} ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝   {Fore.LIGHTYELLOW_EX}██╔══██╗╚██╗ ██╔╝{Fore.RESET}│
{Fore.RESET}│{Fore.BLUE} ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║      {Fore.LIGHTYELLOW_EX}██████╔╝ ╚████╔╝ {Fore.RESET}│
{Fore.RESET}│{Fore.BLUE} ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║      {Fore.LIGHTYELLOW_EX}██╔═══╝   ╚██╔╝  {Fore.RESET}│
{Fore.RESET}│{Fore.BLUE} ╚██████╗██║  ██║   ██║   ██║        ██║      {Fore.LIGHTYELLOW_EX}██║        ██║   {Fore.RESET}│
{Fore.RESET}│{Fore.BLUE}  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝      {Fore.LIGHTYELLOW_EX}╚═╝        ╚═╝   {Fore.RESET}│
└───────────────────────────────────────────────────────────────┘
Developed by Oblivios | Github link: https://github.com/Oblivios
Discord: Obli#2933
"""
print(title)

choice = input("Generate Key ? (Y/N) ").lower() #Y if nobody has the key, N if you have a key
if choice == "y":
    key = Fernet.generate_key()
elif choice == "n":
    key = input("Copy and Paste the key here: ").encode()
print("Key: "+key.decode())
f = Fernet(key)
while True:
    choice_ = input("Encrypt/Decrypt ? (E/D) ").lower()
    if choice_ == "e":
        keyboard.wait("ctrl+c")
        keyboard.wait("ctrl+c")
        record = pc.paste()
        print("")
        print(record)
        print("")
        encrypted = f.encrypt(record.encode())
        keyboard.press_and_release("ctrl+a")
        keyboard.press_and_release("del")
        keyboard.write(str(encrypted.decode()))
        keyboard.press("enter")
        keyboard.release("enter")
    elif choice_ == "d":
        message = input("Message: ")
        decrypted = f.decrypt(message.encode())
        print("")
        print(decrypted.decode())
        print("")
