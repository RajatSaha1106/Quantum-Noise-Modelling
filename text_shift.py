def shift_plaintext(plaintext, shift_values):
    shifted_text = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = shift_values[i % len(shift_values)]
            shifted_text += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
        else:
            shifted_text += char
    return shifted_text
