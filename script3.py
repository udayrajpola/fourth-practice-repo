print("Welcome to the bidders game")

def highest_bidder(bider1):
    value=0
    winner=""
    for key in bider1:
        if bider1[key]>value:
            value=bider1[key]
            winner=key
    print(f"The bidder winner is {winner} with bid amount  {value}")

i=True
Biders={}
while i:
    name=input("What is your name? \n")
    amount=int(input("What is your bid amount?\n"))
    Biders[name] = amount
    more_biders=input("Are there any more bidders?\n")
    if more_biders=="no":
        i=False
        highest_bidder(Biders)
    else:
        print("\n"*100)





