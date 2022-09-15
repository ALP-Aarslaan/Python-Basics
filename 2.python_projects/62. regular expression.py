import re
pattern = r"Colour"
if re.match(pattern, "Colour red Colour. this blood colour"):
    print("matched")

else:
    print("Not matched")

if re.search(pattern,"colour red Colour. this blood colour"):
    print("found")

else:
    print("found")

print(re.findall(pattern,"colour red Colour. this blood Colour"))

pattern1 = "name"
text = "my name is jonayed"
match = re.search(pattern1,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())