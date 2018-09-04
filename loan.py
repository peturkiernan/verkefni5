loan = int(input('Input the cost of the item in $: '))
loan = float(loan)
if loan <= 1000:
    r = 0.015
else:
    r = 0.02
counter = 0
payment = 50
total_interest = 0
while loan > 0:
    if loan > 50:
        payment = 50.0
        interest = loan * r
        remaining_debt = loan - payment + interest
        loan = remaining_debt
        counter += 1
        total_interest += interest
        print('Month:',counter,'Payment:',payment,'Interest paid:',round(interest,2),'Remaining debt:',round(remaining_debt,2))
    else:
        interest = loan * r
        payment = interest + loan
        remaining_debt -= payment - interest
        counter += 1
        total_interest += interest
        loan = remaining_debt
        print('Month:',counter,'Payment:',round(payment,2),'Interest paid:',round(interest,2),'Remaining debt:',round(remaining_debt,2))

print('Number of months:',counter)
print('Total interest paid:',round(total_interest,2))