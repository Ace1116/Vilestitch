def sq(x):
    return x**2

result = sq(5)
print("result",result)



lst=[1, 2, 3, 4, 5]
squared =list(map(lambda x: x**2, lst))
print("squared", squared)

numbers=[1, 2, 3, 4, 5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("even_numbers", even_numbers)`




 import os
def get_fruit_list():
    return ["apple", "banana", "cherry"]