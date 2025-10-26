import random

print("************************欢迎来到大数据241班37号张竣华的猜数字游戏************************")
print()
print("——————————————————————————————————————接下来游戏开始————————————————————————————————————")
n = 1
playing = True
while playing:
    a = random.randint(1, 100)

    while True:
    
        try:
            b = int(input("请输入你猜的数字（1-100）："))
        except ValueError:
            print("输入无效，请输入一个整数。")
            continue
        if b < a:
            print("你猜的数字太小了，请再试一次。")
            n += 1
        elif b > a:
            print("你猜的数字太大了，请再试一次。")
            n += 1
        else:
            print("恭喜你，猜对了！")
            print(f"你一共猜了{n}次。")
            n = 12
            break

    while True:
        choice = input("是否决定继续游戏？(Y/N)").upper()
        if choice.upper() == "Y":
            print("——————————————————————————————————————游戏继续————————————————————————————————————")
            break
        elif choice.upper() == "N":
            print("感谢你的参与，游戏结束！")
            playing = False
            break
        else:
            print("666输入有误，请输入Y或N:")