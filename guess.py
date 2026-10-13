import random

answer = random.randint(1, 100)  # 电脑随机出题：1-100 之间的整数
count = 0  # 计数器：记录猜了几次
print("我想好了一个 1-100 之间的数字，来猜猜看！")

while True:
    guess = input("请输入你猜的数字：")
    count += 1
    if not guess.isdigit():       # 输入的不是数字就重来
        print("请输入一个有效的数字！")
        continue
    guess = int(guess)            # 字符串转成整数才能比大小
    if guess > answer:
        print("大了！")
    elif guess < answer:
        print("小了！")
    else:
        print(f"恭喜猜中！答案是 {answer}，你一共猜了 {count} 次")
        break