import random

def people(group):
    tax = 0
    gdp = 0
    salary = range(15000,560000)

    # group = {
    #     "EMPLOYED" : 5,
    #     "UNEMPLOYED": 10,
    #     "RETIRED": 4
    # }
    for i in group :
        if(i == "EMPLOYED"):
            print("employed : "+ str(group[i]))
            for i in range(group[i]):
                gdp = gdp + random.randint(15000,560000)
        elif(i == "UNEMPLOYED"):
            print("unemployed : "+ str(group[i]))
        else:
            print("retired : " + str(group[i]))
    print(gdp)



def government(group):
     print("Govtment")
     employed =group["EMPLOYED"]
def country():
        group = {
        "EMPLOYED" : 5,
        "UNEMPLOYED": 10,
        "RETIRED": 4
    }
        people(group)

country()
