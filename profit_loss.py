actual_cost = float(input("Please enter Actual Product Price: "))
sale_amount = float(input("Please Enter Sales Amount: "))
if (sale_amount > actual_cost):
 Amount = sale_amount - actual_cost
 print("Total Profit = ", Amount)    
else:
 print("No Profit!!!")