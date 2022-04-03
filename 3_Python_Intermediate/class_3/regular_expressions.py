import re

# Emails
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
    try:
        print(re.search(pattern, email).group(0))
    except AttributeError:
        pass

# Example 2 UUID
# Groups of lengths - 8-4-4-4-12
# UUID will involve numbers and characters


pattern = re.compile("(^\w{8})-(\w{4})-(\w{4})-(\w{4})-(\w{12})$")

uuid = [
    "a483a4ac-0233-480-b385-c86bff96a6d3",
    "c14#df7e-cdfc-4363-8262-eff9146ebe17",
    "752ab434-bdc3-4962-b926-0d0f1efda8a0",
    "3b9ebb2e+ae59-4340-9a1c-629618181c07",
    "344c8900-3717-4dc6-a977-0cb04afc2c01",
    "b6374ebe-ddc7-40c1-9cs2f-d8ed47469eac",
    "1de584a3-7ac5-493f-900b-a5abe9209b16",
    "c504fe4a-ad+8-4998-a144-0sdf9ae3ce32e3",
    "9a8327fa-109e-4dfa-ac48-817d1b788d46",
    "156ca980-abce-45c9-a348-6d09f208a6b8",
    "e87c26e2-c8d7-4fd3-ad6.-e6f29340b681",
    "61875c27-672f-450c-a233-1762385622bb",
    "f85a15c-9be5-4c8d-ae52-e82c7ff1a3ef",
]
for value in uuid:
    match = pattern.search(value)
    if match:
        print(match.group())


