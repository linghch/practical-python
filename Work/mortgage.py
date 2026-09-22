# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
month = 0 # Count the month
current_payment = 0.0 # Every month paid
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    # Get next month
    month = month + 1

    # Compute the principal of the user at the end of each month
    principal = principal * (1 + rate / 12)

    # Confirm the payment of each month
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        current_payment = payment + extra_payment
    else:
        current_payment = payment

    # If the principal is less than or equal to current_payment, don't pay more
    if principal <= current_payment:
        current_payment = principal

    # Compute remaining principal
    principal = principal - current_payment

    # Compute the total payment
    total_paid = total_paid + current_payment

    # Print payment breakdown row by row
    print(f'{month:<10d} {round(total_paid, ndigits=2):<10.2f} {round(principal, ndigits=2):<10.2f}')

print(f'Total_paid {round(total_paid, ndigits=2):<10.2f}')
print(f'Months     {month:<10d}')