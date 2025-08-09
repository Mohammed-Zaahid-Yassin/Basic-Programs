from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current date and time:", now.strftime("%d-%m-%Y %H:%M:%S"))

# Add time — for example, 2 hours and 30 minutes
added_time = now + timedelta(hours=2, minutes=30)
print("After adding 2 hours 30 minutes:", added_time.strftime("%d-%m-%Y %H:%M:%S"))

# Example: Add 5 days
future_date = now + timedelta(days=5)
print("After adding 5 days:", future_date.strftime("%d-%m-%Y %H:%M:%S"))
