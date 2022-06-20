a = int(input("輸入比數a:"))
win = {}
for i in range(a):
    medal,value=input("").split()
    win[medal]=value
for medal , value in win.items():
    print(medal,"牌得到",value,'面')