while True :
    
    luxury_charge = 0.50
    last_name = input("\n enter your name ")
    pizza_size = input("\n enter size of pizza: s,m,l,x : ")
    num_pizza = input("\n enter num of pizza ")


    try:
    
        if pizza_size in "smlx" and (int(num_pizza))>0:
        
            if pizza_size == "s" and num_pizza == 1:
                total_cost = luxury_charge + (1*10)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "s" and 2 <= (int(num_pizza)) <= 5:
                total_cost = luxury_charge + (int(num_pizza)*8.5)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "s" and 6 <= (int(num_pizza)) <= 9:
                total_cost = luxury_charge + (int(num_pizza)*6.25)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            
            elif pizza_size == "s" and  (int(num_pizza)) >= 10:
                total_cost = luxury_charge + (int(num_pizza)*5)
                HST = 0.13 * total_cost
                amount_paid =  total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "m" and  (int(num_pizza)) == 1:
                total_cost = luxury_charge + (int(num_pizza)*16.0)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "m" and 2 <= (int(num_pizza)) <= 5:
                total_cost = luxury_charge + (int(num_pizza)*12)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "m" and 6 <= (int(num_pizza)) <= 9:
                total_cost = luxury_charge + (int(num_pizza)*9)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "m" and (int(num_pizza)) >= 10:
                total_cost = luxury_charge + (int(num_pizza)*8)
                HST = 0.13 * total_cost
                amount_paid =  total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "l" and  (int(num_pizza)) ==1:
                total_cost = luxury_charge + (int(num_pizza)*20)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "l" and 2 <= (int(num_pizza)) <= 5:
                total_cost = luxury_charge + (int(num_pizza)*15)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "l" and 6 <= (int(num_pizza)) <= 9:
                total_cost = luxury_charge + (int(num_pizza)*12)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "l" and  (int(num_pizza)) >=10:
                total_cost = luxury_charge + (int(num_pizza)*10)
                HST = 0.13 * total_cost
                amount_paid = total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "x" and  (int(num_pizza)) == 1:
                total_cost = luxury_charge + (int(num_pizza)*23)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "x" and 2 <= (int(num_pizza)) <= 5:
                total_cost = luxury_charge + (int(num_pizza)*21)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            elif pizza_size == "x" and 6 <= (int(num_pizza)) <= 9:
                total_cost = luxury_charge + (int(num_pizza)*18)
                HST = 0.13 * total_cost
                amount_paid = HST + total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            else :               
                total_cost = luxury_charge + (int(num_pizza)*16)
                HST = 0.13 * total_cost
                amount_paid = total_cost
                print("\n" + last_name + " you bought " + num_pizza + " pizzas at a cost of $" + str(amount_paid) + ".")
            
            
        else:
            print("\nincorect input please enter either s,x,m, or l  for size of pizza")

        
        
    except ValueError:
        print("\n incorrect input at least one pizza needs to be ordered")
    

    
        
    
        
        