def bonAppetit(bill, k, b):
    anna = (sum(bill)-bill[k])//2
    if anna == b:
        print("Bon Appetit")
    else:
        print(bill[k]//2)