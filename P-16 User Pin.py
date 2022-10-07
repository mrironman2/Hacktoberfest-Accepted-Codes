#program for storing pin for atm etc
user_pin=7171
ask_pin=int(input("\t\tEnter Your Pin"))
if ask_pin==user_pin:
    print("\t\tAccess Granted")
    withdraw_amt=int(input("\t\tEnter your amount"))
    cash2000_note=withdraw_amt//2000
    print("\t\tYou will get",cash2000_note,"notes of 2000")
    cash500_note=(withdraw_amt%2000)//500
    print("\t\tYou will get",cash500_note,"notes of 500")
    cash200_note=(withdraw_amt%500)//200
    print("\t\tYou will get",cash200_note,"notes of 200")
    cash100_note=(withdraw_amt%200)//100
    print("\t\tYou will get",cash100_note,"notes of 100")
    cash50_note=(withdraw_amt%100)//50
    print("\t\tYou will get",cash50_note,"notes of 50")
else:
    print("\t\tAccess Denied")
    print("\t\tYou have 2 Attempts Left")
