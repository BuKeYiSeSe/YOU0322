m = int(input("輸入M:"))
d = int(input("輸入D:"))
s = (m*2+d)%3
if s == 0 :
    print("Nomal")
elif s == 1:
    print("Lucky")
else:
    print("SuperLucky")