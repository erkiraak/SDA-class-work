import re

phrase = "test43543lfdsfdsfl534543fdgl432fr"
pattern = "(\d+)"
result = re.findall(pattern, phrase)

print(result)

pattern = "\d"
result = re.sub(pattern, "", phrase)

print(result)

phrase = "+48123456789"
pattern = "^[\+|00]?48\d{9}"

result = re.findall(pattern, phrase)

print(result)
