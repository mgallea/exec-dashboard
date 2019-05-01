import locale

#Convert to USD Format
def to_usd(value):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8') 
        s = locale.currency(value, grouping=True)
        return s

# Function to Convert Month Code to Month

def month_converter(monthCode):
	full_month = {'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return full_month[monthCode]