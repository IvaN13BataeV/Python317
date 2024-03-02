import re


def validate_password(psw):
    return re.findall(r"^[0-9A-Za-z-@_]{6,18}$", psw)


print(validate_password('my-p@ssw0rd'))  # подходит по символам и по длине
print(validate_password('115-X888_p@s$'))  # не подходит по символам
print(validate_password('Test-passwOrD11111_n@n'))  # не подходит по длине
