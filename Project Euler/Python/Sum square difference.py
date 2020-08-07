def difference(n):
    """
        This program will return differnce between square of sum and sum of square. 
    """
    sumOfSquare = 0
    squareOfSum = 0
    for i in range(n+1):
        squareOfSum += i  
        sumOfSquare += i ** 2
    return squareOfSum ** 2 - sumOfSquare
        
if __name__ == "__main__":
    print(difference(100))