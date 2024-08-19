# import pandas as pd

# # Load the CSV file
# file_path = 'attendance.csv'  # Replace with your CSV file path
# df = pd.read_csv(file_path)

# # Specify the column you want to read
# column_name = 'ID'  # Replace with the name of the column you want to read

# # Read the column
# column_data = df[column_name]
# pp=str(column_data)
# # Print the column data
# print(pp)


# import pandas as pd

# # Load the CSV file
# file_path = 'attendance.csv'  # Replace with your CSV file path
# df = pd.read_csv(file_path)

# # Specify the column you want to search in and the value you're looking for
# column_name = 'Name'  # Replace with the name of the column
# search_value = 'Alice'  # Replace with the value you're searching for

# # Search for the value in the specified column
# matching_rows = df[df[column_name] == search_value]
# indexx= matching_rows.index
# pp =matching_rows[column_name]
# # Print the matching rows
# print(pp)
# print(indexx)




# import pandas as pd

# # Load the CSV file
# file_path = 'attendance.csv'  # Replace with your CSV file path
# df = pd.read_csv(file_path)


# search_value = 'Alice'
# column_name = 'Name'
# matching_rows = df[df[column_name] == search_value]
# row_index= matching_rows.index
# row_index=int(row_index)
# # Specify the row index and column name you want to edit
#   # Replace with the index of the row you want to edit
#   # Replace with the name of the column you want to edit
# column_name0="22-05-2024"
# # Set the new value (either 1 or 0)
# new_value = 1  # Replace with the value you want to set (1 or 0)

# # Update the cell's value
# df.at[row_index, column_name0] = new_value

# # Save the modified DataFrame back to the CSV file
# df.to_csv(file_path, index=False)

# print(f"Updated row {row_index} in column '{column_name0}' with value {new_value}.")





import pandas as pd

# Load the CSV file
file_path = 'attendance.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Specify the value you're looking for and the column to search in
search_value = 'Omar'
column_name = 'Name'
matching_rows = df[df[column_name] == search_value]

# Ensure there's exactly one matching row and get its index
if len(matching_rows) == 1:
    row_index = matching_rows.index[0]
    # Specify the column name you want to edit
    column_name0 = '22-05-2024'  # Replace with the name of the column you want to edit

    # Set the new value (either 1 or 0)
    new_value = 1  # Replace with the value you want to set (1 or 0)

    # Update the cell's value
    df.at[row_index, column_name0] = new_value

    # Save the modified DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

    print(f"Updated row {row_index} in column '{column_name0}' with value {new_value}.")
else:
    print(f"No unique match found for {search_value}. Please check your data.")
