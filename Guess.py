from random import randint

answer = 'yes'

while str(answer) != 'No' or answer != 'n' or answer != 'no':
    count = 0

    #computer take a random number from 1 to 999
    guess_num = randint(1,999)

    #take number from the user
    user_num_input = input("Can You guss What number iam thinking ? : ")

    #cheak if the number is low , high or too low , too high
    while int(user_num_input) != guess_num:
        if int(user_num_input) > guess_num:
            print("The number you guessed is high")
        elif int(user_num_input) < guess_num:
            print("The number you guessed is low")
        count+=1
        user_num_input = input("Give Another Try ? : ")
    else:
        print("You guessed it ! :D it took you {} trys".format(count))
        answer = input("Do you Want To play Agine ! :(yes/no) or (y/n) ")
        print(answer)
