def calculate_change(total_bill, amount_paid):
  return amount_paid - total_bill


total_bill = 2.50
amount_paid = 4.00
change = calculate_change(total_bill, amount_paid)


print(f"The shopkeeper should return ${change} to Vishal.")