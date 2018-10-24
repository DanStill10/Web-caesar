def alphabet_position_char(c):
    cval = ord(c)
    if cval >= 97 and cval <= 122:
        return cval -97
    if cval >= 65 and cval <= 90 :
        return cval -65

def alphabet_position(str):
    return alphabet_position_char(str[0])
#Done
def rotate_character(c,rot):
    pos = alphabet_position_char(c)
    cval = ord(c)
    if cval >= 97 and cval <= 122:
        rotated_c = (pos + rot) % 26 + 97
        return chr(rotated_c)
    if cval >= 65 and cval <= 90 :
        rotated_c = (pos + rot) % 26 + 65
        return chr(rotated_c)
    return c

def rotate_string(text, rot):
    Result = ""
    for letter in text:
        Result = Result + rotate_character(letter,rot)
    return Result
#Done
def main():
    Message = input("Type a Message:")
    Numb = int(input ("Rotate by:"))
    return rotate_string(Message,Numb)


if __name__ == "__main__":
    Encrypted_message = main()
    print (Encrypted_message)