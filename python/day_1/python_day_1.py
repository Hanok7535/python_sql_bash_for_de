# 1. Print a welcome message for your data pipeline
print("Welcome to the Data Engineering Challenge!")
# output: Welcome to the Data Engineering Challenge!


# 2.Create a variable called source_file &
#   assign it the value 'data.csv'. Print it.
source_file = "data.csv"
print(source_file)
# output: data.csv

# 3.Simulate reading a file by printing: 
# Reading data from data.csv using the source_file variable.
source_file = "data.csv"
print(f"Reading data from {source_file}")
# output: Reading data from data.csv

#4. Create two variables records_file1 = 1200 &
#   records_file2 = 800. Print their total.
records_file1 = 1200
records_file2 = 800
total_records = records_file1 + records_file2
print("Total records:", total_records)

#5. Take input from the user for a file name and print: Processing <filename>
file_name = input("Enter the file name to process ")
print(f"Processing {file_name}")
#prompt: Enter the file name to process
#input: data_engineering.csv
#output: Processing data_engineering.csv

#6. Write a conditional check: 
# If a batch has more than 1000 records, print “Large batch”.
batch_size = int(input("Enter batch size "))
if batch_size > 1000:
    print("Large batch")
else:
    print("Normal batch")
#prompt: Enter batch size
#input: 5000
#outpuy: Large batch

#7. Create a list of filenames and print each one
file_list = ["users.csv", "orders.csv", "products.csv"]
for file in file_list:
    print(file)
#output:users.csv
#orders.csv
#products.csv


#8.  Create a dictionary storing filenames as keys and record count as values. Print it.
file_stats = {
    "users.csv": 300,
    "orders.csv": 500,
    "products.csv": 200
}
print(file_stats)
#output: {'users.csv': 300, 'orders.csv': 500, 'products.csv': 200}


#9.Print pipeline steps using a for-loop
for step in range(1, 6):
    print(f"Step {step} complete")
#output: Step 1 complete
# Step 2 complete
# Step 3 complete
# Step 4 complete
# Step 5 complete

#10. Use string methods to check if a filename ends with .csv
filename = "data_backup.csv"
if filename.endswith(".csv"):
    print("valid csv file")
else:
    print("invalid file type")