from datetime import date, timedelta, datetime


users = [{'name': 'Kim', 'birthday': date(2023, 1, 21)}, {'name': 'Bim', 'birthday': date(2023, 1, 22)},
         {'name': 'Dim', 'birthday': date(2023, 1, 23)},{'name': 'Tim', 'birthday': date(2023, 1, 27)},
         {'name': 'Dim', 'birthday': date(2023, 1, 27)},{'name': 'Tim', 'birthday': date(2023, 1, 28)},
         {'name': 'Rim', 'birthday': date(2023, 1, 29)}, {'name': 'Vim', 'birthday': date(2023, 2, 4)}]


def get_birthdays_per_week(users):
    day_now = datetime.now()
    delta_end_week = 6-day_now.weekday()
    start_of_period = day_now + timedelta(days = delta_end_week)
    end_of_period = day_now + timedelta(days = (delta_end_week + 6))
    print (start_of_period.date(), end_of_period.date())

    persons_for_weekday = {}

    for char in users:
        if char['birthday'].weekday()==6 and start_of_period.date() <= char['birthday'] <= end_of_period.date():
            day_remember = char['birthday'] + timedelta(days=1)
            if day_remember.strftime("%A") not in persons_for_weekday:
                persons_for_weekday[day_remember.strftime("%A")] = []
            persons_for_weekday[day_remember.strftime("%A")].append(char['name'])
        if char['birthday'].weekday()!=6 and start_of_period.date() <= char['birthday'] <= end_of_period.date():
            day_remember = char['birthday']
            if day_remember.strftime("%A") not in persons_for_weekday:
                persons_for_weekday[day_remember.strftime("%A")] = []
            persons_for_weekday[day_remember.strftime("%A")].append(char['name'])


    for day, list_pers in persons_for_weekday.items():
        pers = ', '.join(list_pers)
        print(f'{day}: {pers}')


get_birthdays_per_week(users)
