import hashlib
import base64
import codecs
from modules import utils

def menu():
    while True:
        print("--- Cryptography ---")
        print("")
        print("1. Hash Generator")
        print("2. ROT13")
        print("3. XOR (ASCII/Hex Inputs With Given Fixed Key)")
        print("4. Caesar Cipher Brute Force")
        print("5. Atbash Cipher")
        print("6. Single-Byte XOR Brute Force")
        print("7. Morse Code Encode/Decode")
        print("8. Back to main menu")
        print("")
        q3 = input("Choose your needs: ")
        print("")

        match q3:
            case "1":
                hash_input = input("Enter text to hash: ")
                print("")
                print("1. Convert to MD5")
                print("2. Convert to SHA1")
                print("3. Convert to SHA256")
                print("4. Convert to SHA512")
                print("5. Convert to all")
                print("")
                hash_convert = input("Select to convert: ")
                print("")

                match hash_convert:
                    case "1":
                        print("MD5:", hashlib.md5(hash_input.encode()).hexdigest())
                        print("")
                    case "2":
                        print("SHA1:", hashlib.sha1(hash_input.encode()).hexdigest())
                        print("")
                    case "3":
                        print("SHA256:", hashlib.sha256(hash_input.encode()).hexdigest())
                        print("")
                    case "4":
                        print("SHA512:", hashlib.sha512(hash_input.encode()).hexdigest())
                        print("")
                    case "5":
                        print("MD5:", hashlib.md5(hash_input.encode()).hexdigest())
                        print("SHA1:", hashlib.sha1(hash_input.encode()).hexdigest())
                        print("SHA256:", hashlib.sha256(hash_input.encode()).hexdigest())
                        print("SHA512:", hashlib.sha512(hash_input.encode()).hexdigest())
                        print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "2":
                rot13_input = input("Enter text: ")
                print("")
                print("1. Encrypt using ROT13")
                print("2. Decrypt using ROT13")
                print("")
                rot13_convert = input("Select to convert: ")
                print("")

                match rot13_convert:
                    case "1":
                        print("Encrypted text:", codecs.encode(rot13_input, "rot13"))
                        print("")
                    case "2":
                        print("Decrypted text:", codecs.encode(rot13_input, "rot13"))
                        print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "3":
                print("")
                print("1. XOR with ASCII")
                print("2. XOR with Hex")
                print("")
                xor_choice = input("Select to convert: ")
                print("")

                match xor_choice:
                    case "1":
                        xor_ascii_string = input("Enter ASCII string: ")
                        xor_ascii_key = input("Enter key: ")
                        print("")
                        xor_ascii = xor_crypt_ascii(xor_ascii_string, xor_ascii_key)
                        try:
                            print(f"XOR (ASCII): {xor_ascii.decode()}")
                        except UnicodeDecodeError:
                            print("XOR (ASCII): The XORed characters are not printable")
                        print(f"XOR (hex): {xor_ascii.hex()}")
                        print("")
                    case "2":
                        xor_hex_string = input("Enter hex string: ")
                        xor_hex_key = input("Enter key: ")
                        print("")
                        try:
                            xor_hex = xor_crypt_hex(xor_hex_string, xor_hex_key)
                        except ValueError:
                            print("Please provide a valid hex string")
                            break
                        try:
                            print(f"XOR (ASCII): {xor_hex.decode()}")
                        except UnicodeDecodeError:
                            print("XOR (ASCII): The XORed characters are not printable")
                        print(f"XOR (hex): {xor_hex.hex()}")
                        print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "4":
                print("")
            case "5":
                atbash_input = input("Enter text: ")
                atbash_output = []
                for char in atbash_input:
                    if char.isalpha():
                        if char.isupper():
                            atbash_output.append(chr(ord('Z') - (ord(char) - ord('A'))))
                        else:
                            atbash_output.append(chr(ord('z') - (ord(char) - ord('a'))))
                    else:
                        atbash_output.append(char)
                atbash_final = ''.join(atbash_output)
                print(f"Atbashed: {atbash_final}")
                print("")
            case "6":
                print("")
            case "7":
                print("")
            case "8":
                break
            case _:
                print("Please select a valid option")
                print("")

def xor_crypt_ascii(data: str, key: str) -> bytes:
    return bytes([ord(c) ^ ord(key[i % len(key)]) for i, c in enumerate(data)])

def xor_crypt_hex(data: str, key: str) -> bytes:
    raw = bytes.fromhex(data)
    xored = bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(raw)])
    return xored
