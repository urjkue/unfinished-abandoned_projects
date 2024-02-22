import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import json

fileObject = open("data.json", "r")
jsonContent = fileObject.read()
nstocks = json.loads(jsonContent)

stock_list =nstocks
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

def save_plt():
        stock_list =nstocks
        data = yf.download(stock_list, start="2015-01-01", end="2020-02-21")
        print('data fields downloaded:', set(data.columns.get_level_values(0)))

        # Plot data graphically
        data['Close'].plot(figsize=(10, 6))
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.title('Stock Price')
        plt.legend(stock_list)
        plt.grid(True)
        plt.show()

        data.to_excel("stock_data.xlsx" , index =True)
        data.head()

save_plt()
