from random import randint


num_bot = randint(1, 10)
#print(num_bot)


answer_error = 'Наступного разу по щастить'

print('==================== ВГАДАЙ ЧИСЛО ====================')

print('Введіть число: ')

num_user = input()
print(f'Ваше число: {num_user}')

if num_user.isdigit():
    check_next_previous(num_user)

elif ',' or '.' in num_user:
    print(answer_error)

elif num_user.isalpha():
    print(answer_error)