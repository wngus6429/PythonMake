# 타입을 바꿔버림
age = "18"
print(age)
print(type(age))
n_age = int(age)
print(type(n_age))
n_age = 100
print(n_age)

# function


def say_hello(game):
    print("hello " + game)  # 들여쓰기 tab으로 하면 됨.
    print("galic " + game)


say_hello("rule")


def plus(a, b=3):
    print(a + b)


plus(5)


def say_helloo(name="powerful"):
    print("hello", name)


say_helloo()
say_helloo("juhyun")
