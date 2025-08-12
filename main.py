from modules import bc, crypto, bfa, stego

print("")
print(" █    ██  ██▓  ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▄▄▄█████▓  █████▒")
print(" ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██   ▒")
print("▓██  ▒██░▒██░  ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒████ ░")
print("▓▓█  ░██░▒██░  ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░▓█▒  ░")
print("▒▒█████▓ ░██████▒▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░▒█░") 
print("░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░    ▒ ░")
print("░░▒░ ░ ░ ░ ░ ▒  ░  ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░     ░")
print(" ░░░ ░ ░   ░ ░   ░        ░░   ░   ░   ▒   ░          ░       ░ ░")
print("   ░         ░  ░          ░           ░  ░░ ░")
print("                                           ░")
print("")
print("By Kaizokuv")
print("Github: https://github.com/kaizokuv")

def mainmenu():
    print("")
    print("--- Main Menu ---")
    print("")
    print("1. Base Conversions")
    print("2. Cryptography")
    print("3. Steganography (WIP)")
    print("4. Binary/File Analysis (WIP)")
    print("5. Exit")
    print("")

def main():
    while True:
        mainmenu()
        q1 = input("Welcome, choose your option: ")
        print("")

        match q1:
            case "1":
                bc.menu()
            case "2":
                crypto.menu()
            case "3":
                stego.menu()
            case "4":
                bfa.menu()
            case "5":
                print("Thank you, please come again")
                print("Any ideas for future updates are welcome, hmu on Github :D")
                print("")
                exit()
            case _:
                print("Please select a valid option.")
                print("")

if __name__ == "__main__":
    main()