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

print(f"""
-----------------------------------------
Each person should pay: ${pay_per_person}
-----------------------------------------""")
