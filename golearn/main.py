from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)

future_month = (current_datetime.month % 12) + 1
print(future_month)
future_year = current_datetime.year + int(current_datetime.month / 12)
print(future_year)
future_datetime = datetime(future_year, future_month, 1)
print(future_datetime)

print(current_datetime < future_datetime)    # True