# Employee salary data
employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}

# Step 1: Find highest salary
highest_salary = max(employees.values())

# Step 2: Find employee with that salary
for name, salary in employees.items():
    if salary == highest_salary:
        print(f"Highest Salary: {name} - {salary}")
