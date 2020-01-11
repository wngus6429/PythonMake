# def plus(a, b):
#     if type(b) is str:
#         return None
#     else:
#         return a + b

# plus(12, "10")

def plus(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None
print(plus(12, 1.2))

def age_check(age):
    print(f"you are {age}")
    if age <= 18:
        print("you can drink")
    elif age == 18:
        print("you are new to this!")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")
    
age_check(20)

