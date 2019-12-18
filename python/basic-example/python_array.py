print('-------------- TEST 1 --------------')

array = [1,2,3,4,5,'ABC', 'DEF', True]
print(array)
print(array[0:3]) # array[0] 부터 3개
print(array[4:]) # array[4] 부터 끝까지
print(array[-2]) # 뒤에서 -2 번째

print('-------------- TEST 2 --------------')

dictionary = {'abc' : 50, 'def' : 40}
print(dictionary)
print(dictionary['abc'])

dictionary_two = dict(abc=20)
print(dictionary_two)
print(dictionary_two['abc'])

print('-------------- TEST 3 --------------')

import random

coffee = ['아아','뜨아','라떼','믹스','핫초코']

co = random.choice(coffee)
print(co)

custom_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(custom_list[1:4])

numbers = list(range(1,10))
print(numbers)

numbers2 = list(range(10))
print(numbers2)

print('-------------- TEST 4 --------------')

# import random
menu = ['A','B','C','D','E']
phone_book = { menu[0] : '010-1111-1111',
              menu[1] : '010-2222-2222',
              menu[2] : '010-3333-3333',
              menu[3] : '010-4444-4444',
              menu[4] : '010-5555-5555'
}
choice_menu = random.choice(menu)
choice_number = phone_book[choice_menu]
print(choice_menu)
print(choice_number)
