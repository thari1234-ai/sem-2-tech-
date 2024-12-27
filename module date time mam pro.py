import datetime
current_datetime=datetime.datetime.now().time()
print(current_datetime)

specific_date=datetime.date(2024,9,23)# to modify the date first month second
print("specific date:",specific_date)
specific_time=datetime.time(14,30,45)
print("specific_time",specific_time)
specific_datetime=datetime.datetime(2024,9,23,14,30,45)
print("specific_datetime :" , specific_datetime)

cu=datetime.datetime.now()
formatted_date=cu.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)

