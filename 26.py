while True:
    a = input("輸入字串(end結束):")
    if a == 'end':
        print("終止檢測")
        break
    else:
        list1 = []
        x = 0
        b = input("檢測單一字元:")
        for i in range(len(a)):
            list1.append(a[i])
        for i in range(len(list1)):
            if b == list1[i]:
                x += 1
        print("字元%s出現次數為:%d" %(b, x))