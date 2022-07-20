monthly_expenses = [2200, 2350, 2600, 2130, 2190]
feb_diff = monthly_expenses[1]-monthly_expenses[0]
firstquarter_expenses = monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[2]
print(2000 in monthly_expenses)
june_expense = monthly_expenses.append(1800)
monthly_expenses[3]=monthly_expenses[3]-200
print(monthly_expenses)

heros=['spider man','thor','hulk','iron man','captain america']
for hero in heros:
    print(hero, len(hero))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3, 'black panther')
heros[1:3]='doctor strange'
print(heros)
print(dir(list))
heros.sort()
print(heros)


user_input = input("enter your number>")
start_no = 1;
odd_no = []
for no in range(int(user_input)):
    if start_no <= int(user_input):
        odd_no.append(start_no)
        start_no += 2
print(odd_no)

