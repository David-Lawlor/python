
def calculateTipDue(total, tipPercentage):
    totalAmountDue = total * ((100 + tipPercentage)/100.0)
    return totalAmountDue

billTotal = int(input("Enter the total bill amount   "))

tipAmount = int(input("Enter the tip percentage    "))

print ("Bill total is " , billTotal)
print ("Tip amount is ", tipAmount)
print ("Total including tip ", calculateTipDue(billTotal, tipAmount))

