print("""
████████ ██ ██████       ██████  █████  ██       ██████ ██    ██ ██       █████  ████████  ██████  ██████  
   ██    ██ ██   ██     ██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
   ██    ██ ██████      ██      ███████ ██      ██      ██    ██ ██      ███████    ██    ██    ██ ██████  
   ██    ██ ██          ██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
   ██    ██ ██           ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██    ██     ██████  ██   ██                                                                                                   
""")

print("\nWelcome to The Tip Calculator!")

bill_amount = float(input("\nWhat was the total bill? : $"))

number_of_people = int(input("\nHow many people to split the bill? : "))

tip_percentage = float(input("\nWhat percentage tip would like to give? : "))

tip_amount = (bill_amount * tip_percentage) / 100

total_bill_amount = bill_amount + tip_amount

pay_per_person = round(total_bill_amount / number_of_people, 2)

# This feature will ensure consistent two-digit precision after the decimal point in the output, even when the
# 'pay_per_person' amount is, for instance, 12.3 or 9.3. The values will be presented as 12.30 and 9.30 respectively.
pay_per_person = "{:.2f}".format(pay_per_person)

print(f"""
-----------------------------------------
Each person should pay: ${pay_per_person}
-----------------------------------------""")
