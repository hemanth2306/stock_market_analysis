import yfinance as yf
import pandas as pd
import descriptive_analysis

import sys
import os


def fetch_stock_data(ticker, start_date, end_date):
    # Fetch stock data using Yahoo Finance API
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data


def home_menu(stock_data, closing_price):
    print( "**********Welcome to Yahoo Finance Stock Market Analysis and Predictions**********" )
    
    home_menu = "\n1. Want to anaylsis the stock using a stock symbol?\n2. View user manual or readme file\n3. want to see a flow chart of a program\n4  exit."
    print(home_menu)
    print("-" * 100)
    choice = input("Please enter your preference: ")
    while choice != "4":
        try:
            if choice == "1":
                ticker = input("Enter the Ticker symbol: ")
                start_date = input("Enter the start date (YYYY-MM-DD): ")
                end_date = input("Enter the end date (YYYY-MM-DD): ")
                stock_data = fetch_stock_data(ticker, start_date, end_date)
                stock_data['Date'] = pd.to_datetime(stock_data.index)
                stock_data.set_index('Date', inplace=True)
                closing_price = stock_data['Close']
                descriptive_analysis.descriptive_menu(stock_data, closing_price)
            elif choice == "2":
                if sys.platform == "win64":
                    os.startfile('Readme.pdf')
                else:
                    os.system("Readme.pdf")
            elif choice == "3":
                if sys.platform == "win64":
                    os.startfile('flow_chart.png')
                else:
                    os.system("open flow_chart.png")
            elif choice =="4":
                sys.exit()
            else:
                print("\n" + "*" * 10 + " Input Error: Please enter a valid option. " + "*" * 10 + "\n")
        except ValueError:
            print("\n" + "*" * 10 + " Input Error: Please enter a valid option. " + "*" * 10 + "\n")
        except Exception as e:
            print("\n" + "*" * 10 + " Sorry, an error occurred. Please try again with valid input. " + "*" * 10 + "\n")
            print(e)
        print("+" * 100)
        print(home_menu)
        print("+" * 100)
        choice = input("Please enter your preference: ")


# Code for testing the function
if __name__ == '__main__':
    # Call the home_menu function
    home_menu(None, None)
