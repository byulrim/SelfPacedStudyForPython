def print_message():
    print("CS101 is fantastic!", "Programming is fun!", sep="\n")


def repeat_message():
    for i in range(2):
        print_message()


repeat_message()
