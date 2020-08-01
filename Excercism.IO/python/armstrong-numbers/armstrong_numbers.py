def is_armstrong_number(number):
    num = str(number)
    exp = len(num)
    return number == sum([int(i)**exp for i in num])