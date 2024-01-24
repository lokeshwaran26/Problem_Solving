def bonAppetit(bill, k, b):
    # Write your code here
    pay = 0
    for i in range(len(bill)):
        if i != k:
            pay += bill[i]
    act = pay/2
    if act == b:
        print("Bon Appetit")
    else:
        n = b - act
        print(int(n))
