# Given data
Expense = {'January': 2200, 'February': 2350,
           'March': 2600, 'April': 2130, 'May': 2190}

# Function returns the amount spend


def amt_spend(in_month):
    return Expense[in_month]
# function for total quarter amount


def quarter():
    # General code
    value = 0
    quarter_sum = []
    for month in Expense:
        quarter_sum.append(Expense[month])
        value += 1
        if value == 3:
            break
    return sum(quarter_sum)

#returns key name
def twenty_hun ():
    for keys,values in Expense.items():
        if values == 2000:
           result = True
        else:
            result = False

    return result








spend = amt_spend('February')
print(spend)
ttl_Amount = quarter()
print(ttl_Amount)
yes = twenty_hun()
print(yes)
Expense.update({'June':1980})
Expense.update({'April':2330})
print(Expense)