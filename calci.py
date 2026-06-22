# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Keep practicing and improving! 💪"
    else:
        return "F", "Don't give up! Try harder next time! 📚"


# Get student name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT")
print("--------------------")
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)