import random




def buy(compani):
    total = []
    print("hello")
    names = ["Robert","Barry","nickker"]
    for x in compani:
         a = ((compani[x])[0])
         b= ((compani[x])[1])
         tot = a *b
         total.append(tot)
         buyer = random.choice(names)
         num = random.randint(1,1000)
         order = num * b
         while True:
             if(num <= tot ):
                #  print(order)
                 print(buyer + " bought " + str(num) + " of " + x)
                 a =  a - num
                 break
             else:
                 num - random.randint(1,100)
                 order = num * b
                 a = a - num
                #  print(order)
                 print(buyer + " bought " + num + " of " + i)




def sell(compani):
    print("")
    totals = []
    print("hello")
    names_s = ["Robert","Barry","nickker"]
    for x in compani:
         a = ((compani[x])[0])
         b= ((compani[x])[1])
         tot = a *b
         totals.append(tot)
         seller = random.choice(names_s)
         num = random.randint(1,1000)
         order = num * b
        #  print(order)
        #  print(a)
         a = order + num

         print(seller + " sold " + str(num) + " of " + x)
        #  print(a)
        #  print(num)
        #  input()

        #  while True: print(a)
        #      if(order <= tot ):
        #          print(order)
        #          break
        #      else:
        #          num - random.randint(1,100)
        #          order = num * b
                #  print(order)

    # print(buyer)

    # if  stock is available , buy stock .
    # so , need to save stock , buy stock


    # market_cap = 0
    # # print("this is buy !")
    # chosen = companies[b_stock]
    # market_cap = chosen[0] * chosen[1]
    # print("Market cap : " + market_cap)

    # print(chosen)
    # for x in chosen:



def main(companies):
    # print(companies)
    timer = 1
    Day = "Monday"
    print("Day: "+Day)
    print("..../......././..........//.......")
    input("Satrt sim")


    while (timer <=5 ):
        buy(companies)
        sell(companies)
        print(timer)
        input()
        timer = timer + 1
    # print("Available stocks :")
    # for i in companies:
    #     print(i)

    # b_stock = input("What stock to buy? : ")
    # buy(b_stock)
    # chosen = companies[b_stock]
    # for x in chosen:



    # companies = ["q","w","f"]
    # for i in companies:
    #     print(i)
    # print("This is the main")



#buy


#sel

#stock
companies = {

   "Appl":  [1000,2],
   "Amazone": [1000,3],
   "Songo": [2000,35]
    # "Amazone" : 50

}
main(companies)
# buy(companies)
# sell(companies)
