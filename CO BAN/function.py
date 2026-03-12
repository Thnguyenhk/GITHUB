# EXERCISE: STUDENT GRADE MANAGEMENT
# Task: Complete the functions below as described to make the program work correctly.

def calculate_average(math, physics, chemistry):
    """
    Function to calculate the average score of 3 subjects.
    Formula: (Math + Physics + Chemistry) / 3
    """
    # TODO: Calculate the sum and divide by 3, then return the result
    average = (math + physics + chemistry) / 3
    return round(average, 2)

def get_classification(average):
    """
    Function to classify students based on their average score:
    - >= 8.0: Excellent
    - >= 6.5: Good
    - >= 5.0: Average
    - Else: Poor
    """
    # TODO: Use if-elif-else structure to return the classification string
    if average >= 8.0:
        return "Excellent"
    elif average >= 6.5:
        return "Good"
    elif average >= 5.0:
        return "Average"
    else:
        return "Poor"
    
def check_scholarship (average):
    if average > 9.0:
        return True
    else:
        return False    

def display_result(name, average, classification):
    """
    Function to print the final result notification.
    """
    print("-" * 30)
    print(f"Student: {name}")
    print(f"Average Score: {average}")
    print(f"Classification: {classification}")
    if check_scholarship (average):
        print(f"{name} got a scholarship!")
    else:
        print(f"{name} has no scholarship.")
    print("-" * 30)

# --- MAIN PROGRAM ---
# Sample data for a student
student_name = "Nguyen Van An"
math_score = 9.5
physics_score = 8.5
chemistry_score = 9.5

# Step 1: Call the function to calculate the average score
avg_score = calculate_average(math_score, physics_score, chemistry_score)

# Step 2: Call the function to get classification
rank = get_classification(avg_score)

# Step 3: Display the results
display_result(student_name, avg_score, rank)





# EXTRA PRACTICE:
# 1. Try changing the student's scores to see how the classification changes.
# 2. Write an additional function 'check_scholarship(average)' that returns True if average > 9.0.