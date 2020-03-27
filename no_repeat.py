def check_guess_user(number):
    list_guess_check = [int(i) for i in str(number)]
    for i in range(len(str(number))):
        for j in range(i+1,len(str(number))):
            if list_guess_check[i] == list_guess_check[j]:
                print("number {} is repeated you can not guess a number with repeated digit, try again".format(list_guess_check[i]))
                return False
    return True


flag = True


def check_guess_cpu(number):
    list_guess_check = [int(i) for i in str(number)]
    for i in range(len(str(number))):
        for j in range(i+1,len(str(number))):
            if list_guess_check[i] == list_guess_check[j]:
                return False
    return True


flag = True


