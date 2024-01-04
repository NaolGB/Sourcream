import random
from datetime import timedelta, time
import numpy as np

def generate_random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)

    random_date = start_date + timedelta(days=random_days)
    return str(random_date.date())

def generate_random_time():
    return str(time(hour=random.randint(0, 11), minute=(random.randint(0, 59)), second=random.randint(0, 59)))

def generate_random_datetime(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_seconds = random.randint(0, 86400)  # 86400 seconds in a day

    random_datetime = start_date + timedelta(days=random_days, seconds=random_seconds)
    return str(random_datetime)

def divide_num_in_normal(num: float, num_parts: int):
    mean = num/2
    std_dev = num/15

    random_numbers = np.random.normal(mean, std_dev, num_parts)
    random_numbers /= sum(random_numbers)

    result = [int(number * num) for number in random_numbers]
    result[-1] += num - sum(result)

    return result
    
# UPTO_YEAR = lambda: timedelta(days=random.randint(1, 365))
# UPTO_MONTH = lambda: timedelta(days=random.randint(1, 30))
# UPTO_WEEK = lambda: timedelta(days=random.randint(1, 7))
# UPTO_DAY = lambda: timedelta(days=0, hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
# UPTO_HOUR = lambda: timedelta(days=0, hours=0, minutes=random.randint(0, 59), seconds=random.randint(0, 59))