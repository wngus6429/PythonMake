# list는 value 들을 열거하는 것이다.

days = ["mon", "tue", "wed", "thir", "fri"]

# print(type(days))

print("mon" in days)  # 존재의 확인 true 나옴
print(days[3])  # days 안에 4번째
print(days)
days.append("sat")
days.reverse()
print(days)

# tuple 은 내용을 바꿀수 없는 list 이다.
# 그냥 괄호로 닫으면 됨
days = ("mon", "tue", "wed", "thir", "fri")
print(type(days))

juhyun = {
    "name": "Park juhyun",
    "age": 28,
    "korean": True,
    "fav_food": ["kimchi", "sashimi"]}
print(juhyun["name"])
juhyun["handsome"] = True
print(juhyun)
