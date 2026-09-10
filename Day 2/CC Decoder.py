def caesar_decrypt(text, shift):
    """
    Decodes a Caesar cipher message using a specific shift value.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the base ASCII value ('A' or 'a')
            base = ord('A') if char.isupper() else ord('a')
            # Apply the reverse shift using the modulo operator for wrap-around
            shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

# Example Usage:
encrypted_message = input("Enter your encrypted message: ")
shift_key = 3
decrypted_message = caesar_decrypt(encrypted_message, shift_key)

print(f"Encrypted message: {encrypted_message}")
print(f"Shift key: {shift_key}")
print(f"Decrypted message: {decrypted_message}")
