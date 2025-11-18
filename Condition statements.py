total=float(input("Enter your total purchase amount"))
print(f"Your purchase amount is {total:.2f}")
big_discount=total-(15/100*total)
small_discount=total-(10/100*total)
if total>=100:
    print(f"You have recieced a 15% discount.Your new total is {big_discount:.2f}")
elif total >= 50 :
    print(f"you have recieved a 10% discount.Your new total is{small_discount:.2f}")
elif total<50:
    print (f"No discount applied.Your total is {total:.2f}")