def check_pesel(pesel):
    if not pesel or len(pesel) != 11 or not pesel.isnumeric():
        return "Incorrect format"
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum_pesel = sum(int(a) * b for a, b in zip(pesel[:-1], multipliers))
    # sum_pesel = 0
    # for order_number, digit in enumerate(pesel):
    #     if order_number in [0, 4, 8]:
    #         sum_pesel += int(digit) * 1
    #     elif order_number in [1, 5, 9]:
    #         sum_pesel += int(digit) * 3
    #     elif order_number in [2, 6]:
    #         sum_pesel += int(digit) * 7
    #     elif order_number in [3, 7]:
    #         sum_pesel += int(digit) * 9
    #     else:
    #         continue
    # print(sum_pesel)
    checksum = 0 if sum_pesel % 10 == 0 else 10 - sum_pesel % 10

    if checksum == int(pesel[-1]):
        return f"PESEL number {pesel} is correct"
    else:
        return f"PESEL number {pesel} is incorrect"


print(check_pesel("02070803628"))

