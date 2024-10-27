def right():
    while True:
        password = input("Enter a password: ")
        
        if len(password) < 8:
            print("Your password must contain at least 8 characters, and a mix of letters and numbers")
            return
        elif not any(char.isdigit() for char in password):
            print("Your password must contain at least 8 characters, and a mix of letters and numbers")
            return

        elif not any(char.isalpha() for char in password):
            print("Your password must contain at least 8 characters, and a mix of letters and numbers")
            return
        else:
            print("Your password is valid")
            break
right()