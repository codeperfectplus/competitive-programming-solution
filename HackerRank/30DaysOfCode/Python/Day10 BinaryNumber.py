if __name__ == "__main__":

    def func(num):
        return num[2:]


n = int(input().strip())
a = max(func(bin(n)).split("0")).count("1")
print(a)
