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
                        print("1. Encrypt")
                        print("2. Decrypt")
                        print("")
                        xor_ascii_choice = input("Select to convert: ")

                        match xor_ascii_choice:
                            case "1":
                                ascii_encrypted = xor_crypt_ascii(xor_ascii_string, xor_ascii_key)
                                print(f"Encrypted XOR: {ascii_encrypted}")
                                print("")
                            case "2":
                                ascii_decrypted = xor_crypt_ascii(xor_ascii_string, xor_ascii_key)
                                print(f"Decrypted XOR: {ascii_decrypted}")
                                print("")
                    case "2":
                        xor_hex_string = input("Enter hex string: ")
                        xor_hex_key = input("Enter key: ")
                        print("")
                        print("1. Encrypt")
                        print("2. Decrypt")
                        print("")
                        xor_hex_choice = input("Select to convert: ")

                        match xor_hex_choice:
                            case "1":
                                hex_encrypted = xor_crypt_hex(xor_hex_string, xor_hex_key)
                                print(f"Encrypted XOR: {hex_encrypted}")
                                print("")
                            case "2":
                                hex_decrypted = xor_crypt_hex(xor_hex_string, xor_hex_key)
                                print(f"Decrypted XOR: {hex_decrypted}")
                                print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "4":
                print("")
            case "5":
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

def xor_crypt_ascii(data: str, key: str) -> str:
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def xor_crypt_hex(data: str, key: str) -> str:
    raw = bytes.fromhex(data)
    xored = bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(raw)])
    return xored.hex()
