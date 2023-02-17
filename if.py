x=1
marks=59
grades=109
amount=500
if (x>0):
    print("The number is positive")
    print(4+10)
    #if...else statement
if marks>=60:
    print("You have passed")
else:
      print("You have failed")

  #if..elif...else
if grades<=29 and grades>=0:
    print("you have failed")
elif grades <=49 and grades>=30:
    print("You have passed")
elif grades<=79 and grades >=50:
    print("you have credid")
elif grades<=100 and grades>=80:
    print("you have distinction")
else:
    print("wrong input")

if amount<=100 and amount>=0:
    print("you cannot make this trsnsaction")
elif amount<=200 and amount>=101:
    print("Free transaction")
elif amount<=500 and amount>=300:
    print("you'll be charged")