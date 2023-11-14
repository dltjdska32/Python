problem_list = ["고구마", "감자", 1, 2, 3, 0.1, "호랑이", "괴물", 3, 12.42424, "토란", 4]
print("문제 - 아래의 리스트의 요소 중 단어로 된 요소를 입력하세요.")
print(*problem_list, sep=", ")

#sorted()함수는 정렬된 새로운 리스트를 만들어 낸다. <-> sort()함수의 경우 일시적으로 소트시킬뿐 새로운 리스트를 만들지 않는다.
result_list = sorted(list(filter(lambda x : type(x) == str, problem_list)))

count = 0
for i in range(len(result_list)):
    if(type(result_list) == str):
        count += 1



while(1):
    print()
    my_stringList = input("답을 입력하세요(단어는 공백으로 구분합니다.) : ")
    my_list = sorted(list(my_stringList.split(" ")))
    
    if(my_list != result_list):
        print()
        print("오답입니다. 다시입력하세요")
        continue
    
    if(my_list == result_list):
        print("정답입니다.")
        break


