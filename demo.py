credit=input("is your credit is good(if good credit then write yes if not write no)")
if credit=='yes':
    good_credit=True
else:
    good_credit=False

if good_credit:
    print("Buyer have to give 10% less")
    print("Down payment is 900000")
else:
    print("buyer have to give 20% less")
    print("Down payment is 800000")
print("thanks for buying")