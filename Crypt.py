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
    keyboard.wait("ctrl+c")
    keyboard.wait("ctrl+c")
    record = pc.paste()
    if record.startswith("gAAAAA")==True:
        decrypted = f.decrypt(record.encode())
        print("decrypted message:")
        print(decrypted.decode())
        print("")
    else:
        encrypted = f.encrypt(record.encode())
        print("encrypted message:")
        print(encrypted.decode())
        print("")
        keyboard.press_and_release("ctrl+a")
        keyboard.press_and_release("del")
        keyboard.write(str(encrypted.decode()))
