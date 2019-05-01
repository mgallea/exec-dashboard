from functions import *

def test_to_usd():
	a = to_usd(3)
	assert a == "$3.00"
	b = to_usd(10)
	assert b == "$10.00"
	c = to_usd(1000)
	assert c == "$1,000.00"
	d = to_usd(1000000)
	assert d == "$1,000,000.00"

def test_month_converter():
	month = month_converter('1')
	assert month == "January"
	month = month_converter('2')
	assert month == "February"
	month = month_converter('3')
	assert month == "March"
	month = month_converter('4')
	assert month == "April"
	month = month_converter('5')
	assert month == "May"
	month = month_converter('6')
	assert month == "June"
	month = month_converter('7')
	assert month == "July"
	month = month_converter('8')
	assert month == "August"
	month = month_converter('9')
	assert month == "September"
	month = month_converter('10')
	assert month == "October"
	month = month_converter('11')
	assert month == "November"
	month = month_converter('12')
	assert month == "December"