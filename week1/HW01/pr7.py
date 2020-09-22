purchase = int(input("Enter the purchase: "))
stateTax = purchase*0.5
salesTax = purchase*2.5
print("The amount of the purchase = "+str(purchase))
print("The state sales tax = " + str(stateTax))
print("The county sales tax = "+str(salesTax))
print("The total sales tax = "+str(salesTax+stateTax))
print("The total of the sale = "+str(salesTax+stateTax+purchase))