list1 =["鼠(rat)","牛(ox)","虎(tiger)","兔(rabbit)","龍(dragon)","蛇(snake)","馬(horse)","羊(sheep)","猴(monkey)","雞(chicken)","狗(dog)","豬(pig)"]
year = int(input("請輸入西元年："))
Y = (year - 2008) % 12

print(list1[Y])
