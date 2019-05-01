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
	month = month_converter('01')
	assert month == "January"
	month = month_converter('02')
	assert month == "February"
	month = month_converter('03')
	assert month == "March"
	month = month_converter('04')
	assert month == "April"
	month = month_converter('05')
	assert month == "May"
	month = month_converter('06')
	assert month == "June"
	month = month_converter('07')
	assert month == "July"
	month = month_converter('08')
	assert month == "August"
	month = month_converter('09')
	assert month == "September"
	month = month_converter('10')
	assert month == "October"
	month = month_converter('11')
	assert month == "November"
	month = month_converter('12')
	assert month == "December"