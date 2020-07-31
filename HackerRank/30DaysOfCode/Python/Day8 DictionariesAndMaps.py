N = int(input())
entry = [input().split() for _ in range(N)]
phoneBook = {name: number for name, number in entry}

while True:
    try:
        name = input()
        if name in phoneBook:
            print(f"{name}={phoneBook[name]}")
        else:
            print("Not found")
    except:
        break
