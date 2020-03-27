import random
import no_repeat

flag = True
while flag:
    guess = random.randint(10000, 99999)
    if no_repeat.check_guess_cpu(guess) == False:
        guess = random.randint(10000, 99999)
        continue
    flag = False
flag = True
print(guess)


while flag:
    round_string = input(print("guess your 5 digit number? "))
    guess_list_items = []
    guess_list_number = []
    try:
        user_guess = int(round_string)
        if no_repeat.check_guess_user(round_string) == False:
            continue
    except (TypeError, ValueError):
        print("This is not an integer number. Please enter a valid number")
        continue
    lst_user_guess = [int(i) for i in str(user_guess)]
    lst_guess = [int(i) for i in str(guess)]
    print(lst_user_guess)
    print(lst_guess)
    if lst_user_guess == lst_guess:
        print("you won, the number was {}".format(guess))
        flag = False
        break

    for i in range(len(lst_user_guess)):
        for j in range(len(lst_guess)):

            if lst_user_guess[i] == lst_guess[j] and i == j:
                guess_list_number.append(lst_user_guess[i])
                guess_list_items.append("+")


            if lst_user_guess[i] == lst_guess[j]:
                if lst_user_guess[i] not in guess_list_number:
                    guess_list_items.append("x")

    print(guess_list_items)


