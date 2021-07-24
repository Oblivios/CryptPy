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
        if keyboard.is_pressed("f2"):
            print("Waiting for your copy...")
            keyboard.wait("ctrl+c")
            keyboard.wait("ctrl+c")
            record = pc.paste()
        if record.startswith("gAAAAA")==True:
            try:
                decrypted = f.decrypt(record.encode())
                print("decrypted message:")
                print(decrypted.decode())
                print("")
            except cryptography.exceptions.InvalidSignature:
                print("Can't decrypt the message.\nYou may have the wrong key!\n")
            except cryptography.fernet.InvalidToken:
                print("Can't decrypt the message.\nYou may have the wrong key!\n")
        else:
            encrypted = f.encrypt(record.encode())
            print("encrypted message:")
            print(encrypted.decode())
            print("")
            keyboard.press_and_release("ctrl+a")
            keyboard.press_and_release("del")
            keyboard.write(encrypted.decode())
            time.sleep(0.1)
            keyboard.press_and_release("enter")
    elif keyboard.is_pressed("f3"):
        print("Paused... Press F3 to re-run CryptPy.")
        keyboard.wait("f3")
        print("Unpaused!")
    elif keyboard.is_pressed("f4"):
        choice = input("Generate Key ? (Y/N) ").lower()
        if choice == "y":
            key = Fernet.generate_key()
        elif choice == "n":
            key = input("Copy and Paste the key here:").encode()
        print("Key: "+key.decode())
        f = Fernet(key)
    elif keyboard.is_pressed("f5"):
        leave = str(input("Type any key to leave... type C to cancel...")).lower()
        if leave!="c":
            exit()
    time.sleep(0.2)
