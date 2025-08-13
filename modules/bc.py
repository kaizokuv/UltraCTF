import base64

def menu():
    while True:
        print("--- Base Conversions ---")
        print("")
        print("1. Binary -> Decimal/Hex/Octal")
        print("2. Decimal -> Binary/Hex/Octal/Unicode")
        print("3. Hex -> Binary/Decimal/Octal/Unicode")
        print("4. Octal -> Binary/Decimal/Hex")
        print("5. Unicode -> Decimal/Hex")
        print("6. Base32")
        print("7. Base58")
        print("8. Base64")
        print("9. Back to main menu")
        print("")
        q2 = input("Choose your needs: ")
        print("")

        match q2:
            case "1":
                binary_input = input("Input binary (Separate by spaces): ")
                print("")
                print("1. Convert to decimal")
                print("2. Convert to hex")
                print("3. Convert to octal")
                print("")
                binary_convert = input("Select to convert: ")
                print("")

                match binary_convert:
                    case "1":
                        result = binary_to_decimal(binary_input)
                        print("Decimal values: ", result)
                        print("")
                    case "2":
                        result = binary_to_hex(binary_input)
                        print("Hex values: ", result)
                        print("")
                    case "3":
                        result = binary_to_octal(binary_input)
                        print("Octal values: ", result)
                        print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "2":
                decimal_input = input("Input decimal values (Separate with spaces): ")
                print("")
                print("1. Convert to binary")
                print("2. Convert to hex")
                print("3. Convert to octal")
                print("4. Convert to unicode")
                print("")
                decimal_convert = input("Select to convert: ")
                print("")

                match decimal_convert:
                    case "1":
                        result = decimal_to_binary(decimal_input)
                        print("Binary values: ", result)
                        print("")
                    case "2":
                        result = decimal_to_hex(decimal_input)
                        print("Hex values: ", result)
                        print("")
                    case "3":
                        result = decimal_to_octal(decimal_input)
                        print("Octal values: ", result)
                        print("")
                    case "4":
                        result = decimal_to_unicode(decimal_input)
                        print("Unicode values: ", result)
                        print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "3":
                hex_input = input("Input hex values (Separate with spaces): ")
                print("")
                print("1. Convert to binary")
                print("2. Convert to decimal")
                print("3. Convert to octal")
                print("4. Convert to unicode")
                print("")
                hex_convert = input("Select to convert: ")
                print("")

                match hex_convert:
                    case "1":
                        result = hex_to_binary(hex_input)
                        print("Binary values: ", result)
                        print("")
                    case "2":
                        result = hex_to_decimal(hex_input)
                        print("Decimal values: ", result)
                        print("")
                    case "3":
                        result = hex_to_octal(hex_input)
                        print("Octal values: ", result)
                        print("")
                    case "4":
                        result = hex_to_unicode(hex_input)
                        print("Unicode values: ", result)
                        print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "4":
                octal_input = input("Input octal values (Separate by spaces): ")
                print("")
                print("1. Convert to binary")
                print("2. Convert to decimal")
                print("3. Convert to hex")
                print("")
                octal_convert = input("Select to convert: ")
                print("")

                match octal_convert:
                    case "1":
                        result = octal_to_binary(octal_input)
                        print("Binary values: ", result)
                        print("")
                    case "2":
                        result = octal_to_decimal(octal_input)
                        print("Decimal values: ", result)
                        print("")
                    case "3":
                        result = octal_to_hex(octal_input)
                        print("Hex values: ", result)
                        print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "5":
                unicode_input = input("Input unicode string: ")
                print("")
                print("1. Convert to decimal")
                print("2. Convert to hex")
                print("")
                unicode_convert = input("Select to convert: ")
                print("")

                match unicode_convert:
                    case "1":
                        result = unicode_to_decimal(unicode_input)
                        print("Decimal values: ", result)
                        print("")
                    case "2":
                        result = unicode_to_hex(unicode_input)
                        print("Hex values: ", result)
                        print("")
                    case _:
                        print("Please select a valid option")
                        print("")
            case "6":
                base32_input = input("Input String: ")
                print("1. Encode to Base32")
                print("2. Decode from Base32")
                print("")
                base32_convert = input("Select to convert: ")
                print("")

                match base32_convert:
                    case "1":
                        result = base32_encode(base32_input)
                        print("Encoded Base32: ", result)
                        print("")
                    case "2":
                        result = base32_decode(base32_input)
                        print("Decoded Base32: ", result)
                        print("")
            case "7":
                base58_input = input("Input String: ")
                print("1. Encode to Base58")
                print("2. Decode from Base58")
                print("")
                base58_convert = input("Select to convert: ")
                print("")

                match base58_convert:
                    case "1":
                        result = base58_encode(base58_input)
                        print("Encoded Base58: ", result)
                        print("")
                    case "2":
                        result = base58_decode(base58_input)
                        print("Decoded Base58: ", result)
                        print("")
            case "8":
                base64_input = input("Input String: ")
                print("1. Encode to Base64")
                print("2. Decode from Base64")
                print("")
                base64_convert = input("Select to convert: ")
                print("")

                match base64_convert:
                    case "1":
                        result = base64_encode(base64_input)
                        print("Encoded Base64: ", result)
                        print("")
                    case "2":
                        result = base64_decode(base64_input)
                        print("Decoded Base64: ", result)
                        print("")
            case "9":
                break
            case _:
                print("Please select a valid option")
                print("")

def binary_to_decimal(text):
    try:
        binaries = text.split()
        return " ".join(str(int(b, 2)) for b in binaries)
    except ValueError:
        return "Invalid binary input."

def binary_to_hex(text):
    try:
        binaries = text.split()
        return " ".join(format(int(b, 2), "x") for b in binaries)
    except ValueError:
        return "Invalid binary input."

def binary_to_octal(text):
    try:
        binaries = text.split()
        return " ".join(format(int(b, 2), "o") for b in binaries)
    except ValueError:
        return "Invalid binary input."

def decimal_to_binary(text):
    try:
        numbers = map(int, text.split())
        return " ".join(format(num, "b") for num in numbers)
    except ValueError:
        return "Invalid decimal input."

def decimal_to_hex(text):
    try:
        numbers = map(int, text.split())
        return " ".join(format(num, "x") for num in numbers)
    except ValueError:
        return "Invalid decimal input."

def decimal_to_octal(text):
    try:
        numbers = map(int, text.split())
        return " ".join(format(num, "o") for num in numbers)
    except ValueError:
        return "Invalid decimal input."

def decimal_to_unicode(text):
    try:
        numbers = map(int, text.split())
        chars = []
        for num in numbers:
            if 0 <= num <= 0x10FFFF:
                chars.append(chr(num))
            else:
                chars.append('?')
        return ''.join(chars)
    except ValueError:
        return "Invalid decimal input."
    
def hex_to_binary(text):
    try:
        hex_values = text.split()
        return " ".join(format(int(h, 16), "b") for h in hex_values)
    except ValueError:
        return "Invalid hex input."

def hex_to_decimal(text):
    try:
        hex_values = text.split()
        return " ".join(str(int(h, 16)) for h in hex_values)
    except ValueError:
        return "Invalid hex input."

def hex_to_octal(text):
    try:
        hex_values = text.split()
        return " ".join(format(int(h, 16), "o") for h in hex_values)
    except ValueError:
        return "Invalid hex input."

def hex_to_unicode(text):
    try:
        hex_values = text.split()
        return ''.join(chr(int(h, 16)) for h in hex_values)
    except ValueError:
        return "Invalid hex input."

def octal_to_binary(text):
    try:
        oct_values = text.split()
        return " ".join(format(int(o, 8), "b") for o in oct_values)
    except ValueError:
        return "Invalid octal input."

def octal_to_decimal(text):
    try:
        oct_values = text.split()
        return " ".join(str(int(o, 8)) for o in oct_values)
    except ValueError:
        return "Invalid octal input."

def octal_to_hex(text):
    try:
        oct_values = text.split()
        return " ".join(format(int(o, 8), "x") for o in oct_values)
    except ValueError:
        return "Invalid octal input."
    
def unicode_to_decimal(text):
    return " ".join(str(ord(c)) for c in text)

def unicode_to_hex(text):
    return " ".join(format(ord(c), "x") for c in text)

def base32_encode(text):
    try:
        return base64.b32encode(text.encode()).decode()
    except Exception:
        return "Invalid input for Base32 encoding."

def base32_decode(text):
    try:
        return base64.b32decode(text.encode()).decode(errors="replace")
    except Exception:
        return "Invalid Base32 string."
    
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58_encode(text):
    try:
        num = int.from_bytes(text.encode(), 'big')
        encoded = ''
        while num > 0:
            num, rem = divmod(num, 58)
            encoded = BASE58_ALPHABET[rem] + encoded
        padding = sum(1 for c in text.encode() if c == 0)
        return BASE58_ALPHABET[0] * padding + encoded
    except Exception:
        return "Invalid input for Base58 encoding."

def base58_decode(text):
    try:
        num = 0
        for char in text:
            num = num * 58 + BASE58_ALPHABET.index(char)
        decoded = num.to_bytes((num.bit_length() + 7) // 8, 'big')
        return decoded.decode(errors="replace")
    except Exception:
        return "Invalid Base58 string."

def base64_encode(text):
    try:
        return base64.b64encode(text.encode()).decode()
    except Exception:
        return "Invalid input for Base64 encoding."

def base64_decode(text):
    try:
        return base64.b64decode(text.encode()).decode(errors="replace")
    except Exception:
        return "Invalid Base64 string."
