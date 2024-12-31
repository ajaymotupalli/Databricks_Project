%python
from datetime import date, timedelta, datetime

today = date.today()
today = today.replace(year = 2023)
print(f'today : {today}')

dbutils.widgets.dropdown("time_period","weekly",['daily','weekly','monthly'])
time_period = dbutils.widgets.get('time_period')


if time_period == "weekly" :
    start_date = today-timedelta(days=today.weekday(),weeks=1)-timedelta(days=110)
    end_date = start_date+timedelta(days=6)
    print(f'time period weekly start date  : {start_date}')
    print(f'time period weekly end date : {end_date}')

elif time_period == "monthly" :
    first_date = today.replace(day = 30).replace(month=10)
    print(first_date)
    end_date = first_date-timedelta(days=1)
    start_date = first_date - timedelta(days=end_date.day)
    print(f'time period monthly start date  : {start_date}')
    print(f'time period monthly end date : {end_date}')

else :
    start_date = today-timedelta(days=110)
    end_date = start_date
    print(f'time period daily start date  : {start_date}')
    print(f'time period daily end date : {end_date}')

display(spark.sql(f"""Select city,sum(Sale) Sale from sales where date between '{start_date}' and '{end_date}' group by all """))