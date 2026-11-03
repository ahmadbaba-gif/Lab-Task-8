


                 Question 1: (Factorial)

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is defined only for non-negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


                 Question 2: (Keyword arguments)

def student_info(name, roll_no, course, grade="N/A"):
    """Display student information using keyword arguments."""
    print("----- Student Information -----")
    print(f"Name    : {name}")
    print(f"Roll No : {roll_no}")
    print(f"Course  : {course}")
    print(f"Grade   : {grade}")


                  Question 3: (*args)

def sum_numbers(*args):
    """Return the sum of any number of numeric arguments."""
    total = 0
    for num in args:
        total += num
    return total


                  Question 4: (**kwargs)

def employee_info(**kwargs):
    """Display employee information passed as keyword arguments."""
    print("----- Employee Information -----")
    for key, value in kwargs.items():
        print(f"{key.replace('_', ' ').title()} : {value}")


                Question 5: (Password checker)

def check_password(password):
    """
    Check if a password:
      - has at least 8 characters
      - has at least one uppercase letter
      - has at least one lowercase letter
      - has at least one digit
      - has at least one special character
    Returns (True, "message") or (False, "message").
    """
    errors = []

    if len(password) < 8:
        errors.append("at least 8 characters")
    if not any(ch.isupper() for ch in password):
        errors.append("at least one uppercase letter")
    if not any(ch.islower() for ch in password):
        errors.append("at least one lowercase letter")
    if not any(ch.isdigit() for ch in password):
        errors.append("at least one digit")
    if not any(ch in string.punctuation for ch in password):
        errors.append("at least one special character")

    if errors:
        return False, "Weak password. Missing: " + ", ".join(errors)
    return True, "Strong password!"


if __name__ == "__main__":
     Q1
    print("Q1: Factorial of 5 =", factorial(5))

    Q2
    print("\nQ2:")
    student_info(name="Ali", roll_no=101, course="Python", grade="A")

     Q3
    print("\nQ3: Sum =", sum_numbers(10, 20, 30, 40))

     Q4
    print("\nQ4:")
    employee_info(name="Sara", employee_id=7, department="IT", salary=50000)

     Q5
    print("\nQ5:")
    for pwd in ["abc", "password123", "Password123", "Pass@123word"]:
        ok, msg = check_password(pwd)
        print(f"{pwd!r:16} -> {msg}")
      
