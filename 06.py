list1 = list(input("請輸入複數值").split(","))
max = ""
min = ""
for i in range(len(list1)):
    list1[i] = int(list1[i])
list1.sort()
for i in range(len(list1)):
    min += str(list1[i])
list1.reverse()
for i in range(len(list1)):
    max += str(list1[i])

print("最大值數列與最小值數列差值為：", int(max) - int(min))
