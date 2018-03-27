"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


sales = 1.0
while sales > 0.0:
    sales = float(input("Enter sales: $"))
    if sales <= 0.0:
        print("Invalid - input")
        break;
    elif sales > 1000 :
        bonus = (sales*0.15)
        print("The bonus is $", '{:.2f}'.format(bonus))
    else:
        bonus = (sales*0.10)
        print("The bonus is $", '{:.2f}'.format(bonus))

