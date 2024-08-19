import pandas as pd
from datetime import datetime

# Example function to detect students (replace with actual YOLOv5 detection logic)
def detect_students():
    # Dummy data: Replace with actual detection logic
    detected_students = ['1', '2']  # List of detected student IDs for the current date
    return detected_students

# Load the existing CSV file if it exists, otherwise create a new DataFrame
try:
    df = pd.read_csv('attendance.csv')
except FileNotFoundError:
    # Initialize DataFrame if CSV does not exist
    data = {
        'ID': ['1', '2', '3', '4', '5'],
        'Name': ['Alice', 'Bob', 'Charlie', 'Booob', 'Chafrlie']
    }
    df = pd.DataFrame(data)

# Get the current date
current_date = datetime.now().strftime('%d-%m-%Y')

# Check if the current date column already exists
if current_date not in df.columns:
    # Initialize new date column with 0 (not present)
    df[current_date] = [0] * len(df)

    # Detect students for the current date
    detected_ids = detect_students()
    
    # Update attendance based on detections
    for idx, student_id in enumerate(df['ID']):
        if student_id in detected_ids:
            df.loc[idx, current_date] = 1

    # Save the updated DataFrame to a CSV file
    df.to_csv('attendance.csv', index=False)
    print(f"Attendance updated for {current_date}")
else:
    print(f"Attendance for {current_date} is already recorded")

print(df)
