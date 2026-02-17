# Attendance record
attendance = ["P", "P", "A", "P", "P"]

# Step 1: Count present days
present_days = 0

for day in attendance:
    if day == "P":
        present_days += 1

# Step 2: Calculate percentage
total_days = len(attendance)
percentage = (present_days / total_days) * 100

# Step 3: Display result
print("Attendance Percentage:", percentage)
