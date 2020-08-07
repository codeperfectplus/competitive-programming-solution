def convert(number):
    sounds = ""
    if number % 3 == 0:
        sounds += "Pling"
    if number % 5 == 0:
        sounds += "Plang"
    if number % 7 == 0:
        sounds += "Plong"
    if sounds == "":
        return str(number)
    else:
        return sounds