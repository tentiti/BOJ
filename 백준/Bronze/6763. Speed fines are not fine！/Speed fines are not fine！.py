l=int(input())
s=int(input())
if s<=l:
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is ${}.".format(100 if s-l <=20 else 270 if s-l <=30 else 500))