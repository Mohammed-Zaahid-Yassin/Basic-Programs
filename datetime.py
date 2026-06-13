from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time for display
date_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("Current date and time:", date_time_string)
