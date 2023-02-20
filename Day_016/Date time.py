from datetime import datetime

# Get the current date and time
now = datetime.now()
print(now)

# Extract the day, month, year, hour, and minute
day = now.date
a = day
print(a)
month = now.month
print(month)
year = now.year
print(year)
hour = now.hour
print(hour)
minute = now.minute
print(minute)

# Get the timestamp
timestamp = datetime.timestamp(now)
# Format the current date
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

# Calculate the time difference between now and new year
new_year = datetime(year=now.year+1, month=1, day=1)
time_diff = new_year - now
print(time_diff)

# Calculate the time difference between 1 January 1970 and now
epoch = datetime(1970, 1, 1)
time_diff = now.timestamp() - epoch.timestamp()
print(time_diff)

