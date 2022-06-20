id = input("input your StudentId:")
data = [["123","Tom DTGD"],["456","Cat CSIE"],["789","Nana ASIE"],["321","Lim DBA"],["654","Won FDD"]]

for i in range(len(data)):
    if id == data[i][0]:
        print("StudentData:", id, data[i][1])
