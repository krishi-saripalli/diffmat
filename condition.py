import random
condition = []
for _ in range(512):
    row = []
    for _ in range(512):
        # r1 = round(random.uniform(1.5, 1.9),2)
        row.append(0.0)
    condition.append(row)

# Define the file path
file_path = r'C:\Users\Krishi Saripalli\AppData\Local\conda\conda\envs\diffmat\Lib\site-packages\diffmat\config\generators\crystal_2.yml'


# Convert the 'condition' list to a string
condition_string = str(condition)

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Modify line 19 (Python index 18)
if len(lines) >= 19:
    lines[18] = lines[18].split(':')[0] + ': ' + condition_string + '\n'

# Write the changes back to the file
with open(file_path, 'w') as file:
    file.writelines(lines)




