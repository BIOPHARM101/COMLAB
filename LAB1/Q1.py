def run():
    Price = input()
    Ship = input()
    Price1 = float(Price)
    Ship1 = float(Ship)
    x = Price1+Ship1
    x1 = str(x)
    
    print('Price : '+ Price)
    print('Shipping : '+ Ship)
    print('Total : '+x1+(" Baht ("+Ship+" Baht shipping fee)"))
run()