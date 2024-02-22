##The imports

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import json

## the stock list 
nstocks = ["AAPL", "GOOGL", "MSFT", "TSLA", "UBER", "NFLX", "NVDA", "META", "AMD"]
json_object = json.dumps(nstocks, indent="")

# creating and looking for the json file
with open("data.json", "w") as outfile:
    outfile.write(json_object)

fileObject = open("data.json", "r")
jsonContent = fileObject.read()
nstocks = json.loads(jsonContent)
stock_list =nstocks

expath = ""
filename = input("Enter the name of the file: ")
expath = input("Enter the excel file folder [will creat if non exsistant] ")
whole_path = (expath+"\\"+filename)
print(whole_path)
input()
while True:

    print('stock_list:', nstocks)
    ans = input("proceed or add or remove a stock from the list? (done to finish): ")
    if ans == "add":

            ans =  input("ENTER THE STOCK NAME : ")
            fileObject = open("data.json", "r")
            jsonContent = fileObject.read()
            nstocks = json.loads(jsonContent)
            tempstocklist = nstocks.append(ans)
            jsonString = json.dumps(nstocks)
            jsonFile = open("data.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            print(nstocks)
            input()
    if ans == "remove":
                    ans =  input("ENTER THE STOCK NAME : ")
                    fileObject = open("data.json", "r")
                    jsonContent = fileObject.read()
                    nstocks = json.loads(jsonContent)
                    tempstocklist = nstocks.remove(ans)
                    tempstocklist = nstocks
                    jsonString = json.dumps(nstocks)
                    jsonFile = open("data.json", "w")
                    jsonFile.write(jsonString)
                    print(nstocks)
                    input()
    else:
            if ans == "done":
                break
 ## saving the data in xslsx file
def save_plt():
        sdate = input ("Input the start date eg: 2023-01-01:y,m,d : ")
        edate = input("Input the end of gthe time frame : ")
        stock_list =nstocks
        data = yf.download(stock_list, start=sdate, end=edate)
        print('data fields downloaded:', set(data.columns.get_level_values(0)))

        # Plot data graphically
        data['Close'].plot(figsize=(10, 6))
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.title('Stock Price')
        plt.legend(stock_list)
        plt.grid(True)
        plt.show()

        data.to_excel(whole_path , index =True)
        data.head()

save_plt()
