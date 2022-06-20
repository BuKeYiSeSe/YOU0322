teacher = int(input("輸入班任教班級數量:"))
class1 = []
for i in range(teacher):
    class1.append(input("輸入班級人數:"))
class1 = list(map(int, class1))
for i in range(teacher-1):
    if class1[i+1] > class1[i]:
        buy = class1[i+1]
print(buy)
