ATM = []
ATM.append(['123','456','9000'])
ATM.append(['456','789','5000'])
ATM.append(['789','888','6000'])
ATM.append(['336','558','10000'])
ATM.append(['775','666','12000'])
ATM.append(['566','221','7000'])

N = int(input("輸入查詢組數:"))
for i in range(N):
    s = input("輸入帳號&密碼:").split()
    for j in range(len(ATM)):
        if s[0] == ATM[j][0] and s[1] == ATM[j][1]:
            print(ATM[j][2])
            break
        else:
            print('error')
            break