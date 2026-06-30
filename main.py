def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


print("=" * 50)
print("        CAESAR CIPHER ENCRYPTION TOOL")
print("=" * 50)

message = input("Enter your message: ").strip()

while True:
    try:
        shift = int(input("Enter shift value (0-25): "))
        if 0 <= shift <= 25:
            break
        else:
            print("Please enter a value between 0 and 25.")
    except ValueError:
        print("Please enter a valid number.")

print("\nChoose an option")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice: ")

if choice == "1":
    print("\nEncrypted Message:", caesar_cipher(message, shift, "encrypt"))

elif choice == "2":
    print("\nDecrypted Message:", caesar_cipher(message, shift, "decrypt"))

else:
    print("\nInvalid choice!")