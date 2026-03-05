import re

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

result = re.sub(r"[ ,\.]", ":", text)

print(result)