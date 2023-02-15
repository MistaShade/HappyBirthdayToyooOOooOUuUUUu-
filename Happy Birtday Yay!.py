from datetime import*

today = date.today()

dob_str = input("(dd/mm/yyyy"))

dob_data = dob_str.split("/")
dobDay = int(dob_data[0])
dobMonth = int(dob_data[1])
dobYear = int(dob_data[2])
dob = date(dobYear, dobMonth, dobDay)

thisYear = today.year
nextBirthday = date(thisYear, dobMonth, dobDay)

if today ==nextBirthday:
   print("Happy Birthday yey!")
ele:
   print("Today is not your birthday...")
