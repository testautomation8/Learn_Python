import re

pattern = r"eggsp"
demo_string = "eggspamsausagespam"
if re.match(pattern, demo_string):
    print("Match found")
else:
    print("Match Not Found")
print(re.match(pattern, demo_string))

match = re.search(pattern, demo_string)
if match:
    print("Match found")
    print(re.search(pattern, demo_string))
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
else:
    print("Match Not Found")


if re.findall(pattern, demo_string):
    print("Match found")
else:
    print("Match Not Found")
print(re.findall(pattern, demo_string))