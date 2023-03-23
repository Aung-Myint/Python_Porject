import math
def travel_with_car(km,fuel_in_tank,tank_max_cap,fuel_per_hundred_km):
    total_fuel=int((km*fuel_per_hundred_km)/100)
    fuel_to_fill_in_tank=total_fuel-fuel_in_tank if total_fuel>fuel_in_tank else 0
    total_ref_time=int(math.ceil(fuel_to_fill_in_tank/tank_max_cap))
    print(total_fuel,fuel_to_fill_in_tank,total_ref_time)
    print(f'Total fuel that you need for your car is {total_fuel} liters')
    print(f'Total fuel to fill in yout car is {fuel_to_fill_in_tank} liters')
    print(f'You need to fill {total_ref_time} times in your travel')

travel_with_car(200,50,80,8.9)