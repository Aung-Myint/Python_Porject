def cafe(hour=0,min=0):
    per_hour=1000
    per_half_hour=500
    hour_cost=0
    min_cost=0
    if hour>=1 :
        hour_cost=(hour*per_hour)
        print(hour_cost)
    else:
        print(f'{hour} is invalid hour')
    
    if min>=1 and min<=30:
            per_half_percentage=(min/30)*100
            min_cost +=(per_half_percentage/100)*per_half_hour
            print(min_cost)

    elif min>30 and min<60:
            per_half_over_percentage=(min/60)*100
            min_cost +=(per_half_over_percentage/100)*per_hour
            print(min_cost)

    else:
        return (f'{min} is invalid minutes')
    total_cost=hour_cost+min_cost
    return f'Your total cost is {round (total_cost,2)} kyats!'

tc=cafe(3,35)
print(tc)
