print('Welcome to the tip calculator.')
amount = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
ppl = int(input("How many people split the bill?"))
res = round((amount/ppl)*(1+tip/100), 2)
print(f"Each person should pay: ${res}")
