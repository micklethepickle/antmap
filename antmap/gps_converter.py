import sys
# encoding=utf8

def to_decimal(GPS_input):
	
	"""from minutes to decimal"""	

	#GPS_input.decode('UTF-8').replace("72".decode('UTF-8'), "o").encode('UTF-8')
	
	#print GPS_input.encode('UTF-8')
	
	GPS_split = GPS_input.split('o')

	

	minutes = float(GPS_split[1].strip('’').decode('UTF-8'))
	decimal = minutes/60
	invert = False
	integer = 0
	for string in GPS_split[0].split():
		try:
			if string.isdigit():
				integer = int(string)
		except:	
			None	
		if  string == 'S' or string == 'E':
			invert = True		
	if invert:
		GPS_decimal = -(integer + decimal)
		
	else:
		GPS_decimal = integer + decimal
	
	return GPS_decimal
if __name__ == "__main__":
	print to_decimal(sys.argv[1])
