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
print("")
print("To use this dashboard tool, please make sure your files are in a folder titled 'Data'")
print("")

while True:
	year = input("What year's sales data would you like to analyze? Please use YYYY: ")
	month = input("What month's sales data would you like to analyze? Please use MM: ")
	filename = "sales-"+year+month+".csv"
	filePath = "Data/"+filename

	if not os.path.isfile(filePath):
		print("Uh oh! We're having some trouble finding that file. Please make sure you have access to the appropriate sales file.")
	else:
		break


# Open the CSV File
dataImport = pd.read_csv(filePath)
uniqueCounter = 0

#Create a list of unique products
uniqueProducts = []
productPrice = []
for x in dataImport['product']:
	if x not in uniqueProducts:
		uniqueProducts.append(x)
		uniqueCounter = uniqueCounter + 1

# Calculate Sales Price by Product
salesPrice = dataImport.groupby(dataImport['product']).sum()
salesPrice = salesPrice.sort_values(by=['sales price'], ascending=False)

# Convert the Month Header
monthName  = month_converter(month)

# Total Sales
totalSalesPrice = salesPrice['sales price'].sum()

print("")
print("")
print("-----------------------")
print("MONTH: " + monthName + " " + year)

print("-----------------------")

print("-----------------------")
print("TOTAL MONTHLY SALES: $" + str("%0.2f" % totalSalesPrice))

print("-----------------------")
print("TOP SELLING PRODUCTS:")

# print out the ranked products and total sales
counter = 0
while counter < uniqueCounter:
	print(str(counter + 1) + ") " + str(salesPrice.index[counter]).ljust(20) + "   $"  + str("%0.2f" % salesPrice.iloc[counter][2]).rjust(8))
	counter = counter + 1

print("-----------------------")
print("VISUALIZING DATA...")

# Create a list with all the item names
visIndex = salesPrice.index.tolist()

# Create a list with all the prices
x = 0
visPrice = []
while x < uniqueCounter:
	visPrice.append(salesPrice.iloc[x][2])
	x = x + 1

# Create the plot to display
fig, diagram = plot.subplots()
#fig.set_figheight(10)
#fig.set_figwidth(5)
fig.set_size_inches(10,5,forward = True)
diagram.barh(visIndex,visPrice)


# Format the plot
tickMark = ticker.StrMethodFormatter('${x:,.2f}')
diagram.set_ylabel("Products")
diagram.set_xlabel("Dollars")
diagram.set_title("Total Sales - " + monthName + " " + year)
diagram.xaxis.set_major_formatter(tickMark)

# Format the text
for h, j in enumerate(visPrice):
	diagram.text(j , h , "   ${0:,.2f}".format(j))

# Display the plot
plot.show()
