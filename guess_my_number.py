import random

quiz_number = random.randint(1, 100)

# print(quiz_number)

print("숫자를 맞춰보세요(1 ~ 100)", "포기하시려면 'Enter' Key를 누르세요", sep="\n")

while 1:
    user_input_number = input()
    if user_input_number == "":
        print("숫자 찾기를 포기하셨습니다.", f"찾는 숫자는 {quiz_number} 였습니다.", sep="\n")
        break

    user_input_number = int(user_input_number)

    if user_input_number > quiz_number:
        print("숫자가 너무 큽니다.")
    elif user_input_number < quiz_number:
        print("숫자가 너무 작습니다.")
    else:
        print(f"정답입니다. 입력한 숫자는 {user_input_number} 입니다.")
        break
