def LetterChanges(stre):
    rv_str = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in stre:
        if ord('a') <= ord(letter) and ord(letter) < ord('z'):
            ch_str = ord(letter) + 1
            if ch_str in map(ord, vowels):
                rv_str += chr(ch_str - 32)
            else:
                rv_str += chr(ch_str)
        elif letter == 'z':
            rv_str += 'A'
        else:
            rv_str += letter
    return rv_str


# keep this function call here
# to see how to enter arguments in Python scroll down
print(LetterChanges(raw_input()))