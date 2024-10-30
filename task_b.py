def letter():
    letter_grade = {'A', 'B', 'C', 'D', 'F'}
    try:

        grade_input = input("Enter a numerical value between 0 and 100: ")

        grade = float(grade_input)

        if grade < 0 or grade > 100:
            print("Error: Grades must be between 0 and 100")
            return 

        elif 80 <= grade <= 100:
            letter_grade = 'A'
        elif 60 <= grade < 80:
            letter_grade = 'B'
        elif 50 <= grade < 60:
            letter_grade = 'C'
        elif 40 <= grade < 50:
            letter_grade = 'D'
        elif 0 <= grade < 40:
            letter_grade = 'F'
        return

        print(f"Your grade is: {letter_grade}")
        return 
    
    except ValueError:
        print("Error: Please enter a number")
        return
letter()      