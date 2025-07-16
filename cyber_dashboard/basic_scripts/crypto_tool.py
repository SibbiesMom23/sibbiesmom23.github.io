# crypto_tool.py

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            # shift character and wrap around alphabet
            shifted = chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            result += shifted
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Simple Caesar Cipher Tool ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Exiting.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift amount (1-25): "))
    except ValueError:
        print("Shift must be a number. Exiting.")
        return
    if not 1 <= shift <= 25:
        print("Shift must be between 1 and 25. Exiting.")
        return

    if choice == 'e':
        output = encrypt(text, shift)
        print("Encrypted message:", output)
    else:
        output = decrypt(text, shift)
        print("Decrypted message:", output)

if __name__ == "__main__":
    main()
