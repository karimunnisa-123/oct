# grade_calculator.py
# -------------------
# A program to calculate total marks, average and grade for a student.

def calculate_grade(average):
    """Function to calculate grade based on average marks."""
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

def main():
    print("===== STUDENT GRADE CALCULATOR =====")
    
    # Get student details
    name = input("Enter student's name: ")
    roll_no = input("Enter roll number: ")

    # Get marks for 5 subjects
    subjects = ["Math", "Science", "English", "Computer", "Social Studies"]
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("❌ Marks must be between 0 and 100. Try again.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

    # Calculate total and average
    total = sum(marks)
    average = total / len(subjects)
    grade = calculate_grade(average)

    # Display results
    print("\n===== RESULT =====")
    print(f"Name       : {name}")
    print(f"Roll No.   : {roll_no}")
    print(f"Total Marks: {total:.2f}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")
    print("===============================")

    # Give a message
    if grade == 'F':
        print("⚠️ Better luck next time!")
    else:
        print("🎉 Congratulations! You passed successfully.")

# Run the program
if __name__ == "__main__":
    main()
