import pytz


def round_number():
    round(1.23, 1)  # 1.2
    round(1.5, 0)  # 2
    round(101.5, -1)  # 100.0
    # format
    format(1.236, "0.2f")  # 1.24
    "value is {:0.2f}".format(1.236)  # value is 1.24
    # decimal module can make result precise


def learn_random():
    import random

    values = [1, 2, 3, 4, 5, 6]
    random.choice(values)
    random.sample(values, 3)
    random.shuffle(values)
    random.randint(0, 9)
    random.random()


def convert_date():
    from datetime import timedelta, datetime


def caculate_date():
    from datetime import datetime, timedelta

    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    def get_previous_byday(dayname, start_date=None):
        if start_date == None:
            start_date = datetime.now()
        day_num = start_date.weekday()
        day_num_target = weekdays.index(dayname)
        days_ago = (7 + day_num - day_num_target) % 7
        if days_ago == 0:
            days_ago = 7
        target_date = start_date - timedelta(days=days_ago)
        return target_date

    get_previous_byday("Sunday", datetime(2021, 10, 29))


def convert_date():
    """convert string to datetime"""
    from datetime import datetime

    text = "2021-10-29"
    date = datetime.strptime(text, "%Y-%m-%d")
    # desired format
    a = datetime.strftime(datetime.now(), "%A %B %b, %Y")
    ## for large dataset
    from datetime import datetime

    def parse_ymd(s):
        year_s, mon_s, day_s = s.split("-")
        return datetime(int(year_s), int(mon_s), int(day_s))


def convert_timezone():
    from datetime import datetime
    from pytz import timezone

    d = datetime(2012, 12, 21, 9, 30, 0)  # 2012-12-21 09:30:00
    # Localize the date for Chicago
    central = timezone("US/Central")
    local_d = central.localize(d)  # 2013-03-10 01:45:00-06:00
    utc_d = local_d.astimezone(timezone(pytz.utc))  # 2013-03-10 07:45:00+00:00
