import random
import no_repeat
flag=True
while flag:
    guess = random.randint(10000, 99999)
    if no_repeat.check_guess_cpu(guess) == False:
        guess = random.randint(10000, 99999)
        continue
    flag = False
flag =True
print(guess)
guess_list_items=[]

while flag:
    round_string = input(print("guess your 5 digit number? "))

    try:
        user_guess = int(round_string)
        if no_repeat.check_guess_user(round_string) == False:
            continue
    except (TypeError, ValueError):
        print("This is not an integer number. Please enter a valid number")

    lst_user_guess = [int(i) for i in str(user_guess)]
    lst_guess = [int(i) for i in str(guess)]
    if lst_user_guess== lst_guess:
        print("you won, the number was {}".format(guess))
        flag= False
        break

    for i in range (0, 5):
        for j in range (0,4):
            if user_guess[i] == guess[j]:
                guess_list_items.append("x")
            if user_guess[i]== guess[j] and i==j:
                guess_list_items.append("+")
    print(guess_list_items)

