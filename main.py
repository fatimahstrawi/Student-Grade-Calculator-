print("Welcome to Student Grade Calculator!")

try:
    name = input("Enter the student's name: ")

    num_subjects = int(input("How many subjects? "))

    if num_subjects <= 0:
        print("Error: Enter at least one subject.")
    else:
        total = 0
        valid_grades = True

        for i in range(num_subjects):
            try:
                grade = float(
                    input(f"Enter grade for subject {i + 1}: ")
                )

                if grade < 0 or grade > 100:
                    print("Error: Grades must be between 0 and 100.")
                    valid_grades = False
                    break

                total += grade

            except ValueError:
                print("Error: Please enter a valid number for the grade.")
                valid_grades = False
                break

        if valid_grades:
            average = total / num_subjects

            if average >= 90:
                letter_grade = "A"
            elif average >= 80:
                letter_grade = "B"
            elif average >= 70:
                letter_grade = "C"
            elif average >= 60:
                letter_grade = "D"
            else:
                letter_grade = "F"

            print("\n--- Student Results ---")
            print("Student Name:", name)
            print("Average Grade:", round(average, 2))
            print("Final Grade:", letter_grade)

except ValueError:
    print("Error: Please enter a valid number of subjects.")
    