a = int(input("輸入比數a:"))
win=[]
for i in range(a):
    metal_value=input().split()
    win.append(metal_value)
for i in range(a):
    print(win[i][0],'牌得到',win[i][1],'面')