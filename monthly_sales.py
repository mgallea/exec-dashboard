# monthly_sales.py

# Import Modules
import os
import pandas as pd
import matplotlib.pyplot as plot
import matplotlib.ticker as ticker

# Function to Convert Month Code to Month

def month_converter(monthCode):
	full_month = {'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return full_month[monthCode]

# Import the file
print("")
print ("Welcome to the Executive Sales Dashboard Helper Tool.")
print("To use this dashboard tool, please make sure your files are in a folder titled 'Data'")
print("")

while True:
	year = input("What year's sales data would you like to analyze? Please use YYYY: ")
	month = input("What month's sales data would you like to analyze? Please use MM: ")
	filename = "sales-"+year+month+".csv"
	filePath = "Data/"+filename

	if not os.path.isfile(filename):
		print("Uh oh! We're having some trouble finding that file. Please make sure you have access to the appropriate sales file.")
	else:
		break


# Open the CSV File
dataImport = pd.read_csv(filePath)

#Create a list of unique products
uniqueProducts = []
for x in dataImport['product']:
	if x not in uniqueProducts:
		uniqueProducts.append(x)
print(uniqueProducts)



print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")
