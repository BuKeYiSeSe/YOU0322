a = int(input("輸入N:"))
b = a//2+1
for i in range(2):
    if i == 0:
        for i in range(b):
            for j in range(b-i):
                print(" ", end='')
            for j in range(2*i+1):
                print("*", end='')
            print()
    else:
        for i in range(a-b, 0, -1):
            for j in range(b-i+1):
                print(" ", end='')
            for j in range(2*i-1):
                print("*", end='')
            print()
