# 1) Get Current DateTime in Python
	
			from datetime import datetime

			now = datetime.now()
			print('Current DateTime:', now)
			print('Type:', type(now))


	# 2) Extract Current Date and Time Separately from a Datetime Object

			# import only datetime class
			from datetime import datetime

			# current datetime
			now = datetime.now()

			current_date = now.date()
			print('Date:', current_date)
			print(type(current_date))

			current_time = now.time()
			print('Time', current_time)
			print(type(current_time))




	# 3) Get Current Year, Month, Day, Hour, Minute, Seconds

			from datetime import datetime

			# Get current date and time
			now = datetime.now()

			# extract attributes 
			print("Year:", now.year)
			print("Month:", now.month)
			print("Day =", now.day)

			print("Hour:", now.hour)
			print("Minute:", now.minute)
			print("Second:", now.second)
			print("Microsecond:", now.microsecond)