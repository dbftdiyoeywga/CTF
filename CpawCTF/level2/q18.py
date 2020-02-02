with open('CpawCTF/level2/files/misc100', 'rb') as f:
    strings = f.read().decode("utf-8", "ignore")

for c in "lovelive!":
    strings = strings.replace(c, "")

strings = strings[1::3]

print(strings.lower())
