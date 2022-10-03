import webbrowser
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

url = "https://finance.yahoo.com/most-active/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAB0BzIcM2lGPhRPg9_i4tBQEUJDLGtXFv2c6ws8cmc6GzWG5zW4wx9GiRNI1ogR1OX8alXFdfbZLKo-KB76CZ1pE5fUhOXyY8vJDge9fFQjeSnyhrCVqfaocVZ_lL5eJIq6zzXnNuJnMKim8A7noReM7HmXIs7YQr71_c2aDhKwI"

tech_stocks = ["AAPL", "MSFT", "INTC"]
tech_stocks_data={}

bank_stocks = ["WFC", "BAC", "C"]
bank_stocks_data={}

commodity_futures = ["GC=F", "SI=F", "CL=F"]
commodity_futures_data={}

cryptocurrencies = ["BTC-USD", "ETH-USD", "XRP-USD"]
cryptocurrencies_data={}

currencies = ["EURUSD=X", "JPY=X", "GBPUSD=X"]
currencies_data={}

mutual_funds = ["PRLAX", "QASGX", "HISFX"]
mutual_funds_data={}

us_treasuries = ["^TNX", "^IRX", "^TYX"]
us_treasuries_data={}

def switch(v): yield lambda *c: v in c
loop=True

while(loop):

    print("================================")
    print("=========    Menu    ===========")
    print("================================")
    print("1)  See Stocks info by category ")
    print("2)  Enter Stock Symbol          ")
    print("3)  Open Yahoo Finance...       ")
    print("4)  Exit                        ")
    print("================================")

    menu = int(input("Choose from Menu above...\n"))
    for case in switch(menu):
        if case(1):
            print("================================")
            print("=========    Menu    ===========")
            print("================================")
            print("1)  tech_stocks                 ")
            print("2)  bank_stocks                 ")
            print("3)  commodity_futures           ")
            print("4)  currencies                  ")
            print("5)  mutual_funds                ")
            print("6)  us_treasuries               ")
            print("7)  Exit                        ")
            print("================================")
            menu_cat = int(input("Choose from Menu above...\n"))
            for case in switch(menu_cat):
                if case(1):
                    for ticker in tech_stocks:
                        ticker_object = yf.Ticker(ticker)
                        # convert info() output from dictionary to dataframe
                        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
                        temp.reset_index(inplace=True)
                        temp.columns = ["Attribute", "Recent"]
                        pd.set_option('display.max_rows', None)
                        # add (ticker, dataframe) to main dictionary
                        tech_stocks_data[ticker] = temp

                    print(tech_stocks_data)

                    export = input("Do you want to Export in CSV? yes/no\n")
                    if (export=="yes") or (export=="Yes") or (export=="YES"):
                        try:
                            with open('tech_stocks_data.csv', 'w') as f:
                                for key in tech_stocks_data.keys():
                                    f.write("%s, %s\n" % (key, tech_stocks_data[key]))
                        except IOError:
                            print("I/O error")
                    else:
                        print("nothing exported")
                    break
                if case(2):

                    for ticker in bank_stocks:
                        ticker_object = yf.Ticker(ticker)

                        # convert info() output from dictionary to dataframe
                        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
                        temp.reset_index(inplace=True)
                        temp.columns = ["Attribute", "Recent"]
                        pd.set_option('display.max_rows', None)
                        # add (ticker, dataframe) to main dictionary
                        bank_stocks_data[ticker] = temp

                    print(bank_stocks_data)

                    export = input("Do you want to Export in CSV? yes/no\n")
                    if (export=="yes") or (export=="Yes") or (export=="YES"):
                        try:
                            with open(' bank_stocks_data.csv', 'w') as f:
                                for key in bank_stocks_data.keys():
                                    f.write("%s, %s\n" % (key, bank_stocks_data[key]))
                        except IOError:
                            print("I/O error")
                    else:
                        print("nothing exported")
                    break

                if case(3):
                    for ticker in commodity_futures:
                        ticker_object = yf.Ticker(ticker)

                        # convert info() output from dictionary to dataframe
                        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
                        temp.reset_index(inplace=True)
                        temp.columns = ["Attribute", "Recent"]
                        pd.set_option('display.max_rows', None)
                        # add (ticker, dataframe) to main dictionary
                        commodity_futures_data[ticker] = temp

                    print(commodity_futures_data)

                    export = input("Do you want to Export in CSV? yes/no\n")
                    if (export=="yes") or (export=="Yes") or (export=="YES"):
                        try:
                            with open(' commodity_futures_data.csv', 'w') as f:
                                for key in commodity_futures_data.keys():
                                    f.write("%s, %s\n" % (key, commodity_futures_data[key]))
                        except IOError:
                            print("I/O error")
                    else:
                        print("nothing exported")
                    break

                if case(4):
                    for ticker in currencies:
                        ticker_object = yf.Ticker(ticker)

                        # convert info() output from dictionary to dataframe
                        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
                        temp.reset_index(inplace=True)
                        temp.columns = ["Attribute", "Recent"]
                        pd.set_option('display.max_rows', None)
                        # add (ticker, dataframe) to main dictionary
                        currencies_data[ticker] = temp

                    print(currencies_data)

                    export = input("Do you want to Export in CSV? yes/no\n")
                    if (export=="yes") or (export=="Yes") or (export=="YES"):
                        try:
                            with open(' currencies_data.csv', 'w') as f:
                                for key in currencies_data.keys():
                                    f.write("%s, %s\n" % (key, currencies_data[key]))
                        except IOError:
                            print("I/O error")
                    else:
                        print("nothing exported")
                    break
                if case(5):
                    for ticker in mutual_funds:
                        ticker_object = yf.Ticker(ticker)

                        # convert info() output from dictionary to dataframe
                        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
                        temp.reset_index(inplace=True)
                        temp.columns = ["Attribute", "Recent"]
                        pd.set_option('display.max_rows', None)
                        # add (ticker, dataframe) to main dictionary
                        mutual_funds_data[ticker] = temp

                    print(mutual_funds_data)

                    export = input("Do you want to Export in CSV? yes/no\n")
                    if (export=="yes") or (export=="Yes") or (export=="YES"):
                        try:
                            with open(' mutual_funds_data.csv', 'w') as f:
                                for key in mutual_funds_data.keys():
                                    f.write("%s, %s\n" % (key, mutual_funds_data[key]))
                        except IOError:
                            print("I/O error")
                    else:
                        print("nothing exported")
                    break
                if case(6):
                    for ticker in us_treasuries:
                        ticker_object = yf.Ticker(ticker)
                        # convert info() output from dictionary to dataframe
                        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
                        temp.reset_index(inplace=True)
                        temp.columns = ["Attribute", "Recent"]
                        pd.set_option('display.max_rows', None)
                        # add (ticker, dataframe) to main dictionary
                        us_treasuries_data[ticker] = temp

                    print(us_treasuries_data)

                    export = input("Do you want to Export in CSV? yes/no\n")
                    if (export=="yes") or (export=="Yes") or (export=="YES"):
                        try:
                            with open(' us_treasuries_data.csv', 'w') as f:
                                for key in us_treasuries_data.keys():
                                    f.write("%s, %s\n" % (key, us_treasuries_data[key]))
                        except IOError:
                            print("I/O error")
                    else:
                        print("nothing exported")
                    break
                elif case(7):
                    exit()
                else:
                    print("Choose something from the menu")
        elif case(2):
            print("================================")
            print("=====Enter another Stock...=====")
            print("================================")
            # Interval required 1 minute
            Stock = input("Enter Stock name: \n")
            data = yf.download(tickers=Stock, period='1d', interval='1m')
            # declare figure
            fig = go.Figure()

            # Candlestick
            fig.add_trace(go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'], name='market data'))

            # Add titles
            fig.update_layout(
                title=Stock+' live share price evolution',
                yaxis_title='Stock Price (USD per Shares)')

            # X-Axes
            fig.update_xaxes(
                rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=15, label="15m", step="minute", stepmode="backward"),
                        dict(count=45, label="45m", step="minute", stepmode="backward"),
                        dict(count=1, label="HTD", step="hour", stepmode="todate"),
                        dict(count=3, label="3h", step="hour", stepmode="backward"),
                        dict(step="all")
                    ])
                )
            )
            # Show
            fig.show()
        elif case(3):
            webbrowser.open(url, new=0, autoraise=True)
        elif case(4):
            exit()
        else:
            print("Choose something from the menu\n")

