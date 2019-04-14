#  coding:utf-8
#  输入，本文件不能 ctrl+b 运行
#  需要 python hardway/ex11.py运行

# 你多大了？
print("How old are you?", end=" ")
age = input()
# 你有多高？
print("How tall are you?", end=" ")
height = input()
# 你体重多少？
print("How much do you weigh?", end=" ")
weight = input()

# 你是“ ”身高“ ”体重“ ”
print(f"So, you're {age} old, {height} tall, {weight} heavy.")
