from datetime import date

def calculate_age(birthday):
    today = date.today()

    # Check if the birthdate is in the future
    if today < birthday:
        return "Invalid birthdate. Please enter a valid date."

    # Start with full year, month, day differences
    years = today.year - birthday.year
    months = today.month - birthday.month
    days = today.day - birthday.day

    # Adjust days and months if negative
    if days < 0:
        months -= 1
        # Borrow days from previous month
        prev_month = (today.month - 1) or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days += (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return f"Age: {years} years, {months} months, and {days} days"

if __name__ == "__main__":
    print("Age Calculator by Python")

    try:
        birthYear = int(input("Enter the birth year: "))
        birthMonth = int(input("Enter the birth month: "))
        birthDay = int(input("Enter the birth day: "))
        dateOfBirth = date(birthYear, birthMonth, birthDay)
        age = calculate_age(dateOfBirth)
        print(age)
    except ValueError:
        print("Invalid input. Please enter valid integers for the year, month, and day.")
