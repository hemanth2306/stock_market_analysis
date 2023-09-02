
import numpy as np
from numpy import percentile
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import dates as mpl_dates
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from matplotlib import pylab
rcParams['figure.figsize'] = 15, 10
import scipy.stats as ss
from scipy.stats import kurtosis
from scipy.stats import skew
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from datetime import datetime, timedelta, date
import dateutil

import warnings
warnings.filterwarnings("ignore")

import seaborn as sns
sns.set_style('whitegrid')


                                                    #Descriptive Analytics Menu 
def descriptive_menu(stock_all_data,stock_closing_price):
    print ("-" * 100)
    descriptive_menu = "\n select a Choice of services mentioned in Descriptive Analysis:\n1. Statistical Information\n2. Graphical Visualisation\n3. Go back to the Main Menu\n"
    print(descriptive_menu)
    print ("-" * 100)
    descriptive_choice = input("Please enter your choice: ")
    while descriptive_choice != "3":
        try:
            if descriptive_choice == "1":
                descriptive_stats_menu(stock_all_data,stock_closing_price)
            elif descriptive_choice == "2":
                graph_menu(stock_all_data,stock_closing_price)
            else:
                print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
        except ValueError:
            print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
        except:
            print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
        print ("-" * 100)
        print(descriptive_menu)
        print ("-" * 100)
        descriptive_choice = input("Please enter your choice: ")

                                #Descriptive Analytics- Statistics Analysis 
def descriptive_stats_menu(stock_all_data,stock_closing_price):
    print ("-" * 100)
    descriptive_stats_menu = "\nSelect the key factor for statistical insights: \n1. Opening Price\n2. Closing Price\n3. Adjacent Closing Price\n4. High Price\n5. Low Price\n6. Volume\n7. Stock Information (First and Last 10 records)\n8. Go to Previous Menu\n"
    print(descriptive_stats_menu)
    print ("-" * 100)
    data_function_choice = input("Please enter your choice: ")
    while data_function_choice != "8":
        try:
            if data_function_choice == "1":
                selection = "Open Price"
                opening_Price = stock_all_data.Open
                Stats_Figures(opening_Price, selection)
            elif data_function_choice == "2":
                selection = "Close Price"
                closing_Price = stock_all_data.Close
                Stats_Figures(closing_Price, selection)
            elif data_function_choice == "3":
                selection = "Adj_Close Price"
                adjacent_closing = stock_all_data.Adj_Close
                Stats_Figures(adjacent_closing,selection)
            elif data_function_choice == "4":
                selection = "High Price"
                high_closing = stock_all_data.High
                Stats_Figures(high_closing, selection)
            elif data_function_choice == "5":
                selection = "Low Price"
                Low_closing = stock_all_data.Low
                Stats_Figures(Low_closing, selection)
            elif data_function_choice == "6":
                selection = "Volume"
                Volume = stock_all_data.Volume
                Stats_Figures(Volume, selection)
            elif data_function_choice == "7":
                print("-" * 77)
                print("The stock details for first 10 days of a given stock   is :")
                print(stock_all_data.head(10))
                print("*" * 77)
                print("The stock details for last 10 days pf a given stock  is :")
                print(stock_all_data.tail(10))
                print("=" * 10)
            else:
                print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
        except ValueError as ex:
            print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
            print(ex.args[0])
        except Exception as ex:
            print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
            print(ex.args[0])
        print ("-" * 100)
        print(descriptive_stats_menu)
        print ("-" * 100)
        data_function_choice = input("Please enter your choice: ")

#Descriptive Analytics- Graphical Analysis 
def graph_menu(stock_all_data,stock_closing_price):
    print ("-" * 100)
    graph_menu = "\nSelect the Visualisation Technique:\n1. Time Series\n2. Moving Averages & Rolling Standard Deviation\n3. Weighted Moving Average\n4. Trendline\n5. Candlestick Chart\n6. Go to Previous Menu\n"
    print(graph_menu)
    print ("-" * 100)
    graph_choice = input("Please enter your choice: ")
    while graph_choice != "6":
        try:
            if graph_choice == "1":
                display_timeseries(stock_all_data,stock_closing_price)
            elif graph_choice == "2":
                display_MovingAverages_SD(stock_all_data,stock_closing_price)
           
            elif graph_choice == "3":
                weighted_moving_average(stock_all_data)                
            elif graph_choice == "4":
                trend_line(stock_all_data,stock_closing_price)              
            elif graph_choice == "5":
                candlestick(stock_all_data) 
            else:
                print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
        except ValueError as v:
            print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
            print(v.args[0])
        except Exception as ex:
            print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input.." , "*" * 10, "\n")
            print(ex.args[0])
        print ("-" * 100)
        print(graph_menu)
        print ("-" * 100)
        graph_choice = input("Please enter your choice: ")
   
def Stats_Figures(Price, selection):
    if Price.empty or Price.isnull().all():
        print(f"No data available for {selection}.")
        return

    print("-" * 100)
    print(f"The details for {selection} are:")
    print(f"The value for {selection} is:\n{Price}")
    print(f"Standard Deviation for {selection} is {np.std(Price)}")
    print(f"Mean for {selection} is {np.mean(Price)}")
    print(f"Quartile range for {selection} is {percentile(Price, [25, 50, 75])}")
    max_value = max(Price)
    min_value = min(Price)
    print(f"Maximum Value for {selection} is {max_value}")
    print(f"Minimum Value for {selection} is {min_value}")
    print(f"Range between Maximum and Minimum Value for {selection} is: {max_value - min_value}")
    print(f"Co-efficient of Variation for {selection} is {ss.variation(Price)}")
    print("-" * 100)
#Display Time Series using Close Price or Volume               
def display_timeseries(stock_all_data,stock_closing_price):
  print ("-" * 100)
  timeseries_menu = "\nSelect the key factor to display the time-series:\n1. Closing Price\n2. Opening Price\n3. Go to Previous Menu\n"
  print(timeseries_menu)
  print ("-" * 100)
  timeseries_choice = input("Please enter your choice: ")
  while timeseries_choice!= "3":
    try:
        if timeseries_choice == "1":
          stock_all_data['Close'].plot(linewidth=5,fontsize=20, legend = True)
          plt.xlabel("Date", fontsize = 20)
          plt.ylabel("Closing Price", fontsize = 20)
          plt.grid(True)
          plt.title('Raw Time Series - Closing Price', fontdict = {'fontsize' : 25})
          plt.show()
        elif timeseries_choice == "2":
          stock_all_data['Open'].plot(linewidth=5,fontsize=20, legend = True)
          plt.xlabel("Date", fontsize = 20)
          plt.ylabel("Opening Price", fontsize = 20)
          plt.grid(True)
          plt.title('Raw Time Series - Opening Price', fontdict = {'fontsize' : 25})
          plt.show()
        else:
          print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
    except ValueError:
          print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
    except Exception as ex:
          print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
    print ("-" * 100)
    print(timeseries_menu)
    print ("-" * 100)
    timeseries_choice = input("Please enter your choice: ")


#Display Moving Averages and SD using Close Price
def display_MovingAverages_SD(stock_all_data_ma,stock_closing_price):
    stock_all_data = stock_all_data_ma.copy()
    try:
        #Rolling Statistics
        window_value = int(input("\nEnter Window Size: "))
        stock_all_data['rollmean'] = stock_all_data.Close.rolling(window_value, center = True, min_periods = 1).mean()
        stock_all_data['rollSTD'] = stock_all_data.Close.rolling(window_value, center = True, min_periods = 1).std()
        # plt.figure(figsize = (15,10))
        plt.xlabel("Date", fontsize = 15)
        plt.ylabel("Closing Price", fontsize = 15)
        plt.plot(stock_all_data['Close'], label = 'Original')
        plt.plot(stock_all_data['rollmean'], label = 'Rolling Mean')
        plt.plot(stock_all_data['rollSTD'], label = 'Rolling STD')
        plt.grid(True)
        plt.legend(loc = 'best')
        plt.title('Moving Averages & Standard Deviation', fontdict = {'fontsize' : 20})
        plt.show()
    except:
        print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
        
#      Display Weighted Moving Averages using Close Price

def weighted_moving_average(stock_all_data_wma):
    
    
    
    try:
        #Weighted Moving Average
         stock_all_data = stock_all_data_wma.copy()
         window_value = int(input("\nEnter Window Size: "))
         weight_no = np.arange(1,window_value+1)
         stock_all_data['WMA'] = stock_all_data['Close'].rolling(window_value).apply(lambda Close: np.dot(Close,weight_no/weight_no.sum()),raw= True)
         plt.xlabel("Date", fontsize = 15)
         plt.ylabel("Closing Price", fontsize = 15)
         plt.plot(stock_all_data['WMA'], color = 'blue')
         plt.title('Weighted Moving Averages', fontdict = {'fontsize' : 20})
         plt.show()
    except:
        print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")

#           Display Trend Line 
def trend_line(stock_all_data,stock_closing_price):
    try:
        fig, ax = plt.subplots()
        dates = stock_all_data['Close'].keys().date
        closing_val = stock_closing_price['Close'].values

        plt.title('Trend Line Graph', fontdict = {'fontsize' : 20})
        plt.xlabel('Date', fontsize = 15)
        plt.ylabel('Closing Price', fontsize = 15)

        x = mdates.date2num(dates)
        y = closing_val
        plt.scatter(x, y)
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x,p(x),"r--")

        loc = mdates.AutoDateLocator()
        plt.gca().xaxis.set_major_locator(loc)
        plt.gca().xaxis.set_major_formatter(mdates.AutoDateFormatter(loc))
        plt.gcf().autofmt_xdate()
        plt.show()

    except Exception as e:
        print(e.args[0])
        print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")

#Display Candlestick Chart using Open, High, Low, Close values       
def candlestick(stock_all_data):
    try:
        stock_all_data = stock_all_data[['Open', 'High', 'Low', 'Close']]
        stock_all_data.reset_index(inplace=True)
        stock_all_data['Date'] = stock_all_data['Date'].map(mdates.date2num)

        ax = plt.subplot()
        ax.grid(True)
        ax.set_xlabel('xlabel', fontsize=12)
        ax.set_ylabel('ylabel', fontsize=12)
        ax.set_axisbelow(True)
        ax.set_title('Candlestick Chart', fontdict = {'fontsize' : 20})
        ax.xaxis_date()
        

        candlestick_ohlc(ax, stock_all_data.values, width=0.75, colorup='g', colordown='r')
        plt.xlabel('Date', fontsize = 15)
        plt.ylabel('Price', fontsize = 15)
        plt.show()
      

    except Exception as e:
        print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
        print(e.args[0])
        



# import streamlit as st
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
# from matplotlib.pylab import rcParams
# from matplotlib import pylab
# from mpl_finance import candlestick_ohlc
# import matplotlib.dates as mdates
# from datetime import datetime, timedelta, date
# import yahoofinance as yf
# import scipy.stats as ss
# from scipy.stats import kurtosis
# from scipy.stats import skew

# rcParams['figure.figsize'] = 15, 10

# # Function to fetch stock data using Yahoo Finance API
# def fetch_stock_data(ticker, start_date, end_date):
#     # Implement the function to fetch stock data using Yahoo Finance API
#     # You can use the yfinance library to fetch the data similar to how it was done in the previous code.
#     stock_data = yf.download(ticker, start=start_date, end=end_date)
#     return stock_data
#     pass

# def descriptive_stats_menu(stock_all_data, stock_closing_price):
#     # Implement the descriptive_stats_menu function
#     descriptive_stats_menu = "\nSelect the key factor for statistical insights: \n1. Opening Price\n2. Closing Price\n3. Adjacent Closing Price\n4. High Price\n5. Low Price\n6. Volume\n7. Stock Information (First and Last 10 records)\n8. Go to Previous Menu\n"
#     print(descriptive_stats_menu)
#     print ("-" * 100)
#     data_function_choice = input("Please enter your choice: ")
#     while data_function_choice != "8":
#         try:
#             if data_function_choice == "1":
#                 selection = "Open Price"
#                 opening_Price = stock_all_data.Open
#                 Stats_Figures(opening_Price, selection)
#             elif data_function_choice == "2":
#                 selection = "Close Price"
#                 closing_Price = stock_all_data.Close
#                 Stats_Figures(closing_Price, selection)
#             elif data_function_choice == "3":
#                 selection = "Adj_Close Price"
#                 adjacent_closing = stock_all_data.Adj_Close
#                 Stats_Figures(adjacent_closing,selection)
#             elif data_function_choice == "4":
#                 selection = "High Price"
#                 high_closing = stock_all_data.High
#                 Stats_Figures(high_closing, selection)
#             elif data_function_choice == "5":
#                 selection = "Low Price"
#                 Low_closing = stock_all_data.Low
#                 Stats_Figures(Low_closing, selection)
#             elif data_function_choice == "6":
#                 selection = "Volume"
#                 Volume = stock_all_data.Volume
#                 Stats_Figures(Volume, selection)
#             elif data_function_choice == "7":
#                 print("-" * 77)
#                 print("The stock details for first 10 days of a given stock   is :")
#                 print(stock_all_data.head(10))
#                 print("*" * 77)
#                 print("The stock details for last 10 days pf a given stock  is :")
#                 print(stock_all_data.tail(10))
#                 print("=" * 10)
#             else:
#                 print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
#         except ValueError as ex:
#             print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
#             print(ex.args[0])
#         except Exception as ex:
#             print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
#             print(ex.args[0])
#         print ("-" * 100)
#         print(descriptive_stats_menu)
#         print ("-" * 100)
#         data_function_choice = input("Please enter your choice: ")
#     pass

# def display_timeseries(stock_all_data, stock_closing_price):
#     # Implement the display_timeseries function
#     print ("-" * 100)
#     timeseries_menu = "\nSelect the key factor to display the time-series:\n1. Closing Price\n2. Opening Price\n3. Go to Previous Menu\n"
#     print(timeseries_menu)
#     print ("-" * 100)
#     timeseries_choice = input("Please enter your choice: ")
#     while timeseries_choice!= "3":
#       try:
#           if timeseries_choice == "1":
#             stock_all_data['Close'].plot(linewidth=5,fontsize=20, legend = True)
#             plt.xlabel("Date", fontsize = 20)
#             plt.ylabel("Closing Price", fontsize = 20)
#             plt.grid(True)
#             plt.title('Raw Time Series - Closing Price', fontdict = {'fontsize' : 25})
#             plt.show()
#           elif timeseries_choice == "2":
#             stock_all_data['Open'].plot(linewidth=5,fontsize=20, legend = True)
#             plt.xlabel("Date", fontsize = 20)
#             plt.ylabel("Opening Price", fontsize = 20)
#             plt.grid(True)
#             plt.title('Raw Time Series - Opening Price', fontdict = {'fontsize' : 25})
#             plt.show()
#           else:
#             print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
#       except ValueError:
#             print("\n" , "*" * 10 , "Input Error: Please enter a valid option." , "*" * 10, "\n")
#       except Exception as ex:
#             print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
#       print ("-" * 100)
#       print(timeseries_menu)
#       print ("-" * 100)
#       timeseries_choice = input("Please enter your choice: ")
#     pass

# def display_MovingAverages_SD(stock_all_data_ma, stock_closing_price):
#     # Implement the display_MovingAverages_SD function
#     stock_all_data = stock_all_data_ma.copy()
#     try:
#         #Rolling Statistics
#         window_value = int(input("\nEnter Window Size: "))
#         stock_all_data['rollmean'] = stock_all_data.Close.rolling(window_value, center = True, min_periods = 1).mean()
#         stock_all_data['rollSTD'] = stock_all_data.Close.rolling(window_value, center = True, min_periods = 1).std()
#         # plt.figure(figsize = (15,10))
#         plt.xlabel("Date", fontsize = 15)
#         plt.ylabel("Closing Price", fontsize = 15)
#         plt.plot(stock_all_data['Close'], label = 'Original')
#         plt.plot(stock_all_data['rollmean'], label = 'Rolling Mean')
#         plt.plot(stock_all_data['rollSTD'], label = 'Rolling STD')
#         plt.grid(True)
#         plt.legend(loc = 'best')
#         plt.title('Moving Averages & Standard Deviation', fontdict = {'fontsize' : 20})
#         plt.show()
#     except:
#         print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
#     pass

# def weighted_moving_average(stock_all_data_wma):
#     # Implement the weighted_moving_average function
      
#     try:
#         #Weighted Moving Average
#          stock_all_data = stock_all_data_wma.copy()
#          window_value = int(input("\nEnter Window Size: "))
#          weight_no = np.arange(1,window_value+1)
#          stock_all_data['WMA'] = stock_all_data['Close'].rolling(window_value).apply(lambda Close: np.dot(Close,weight_no/weight_no.sum()),raw= True)
#          plt.xlabel("Date", fontsize = 15)
#          plt.ylabel("Closing Price", fontsize = 15)
#          plt.plot(stock_all_data['WMA'], color = 'blue')
#          plt.title('Weighted Moving Averages', fontdict = {'fontsize' : 20})
#          plt.show()
#     except:
#         print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
#     pass

# def trend_line(stock_all_data, stock_closing_price):
#     # Implement the trend_line function
#     try:
#         fig, ax = plt.subplots()
#         dates = stock_all_data['Close'].keys().date
#         closing_val = stock_closing_price['Close'].values

#         plt.title('Trend Line Graph', fontdict = {'fontsize' : 20})
#         plt.xlabel('Date', fontsize = 15)
#         plt.ylabel('Closing Price', fontsize = 15)

#         x = mdates.date2num(dates)
#         y = closing_val
#         plt.scatter(x, y)
#         z = np.polyfit(x, y, 1)
#         p = np.poly1d(z)
#         plt.plot(x,p(x),"r--")

#         loc = mdates.AutoDateLocator()
#         plt.gca().xaxis.set_major_locator(loc)
#         plt.gca().xaxis.set_major_formatter(mdates.AutoDateFormatter(loc))
#         plt.gcf().autofmt_xdate()
#         plt.show()

#     except Exception as e:
#         print(e.args[0])
#         print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
#     pass

# def candlestick(stock_all_data):
#     # Implement the candlestick function
#     try:
#         stock_all_data = stock_all_data[['Open', 'High', 'Low', 'Close']]
#         stock_all_data.reset_index(inplace=True)
#         stock_all_data['Date'] = stock_all_data['Date'].map(mdates.date2num)

#         ax = plt.subplot()
#         ax.grid(True)
#         ax.set_xlabel('xlabel', fontsize=12)
#         ax.set_ylabel('ylabel', fontsize=12)
#         ax.set_axisbelow(True)
#         ax.set_title('Candlestick Chart', fontdict = {'fontsize' : 20})
#         ax.xaxis_date()
        

#         candlestick_ohlc(ax, stock_all_data.values, width=0.75, colorup='g', colordown='r')
#         plt.xlabel('Date', fontsize = 15)
#         plt.ylabel('Price', fontsize = 15)
#         plt.show()
      

#     except Exception as e:
#         print("\n" , "*" * 10 , "Sorry an error occurred. Please try again with valid input." , "*" * 10, "\n")
#         print(e.args[0])
        
#     pass

# def descriptive_menu(stock_data, closing_price):
#     st.title("Descriptive Analytics Menu")
#     st.markdown("Select a Choice of services mentioned in Descriptive Analysis:")
    
#     descriptive_choice = st.selectbox("Descriptive Analytics:", ["Statistical Information", "Graphical Visualization"])
#     if descriptive_choice == "Statistical Information":
#         descriptive_stats_menu(stock_data, closing_price)
#     elif descriptive_choice == "Graphical Visualization":
#         graph_menu(stock_data, closing_price)

# def descriptive_stats_menu(stock_all_data, stock_closing_price):
#     st.markdown("Select the key factor for statistical insights:")
#     stats_choice = st.selectbox("Statistics Insight:", ["Opening Price", "Closing Price", "Adj_Close Price", "High Price", "Low Price", "Volume", "Stock Information (First and Last 10 records)"])
    
#     if stats_choice == "Opening Price":
#         selection = "Open Price"
#         Price = stock_all_data['Open']
#         Stats_Figures(Price, selection)
#     elif stats_choice == "Closing Price":
#         selection = "Close Price"
#         Price = stock_all_data['Close']
#         Stats_Figures(Price, selection)
#     elif stats_choice == "Adj_Close Price":
#         selection = "Adj_Close Price"
#         Price = stock_all_data['Adj_Close']
#         Stats_Figures(Price, selection)
#     elif stats_choice == "High Price":
#         selection = "High Price"
#         Price = stock_all_data['High']
#         Stats_Figures(Price, selection)
#     elif stats_choice == "Low Price":
#         selection = "Low Price"
#         Price = stock_all_data['Low']
#         Stats_Figures(Price, selection)
#     elif stats_choice == "Volume":
#         selection = "Volume"
#         Price = stock_all_data['Volume']
#         Stats_Figures(Price, selection)
#     elif stats_choice == "Stock Information (First and Last 10 records)":
#         st.write("The stock details for first 10 days of a given stock are:")
#         st.write(stock_all_data.head(10))
#         st.write("The stock details for last 10 days of a given stock are:")
#         st.write(stock_all_data.tail(10))

# def Stats_Figures(Price, selection):
#     # Implement the Stats_Figures function
#     pass

# def graph_menu(stock_all_data, stock_closing_price):
#     st.markdown("Select the Visualization Technique:")
#     graph_choice = st.selectbox("Graphical Visualization:", ["Time Series", "Moving Averages & Rolling Standard Deviation", "Weighted Moving Average", "Trend Line", "Candlestick Chart"])
    
#     if graph_choice == "Time Series":
#         display_timeseries(stock_all_data, stock_closing_price)
#     elif graph_choice == "Moving Averages & Rolling Standard Deviation":
#         display_MovingAverages_SD(stock_all_data, stock_closing_price)
#     elif graph_choice == "Weighted Moving Average":
#         weighted_moving_average(stock_all_data)
#     elif graph_choice == "Trend Line":
#         trend_line(stock_all_data, stock_closing_price)
#     elif graph_choice == "Candlestick Chart":
#         candlestick(stock_all_data)

# # Code for testing the function
# if __name__ == '__main__':
#     # Fetch the stock data using the fetch_stock_data() function (use some dummy data or provide a method to enter data)
#     stock_data = None
#     closing_price = None
    
#     descriptive_menu(stock_data, closing_price)



