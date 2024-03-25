import sys

type = sys.argv[1]

if type == "t2.micro":
    print("yes we can create")
elif type == "t2.medium":
    print("price is 3 dollars")
else:
    print("we cant")
