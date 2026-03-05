import re

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern = r"ab{2,3}"

matches = re.findall(pattern, text)

print(matches)