num1=int(input("\tEnter the Number of items "))
if num1<0 and num1<10:
 print("\t__________________")
 total_amount=120*num1
 print("\tTotal Amount",total_amount)
elif num1>10 and num1<99:
 total_amount=100*num1
 print("\t__________________")
 print("\tTotal Amount",total_amount)
elif num1>100:
    total_amount=70*num1
    print("\tTotal Amount",total_amount)
    print("\t__________________")
else:
    print("\t__________________")
    print("Enter a valid value")
