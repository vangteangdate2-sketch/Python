def caesar_cipher_encoder(text, shift):
    result = ""
    # Ensure shift is within the 0-25 range
    shift = shift % 26

    for char in text:
        if char.isalpha():
            # Determine the base ASCII value for 'A' or 'a'
            base = ord('A') if char.isupper() else ord('a')
            # Calculate the new position using modular arithmetic
            shifted_position = (ord(char) - base + shift) % 26
            # Convert the new position back to a character and add to the result
            result += chr(base + shifted_position)
        else:
            # Append non-alphabetic characters without shifting
            result += char

    return result

# --- Example Usage ---
plaintext = input("Enter your Plain Text: ")
key = int(input("Enter your key number: "))
encrypted_message = caesar_cipher_encoder(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Shift Key: {key}")
print(f"Ciphertext: {encrypted_message}")

# To decrypt, you can use the same function with a negative shift value, or a shift of 26 - key
decrypted_message = caesar_cipher_encoder(encrypted_message, -key)
print(f"Decrypted: {decrypted_message}")
