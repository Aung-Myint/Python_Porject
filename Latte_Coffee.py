def latte(milk,expresso_beans):
    milk_in_ml_per_cup=round(8/0.033814,2)
    expresso_beans_per_cup=16.5
    cup_size_in_ml=round(11/0.033814,2)
    print(milk_in_ml_per_cup,expresso_beans_per_cup,cup_size_in_ml)
    milk_in_cups=int(milk/milk_in_ml_per_cup)
    expresso_beans_in_cup=int(expresso_beans/expresso_beans_per_cup)
    print(milk_in_cups,expresso_beans_in_cup)

    if (milk_in_cups>expresso_beans_in_cup):
        print(f'Total : {expresso_beans_in_cup} latte cups.')
    elif (expresso_beans_in_cup>milk_in_cups):
        print(f'Total : {milk_in_cups} latte cups.')
    else:
        if milk_in_cups == expresso_beans_in_cup:
            print(f'Total : {milk_in_cups} latte cups.')

latte(3000,500)