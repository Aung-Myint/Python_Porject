from datetime import date
def ageCal(birthday_year,birth_month,birth_day):
    try:
       date(birthday_year,birth_month,birth_day)
    except TypeError:
        return 'Int Error'
    except ValueError:
        return 'Invalid Date'

    dob= date(birthday_year,birth_month,birth_day)
    print(dob)
    current_date=date.today()
    days_in_year=365.2425
    age=(int((current_date-dob).days/days_in_year))
    return f'{age} years old'

ans=ageCal(2001,2,30)
print(ans)