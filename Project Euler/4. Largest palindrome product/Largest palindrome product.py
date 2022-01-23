def largestPalindrome(bot, top):
    z = 0
    for i in range(top, bot, -1):
        for j in range(top, bot, -1):
            if isPalindrome(i*j):                
                if i * j > z:
                    z = i * j
    return z
    

def isPalindrome(num):
    return str(num) == str(num)[::-1]

print(largestPalindrome(100,999))