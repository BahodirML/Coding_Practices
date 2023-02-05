from transliterate import to_cyrillic, to_latin
matn = input('Mant kirinting')

if matn.isascii():
    print(to_cyrillic(matn))
else: print(to_latin(matn))