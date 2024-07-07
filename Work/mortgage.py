# mortgage.py
#
# Exercise 1.7

principal = 500_000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = (5 * 12) # inclusive
extra_payment_end_month = extra_payment_start_month + (4 * 12) # exclusive
extra_payment = 1000

def compute_payment(month):
    if extra_payment_start_month <= month < extra_payment_end_month:
        return base_payment + extra_payment
    return base_payment

def report(*args, ndigits = 6):
    out = [round(a, ndigits) for a in args]
    print(*out)

while principal > 0:
    month = month + 1
    payment = min(compute_payment(month), principal)
    if payment >= principal:
        payment = principal
        principal = 0
    else:
        principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    print(f"{month} {total_paid:.2f} {principal:.2f}")

print(f"Total paid {total_paid:.2f}")
print("Months", month)
