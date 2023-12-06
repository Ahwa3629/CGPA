def calculate_grade_points(grade):
    if grade >= 70:
        return 5
    elif grade >= 60:
        return 4
    elif grade >= 50:
        return 3
    elif grade >= 45:
        return 2
    elif grade >= 40:
        return 1
    else:
        return 0

# Step 1: Allowing the user to input courses and their credit units and grades
num_courses = int(input("Enter the number of courses you are offering: "))

# Initialize variables to keep track of total credit units and total weighted score
total_credit_units = 0
total_weighted_score = 0

# Step 2: Allowing the user to input scores for each course
for i in range(num_courses):
    course_name = input(f"Enter the name of course {i + 1}: ")
    credit_unit = int(input(f"Enter the credit unit for course {i + 1}: "))
    grade = int(input(f"Enter your grade for course {i + 1}: "))

    # Step 3: Calculate the Grade Points and Weighted Score for the course
    grade_points = calculate_grade_points(grade)
    weighted_score = grade_points * credit_unit

    # Step 4: Add the Weighted Score and Credit Units to the total
    total_weighted_score += weighted_score
    total_credit_units += credit_unit
    print(f'Your total credit Unit is:  {total_credit_units} \n')

# Step 5: Calculate the CGPA (Cumulative Grade Point Average)
cgpa = total_weighted_score / total_credit_units

# Step 6: Determine the class of degree based on CGPA
class_of_degree = ""
if cgpa >= 4.5 and cgpa <= 5.00:
    class_of_degree = "First class of Degree"
elif cgpa >= 3.5 and cgpa < 4.5:
    class_of_degree = "Second class upper of Degree"
elif cgpa >= 2.5 and cgpa < 3.5:
    class_of_degree = "Second class lower of Degree"
elif cgpa >= 1.5 and cgpa < 2.5:
    class_of_degree = "On Probation"
else:
    class_of_degree = "Failed and not meeting the academic requirements."

# Step 7: Print the CGPA and class of degree
print(f"Your CGPA is: {cgpa:.2f}")
print(f"You are awarded: {class_of_degree}")
