import re

pattern = "^([\w-]{3,30})@([\w-]{2,20})\.{1}([\w]{2,5}(\.[\w]{2,5})?)$"

emails = [
    "emanuel@gmail.com",
    "mikk@yahoo.com",
    "sandrius@ge-mail.com",
    "sandri+us@ge-mail.com",
    "sandrius@ge-mail.com.edu",
    "ziad@google.com",
    "ziad@google. com",
    "zia#d@google. com",
]

for email in emails:
    print(re.search(pattern, email).group(0))