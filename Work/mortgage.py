# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
total_months_paid = 0

while principal > 0:
    total_months_paid += 1
    if extra_payment_start_month <= total_months_paid <= extra_payment_end_month:
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if principal < 0:
        print(f"{total_months_paid:0.2f} {total_paid:0.2f} {principal+payment:0.2f}")
    else:
        print(f"{total_months_paid:0.2f} {total_paid:0.2f} {principal:0.2f}")

print(f"Total paid {total_paid:0.2f}")
print(f"Months {total_months_paid:0.2f}")
