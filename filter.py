numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)

num = [-1, 1, 2, 3, 5 ,"이성남", "멋쟁이", 9, 8, ""]
result = list(filter(lambda x: type(x) == int, num))
print(result)

sum = 0
for i in range(len(result)):
    sum = sum + result[i]

print(sum)

my_list = ["호랑이", "코끼리", "고구마", 19, 20, 30, -1, "감자", 3, "토란"]

changed_list = list(filter(lambda x : type(x) == str, my_list))
print(changed_list)

my_list = ["호랑이", 0.1, -1, 11, "감자", "토란", 12.9, 15.1569898143748, "고양이"]
changed_list = list(filter(lambda x : type(x) == float, my_list))
print(changed_list)



