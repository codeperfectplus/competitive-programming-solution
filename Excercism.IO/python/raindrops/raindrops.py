def convert(number):
    if(number%3==0) and (number%5==0) and (number%7==0):
        return "".join("PlingPlangPlong")
    if(number%3==0) and (number%5==0):
        return "".join("PlingPlang")
    if(number%3==0) and (number%7==0):
        return "".join("PlingPlong")
    if(number%5==0) and (number%7==0):
        return "".join("PlangPlong")
    elif(number%3==0):
        return "".join("Pling")
    elif(number%5==0):
        return "".join("Plang")
    elif(number%7==0):
        return "".join("Plong")
    else:
        return f"{number}"
