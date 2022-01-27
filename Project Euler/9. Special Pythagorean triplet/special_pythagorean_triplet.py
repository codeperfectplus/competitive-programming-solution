""" 
# Problem Statement 

`Special Pythagorean triplet`
 """

def solver(num):
    for i in range(1, int(num/3)):
        for j in range(i+1, int(num/2)):
            k = num - i - j
            if i**2 + j**2 == k**2:
                return i * j * k

print(solver(1000))
# 200 * 375 * 425 = 31875000
# NOTE: This is a naive solution. It is possible to do this in a more efficient way.