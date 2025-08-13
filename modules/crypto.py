import hashlib
import codecs
import collections
import string

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
        print("7. Morse Code")
        print("8. Normal Substitution (Only Letters)")
        print("9. Custom Substitution (Printable ASCII Range)")
        print("10. Back to main menu")
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
                caesar_input = input("Enter text: ")
                print("")
                print("Brute forcing...")
                print("")
                for shift in range(1, 26):
                    print(f"Shift Number {shift}: {caesar_decrypt(caesar_input, shift)}")
                print("")
                print("(I'm sorry you have to search through the whole thing TwT..)")
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
                xor_brute_force_input = input("Enter hex string: ")
                xor_brute_force_key_input = input("Enter single byte key in decimal or hex (Enter 'null' if no present key): ")
                if xor_brute_force_key_input == 'null':
                    print("")
                    print("Brute forcing...")
                    print("")
                    data = bytes.fromhex(xor_brute_force_input)
                    candidates = []
                    for key in range(256):
                        decoded_bytes = xor_brute_force(data, key)
                        try:
                            decoded_str = decoded_bytes.decode("utf-8")
                        except UnicodeDecodeError:
                            continue
                        score = xor_brute_force_score(decoded_str)
                        candidates.append((score, key, decoded_str))
                    candidates.sort(reverse=True, key=lambda x: x[0])
                    print("Here's the top 25 keys (Maybe in English..? I'm sorry if it's not TwT..): ")
                    print("")
                    for score, key, text in candidates[:25]:
                        print(f"Key {key} (0x{key:02x}) -> {text}")
                    print("")
                    print("Here's the rest of the keys if it's not in the top 25 (I'm sorry if you have to search through the whole thing TwT..)")
                    remaining = len(candidates) - 25
                    if remaining > 0:
                        print(f"There are {remaining} more keys. Press 'Q' to see the next 25, or any other key to stop.")
                    start_index = 25
                    while start_index < len(candidates):
                        xor_brute_force_paging = input("> ").strip()
                        if xor_brute_force_paging.lower() != 'q':
                            break
                        end_index = min(start_index + 25, len(candidates))
                        print("")
                        print(f"Here's the next 25 keys from {start_index + 1} to {end_index}:")
                        print("")
                        for score, key, text in candidates[start_index:end_index]:
                            print(f"Key with a score of {score:.2f}: {key} (0x{key:02x}) -> {text}")
                        start_index += 25
                        print("")
                else:
                    data = bytes.fromhex(xor_brute_force_input)
                    if xor_brute_force_key_input.lower() != "null":
                        try:
                            key = int(xor_brute_force_key_input, 16) if xor_brute_force_key_input.startswith("0x") else int(xor_brute_force_key_input)
                        except ValueError:
                            print("Please enter the key as a decimal or a hex")
                            return
                        if not (0 <= key <= 255):
                            print("Please enter a single byte key (0-255)")
                            return
                        else:
                            decoded_bytes = xor_brute_force(data, key)
                            try:
                                decoded_str = decoded_bytes.decode("utf-8")
                            except UnicodeDecodeError:
                                decoded_str = decoded_bytes.decode("utf-8", errors="replace")
                            print("")
                            print(f"The plaintext with the given key {key} (0x{key:02x}) is: {decoded_str}")
                            print("")
            case "7":
                print("1. Encrypt with Morse Code")
                print("2. Decrypt with Morse Code")
                print("")
                morse_code_input = input("Select to convert: ")
                print("")

                match morse_code_input:
                    case "1":
                        morse_code_encrypt_input = input("Enter text: ")
                        print("")
                        morse_code_encrypt_input_caps = morse_code_encrypt_input.upper()
                        if all(char in morse_code_def or char.isspace() for char in morse_code_encrypt_input_caps):
                            morse_output = []
                            for char in morse_code_encrypt_input_caps:
                                if char != " ":
                                    morse_output.append(morse_code_def[char])
                                else:
                                    morse_output.append("  ") 
                            print(" ".join(morse_output))
                        else:
                            print("Please enter valid ASCII text")
                            print("")
                    case "2":
                        morse_code_decrypt_input = input("Enter morse code: ")
                        print("")
                        words = morse_code_decrypt_input.split("   ")
                        ascii_output = []
                        try:
                            for word in words:
                                letters = word.split(" ")
                                decoded_word = "".join(morse_code_reverse_def[letter] for letter in letters if letter)
                                ascii_output.append(decoded_word)
                            print(" ".join(ascii_output))
                            print("")
                        except KeyError:
                            print("Please enter valid morse text")
                            print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "8":
                print("1. Encrypt with Substitution")
                print("2. Decrypt with Substitution")
                print("")
                substitution_choice = input("Select to convert: ")
                print("")

                match substitution_choice:
                    case "1":
                        substitution_input = input("Enter text: ")
                        if not all(char in PRINTABLE for char in substitution_input):
                            print("")
                            print("Please enter valid ASCII characters")
                            print("")
                        else:
                            raw_substitution_pattern = input("Input pattern (e.g. format: +1, -14, +7, -5, +12): ")
                            print("")
                            substitution_pattern = [int(x) for x in raw_substitution_pattern.replace(" ", "").split(",")]
                            print("Substituted text:", substitute(substitution_input, substitution_pattern))
                            print("")
                    case "2":
                        reverse_input = input("Enter substituted text: ")
                        if not all(char in PRINTABLE for char in reverse_input):
                            print("")
                            print("Please enter valid ASCII characters")
                            print("")
                        else:
                            raw_reverse_substitution_pattern = input("Input pattern (e.g. format: +1, -14, +7, -5, +12): ")
                            reverse_pattern = [int(x) for x in raw_reverse_substitution_pattern.replace(" ", "").split(",")]
                            print("Original text:", reverse_substitute(reverse_input, reverse_pattern))
                            print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "9":
                print("1. Encrypt with Substitution")
                print("2. Decrypt with Substitution")
                print("")
                custom_substitution_printable_choice = input("Select to convert: ")
                print("")

                match custom_substitution_printable_choice:
                    case "1":
                        custom_substitution_printable_input = input("Enter text: ")
                        if not all(char in PRINTABLE for char in custom_substitution_printable_input):
                            print("")
                            print("Please enter valid ASCII characters")
                            print("")
                        else:
                            raw_custom_substitution_printable_pattern = input("Input pattern (e.g. format: +1, -14, +7, -5, +12): ")
                            print("")
                            custom_substitution_printable_pattern = [int(x) for x in raw_custom_substitution_printable_pattern.replace(" ", "").split(",")]
                            print("Substituted text:", custom_substitution_printable(custom_substitution_printable_input, custom_substitution_printable_pattern))
                            print("")
                    case "2":
                        reversed_custom_substitution_printable_input = input("Enter text: ")
                        if not all(char in PRINTABLE for char in reversed_custom_substitution_printable_input):
                            print("")
                            print("Please enter valid ASCII characters")
                            print("")
                        else:
                            reversed_raw_custom_substitution_printable_pattern = input("Input pattern (e.g. format: +1, -14, +7, -5, +12): ")
                            print("")
                            reversed_custom_substitution_printable_pattern = [int(x) for x in reversed_raw_custom_substitution_printable_pattern.replace(" ", "").split(",")]
                            print("Original text:", reverse_custom_substitution_printable(reversed_custom_substitution_printable_input, reversed_custom_substitution_printable_pattern))
                            print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "10":
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

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - start - shift) % 26 + start)
        else:
            plaintext += char
    return plaintext

def xor_brute_force(ciphertext: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in ciphertext])

def xor_brute_force_score(text):
    text_l = ''.join(c.lower() for c in text if c.isalpha())
    if not text_l:
        return 0.0
    observed = collections.Counter(text_l)
    chi = 0.0
    for ch, exp in xor_brute_force_score_freq.items():
        obs = observed.get(ch, 0)
        expected_count = exp * len(text_l)
        chi += (obs - expected_count)**2 / (expected_count + 1e-9)
    return 1 / (1 + chi)

xor_brute_force_score_freq = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074
}

morse_code_def = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

morse_code_reverse_def = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
    '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
    '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@'
}

ALPHA_ONLY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRINTABLE = "".join(ch for ch in string.printable if ch not in "\n\r\t")

def substitute(text, pattern):
    return pattern_cipher(text, pattern, mode="alpha", reverse=False)

def reverse_substitute(text, pattern):
    return pattern_cipher(text, pattern, mode="alpha", reverse=True)

def custom_substitution_printable(text, pattern):
    return pattern_cipher(text, pattern, mode="ascii", reverse=False)

def reverse_custom_substitution_printable(text, pattern):
    return pattern_cipher(text, pattern, mode="ascii", reverse=True)

def pattern_cipher(text, pattern, mode="alpha", reverse=False):
    if mode == "alpha":
        charset = ALPHA_ONLY
    elif mode == "ascii":
        charset = PRINTABLE
    else:
        raise ValueError("Please enter valid ASCII characters")
    if reverse:
        pattern = [-p for p in pattern]
    result = []
    pat_len = len(pattern)
    for i, ch in enumerate(text):
        if ch in charset:
            idx = charset.index(ch)
            shift = pattern[i % pat_len]
            new_idx = (idx + shift) % len(charset)
            result.append(charset[new_idx])
        else:
            result.append(ch)
    return "".join(result)
