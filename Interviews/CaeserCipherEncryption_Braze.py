

def getExcryptedText(text, k):
    res = ''
    k = k %26
    for char in text:
        if not char.isalpha():
            res += char
            continue
        elif 'a' <= char <= 'z':
            start_idx = 97
            first_letter = 'a'
        elif 'A' <= char <= 'Z':
            start_idx = 65
            first_letter = 'A'

        newchar = chr((((ord(char) - ord(first_letter)) + k) % 26) + start_idx)
        res += newchar
    print("Encrypted Text: ", res)
    return res

def getDecryptedText(text, k):
    res = ''
    k = k %26
    for char in text:
        if not char.isalpha():
            res += char
            continue
        elif 'a' <= char <= 'z':
            start_idx = 97
            first_letter = 'a'
        elif 'A' <= char <= 'Z':
            start_idx = 65
            first_letter = 'A'

        num = (((ord(char) - ord(first_letter)) - k) % 26) + start_idx
        newchar = chr(num)
        res += newchar
    print("Decrypted Text: ", res)
    return res



if __name__ == "__main__":
    encrypted_word = getExcryptedText("attackatonceyATTAY", 4)
    original_text = getDecryptedText(encrypted_word, 4)