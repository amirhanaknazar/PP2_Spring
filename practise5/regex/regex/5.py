import re

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern = r"a.*b"

matches = re.findall(pattern, text)

print(matches)