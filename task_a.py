days = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday' : 3,
        'Thursday': 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }
day_selected = input("Please enter a day of the week: ").strip()


day_formatted = day_selected.capitalize()

if day_formatted in days:
    print(f"{day_formatted} is day {days[day_formatted]}")
else:
    print("Please enter a valid day")