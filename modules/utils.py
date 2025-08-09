def is_printable(b):
    try:
        text = b.decode()
        return all(32 <= ord(c) <= 126 or c in '\n\r\t' for c in text)
    except UnicodeDecodeError:
        return False