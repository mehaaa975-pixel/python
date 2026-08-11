def get_mark():
    English = int(input("Enter English mark: "))
    Maths = int(input("Enter Maths mark: "))
    science = int(input("Enter Science mark: "))
    social = int(input("Enter Social mark: "))
    computer = int(input("Enter Computer mark: "))

    return English, Maths, science, social, computer


def total_mark(English, Maths, science, social, computer):
    return English + Maths + science + social + computer


def calculate_average(total_mark):
    avg = total_mark / 5
    return avg


def find_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"


def display_result(total, avg, grade):
    print("\nStudent Result:")
    print("Total mark:", total)
    print("Average mark:", avg)
    print("Grade:", grade)

    if grade == "Fail":
        print("Result: Fail")
    else:
        print("Result: Pass")


English, Maths, science, social, computer = get_mark()

total = total_mark(English, Maths, science, social, computer)

avg = calculate_average(total)

grade = find_grade(avg)

display_result(total, avg, grade)






   

 
      







