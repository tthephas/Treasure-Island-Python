# treasure islan project
# logic, if else statements


print('Welcome to python pizza deliveries')
size = input('what size pizza do you want? S, M or L?')
add_pepperoni = input('Do you want pepperoni? Y or N')
extra_cheese = input('Do you want extra cheese? Y or N')

# small pizza: 15
# medium pizza: 20
# large pizza: 25
# pepperoni on small: 2
# pepperoni on m or l: 3
# extra cheese: 1
# Calculate final bill
# 

final_bill = 0
if size == 'S':
    final_bill += 15
    if add_pepperoni == 'Y':
        final_bill += 2
        if extra_cheese == 'Y':
            final_bill += 1
print(f'Your total is ${final_bill}')