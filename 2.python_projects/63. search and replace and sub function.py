import re

pattern = r"colour"
text = " i love green colour, this colour represents everlasting freshness of our nature"
string = re.sub(pattern, "color", text)
print(string)

pattern = r"colour"
text = " i love green colour, this colour represents everlasting freshness of our nature"
string = re.sub(pattern, "color", text, count=1)
print(string)
