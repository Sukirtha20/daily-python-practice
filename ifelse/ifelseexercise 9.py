maths=int(input("Maths:"))
science=int(input("Science:"))
socialscience=int(input("Social Science:"))
tamil=int(input("Tamil:"))
english=int(input("English:"))
average=(maths+science+socialscience+tamil+english)/5
if(average<35):
    print("additional class is required")
else:
    print("you are good")
