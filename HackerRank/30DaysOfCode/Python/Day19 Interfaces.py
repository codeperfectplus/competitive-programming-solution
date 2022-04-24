class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        factors = []
        factors.append(n)
        for i in range(1, int(n/2)+ 1):
            if n % i == 0:
                factors.append(i)
        
        return sum(factors)
    

n = int(input("Please enter the number: "))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)