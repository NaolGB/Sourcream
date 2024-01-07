import random
from datetime import timedelta, time, datetime
import numpy as np

def generate_random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)

    random_date = start_date + timedelta(days=random_days)
    return random_date.date()

def generate_random_time():
    return time(hour=random.randint(0, 11), minute=(random.randint(0, 59)), second=random.randint(0, 59))

def add_random_days(min_days: int, max_days: int, current_date: datetime):
    latest_date = current_date + timedelta(days=random.randint(min_days, max_days))
    return latest_date

def add_random_hours(max_hours: int, current_time: time) -> time:
    current_datetime = datetime.combine(datetime.today(), current_time)
    random_hours = random.randint(0, max_hours)
    random_timedelta = timedelta(hours=random_hours, seconds=5)
    latest_datetime = current_datetime + random_timedelta
    
    latest_time = latest_datetime.time()
    
    return latest_time

def process_strings(strings):
    """given lines of strings, cleans up and returns a set of non-whitespaced string"""
    stripped_strings = [s.strip() for s in strings]
    
    # Use a list to maintain the order and remove duplicates
    unique_strings = []
    
    for s in stripped_strings:
        if s not in unique_strings:
            unique_strings.append(s)
    
    # Sort the list of unique strings
    sorted_unique_strings = sorted(unique_strings)
    sorted_strings_with_new_line = ""
    for i in sorted_unique_strings:
        sorted_strings_with_new_line += f"{i}\n" 
    
    return sorted_strings_with_new_line
    
UPTO_YEAR = lambda: timedelta(days=random.randint(1, 365))
UPTO_MONTH = lambda: timedelta(days=random.randint(1, 30))
UPTO_WEEK = lambda: timedelta(days=random.randint(1, 7))
UPTO_DAY = lambda: timedelta(days=0, hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
UPTO_HOUR = lambda: timedelta(days=0, hours=0, minutes=random.randint(0, 59), seconds=random.randint(0, 59))