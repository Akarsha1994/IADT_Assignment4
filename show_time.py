from datetime import datetime
from datetime import date

now = datetime.now()
today = date.today()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Today's date:", today)
print("Day:", datetime.today().weekday())
