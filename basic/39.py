def interest_rate(amt,interest,years):
	amount = amt*(1+interest)**years
	return amount

print(interest_rate(1000,.1,1))
print(interest_rate(1000,.1,2))

