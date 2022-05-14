interest_rate = 5.0
years = 3
initial_amount = 1000

final_amount = initial_amount * (1 + interest_rate / 100) ** years

print '{} euros after {} years at the rate of {} is {} euros'.format(initial_amount, years, interest_rate, final_amount)