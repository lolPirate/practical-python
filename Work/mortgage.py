# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months += 1
    interest = principal * (1+rate/12)
    if interest < payment:
        payment = interest
    principal = interest - payment
    total_paid = total_paid + payment
    if extra_payment_start_month <= months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    print(f'{months}\t{round(total_paid, 2)}\t{round(principal, 2)}')

print(f'{round(total_paid, 2)} over {months} months')
