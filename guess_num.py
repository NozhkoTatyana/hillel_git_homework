from random import randint


num_bot = randint(1, 10)
print(num_bot)


answer_error = 'Наступного разу по щастить'

print('==================== ВГАДАЙ ЧИСЛО ====================')

print('Введіть число: ')

num_user = input()
print(f'Ваше число: {num_user}')


def check_next_previous(num_user):
    num = abs(int(num_user) - num_bot)

    if (int(num_user) < num_bot or int(num_user) > num_bot) and num != 1 or\
     (int(num_user) < 1 or int(num_user) > 10):
        print(answer_error)

    elif int(num_user) == num_bot:
        print('ВІТАЮ, ВИ ЦЕ ЗРОБИЛИ')

    else:
        print("ВИ БУЛИ МАКСИМАЛЬНО БЛИЗЬКО")


if num_user.isdigit():
    check_next_previous(num_user)

elif ',' or '.' in num_user:
    print(answer_error)

elif num_user.isalpha():
    print(answer_error)