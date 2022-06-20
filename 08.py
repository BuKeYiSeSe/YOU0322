op = (input("請輸入一正整數:"))
ed = input("請輸入數列(用空白隔開):").split()
r = 1
for i in ed:
    if ed.count(i) > r :
        r = ed.count(i)
        Maxr = i
if i == 1:
    print("每個數字剛好只出現 1 次")
else :
    print(f"最大出現次數的數字為:{Maxr}")
    print(f"出現次數為:{r}")