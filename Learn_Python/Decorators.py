def decor(func):
    def wrap(text):
        print("this is added by decorator at the beginning")
        func(text)
        print("this is added by decorator at the end")

    return wrap


@decor
def print_text(text):
    print("Your text is : {}".format(text))


user_text = input("Please enter text: ")
print_text(user_text)
