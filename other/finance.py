import pandas as pd
import yfinance as fin
import matplotlib.pyplot as plt
import pygame

print("hELLO ")

nstocks = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'UBER', 'NFLX' ,'NVDA']  # List of known stocks

def main():
    data(stock_tickers)

def data(stock_tickers):
    date = '2023-01-01'
    end_date = pd.Timestamp.today().strftime('%Y-%m-%d')
    df = pd.DataFrame()
    for ticker in stock_tickers:
        data = fin.download(ticker, start=date, end=end_date)
        data = data[['Adj Close']]
        data.columns = [ticker]
        high = fin.download(ticker, high)
        df = pd.concat([df, data, high], axis=1)

    df.index = pd.to_datetime(df.index)

    fig, ax = plt.subplots(figsize=(15, 8))
    for column in df.columns:
        ax.plot(df.index, df[column], label=column)
        ax.set_title('Stock Performance')
        ax.set_xlabel('Date')
        ax.set_ylabel('Adj Close Price')
        ax.legend()
        ax.grid(True)
        plt.xticks(rotation=35)
        plt.tight_layout()

    plt.show()

    output_file = 'stock.xlsx'
    df.to_excel(output_file)
    print(f"Stock performance data saved to {output_file}.")





# Display the list of known stocks
print("Known Stocks:", nstocks)

# Take user input for stock tickers
stock_input = input("Enter Stock Tickers (, to separate): ")
stock_tickers = stock_input.upper().split(',')

# import the pygame module

# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((300, 300))

# Set the caption of the screen
pygame.display.set_caption('saved')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:

# for loop through the event queue
	for event in pygame.event.get():

		# Check for QUIT event
		if event.type == pygame.QUIT:
			running = False


main()
