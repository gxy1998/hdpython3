# coding=utf-8
# 字符串与文本

types_of_people = 10
x = f"There are {types_of_people} types_of_people"

binary = "binary"
do_not = "don't"
y = f"Those who knows {binary} and Those who {do_not}"
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w ="This is the left side of..."
e = "a string with a right side"
print(w + e)
