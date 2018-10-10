'''
Write a function called get_change, which accepts one argument amount (an integer). The function should return the coins needed to dispense that amount.
The coin denominations are Euro
(1, 2, 5, 10, 20, 50, 100, 200)
The function should return the fewest coins possible to make the amount.
E.g. 76c = 50, 20, 5, 1
     44c = 20, 20, 2, 2
'''



def get_change(amount):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    change = []
    for num in coins:
        while amount >= num:
            change.append(num)
            amount -= num
    return change
            
            
            
            
            
                

amount = int(input("Enter amount: "))

change = get_change(amount) 

print(change)
        
    