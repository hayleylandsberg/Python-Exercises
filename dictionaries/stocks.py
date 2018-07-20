# Instructions
# A block of publicly traded stock has a variety of attributes, we'll look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'AAPL':'Apple, Inc.', 'GOOG': "Google" }

print(stockDict)
# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

purchases = [ ( 'AAPL', 100, '10-sep-2011', 48 ),
 ( 'GOOG', 100, '1-apr-2009', 24 ),
 ( 'CAT', 200, '1-jul-2018', 56 ) ]
# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

for y in purchases:
    print(y[0])
    print(y[1] * y[3])


portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]

    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

    minimal_purchase = (purchase[1], purchase[2], purchase[3])

    try:
        portfolio[ticker].append(purchase) #append the purchase to the ticker list
    except KeyError:
        portfolio[ticker] = list() #if key doesn't exist yet, create it
        portfolio[ticker].append(purchase)

    print("I purchase {} stock for ${}".format(full_company_name, full_purchase_price)) 

    print(portfolio)

    for ticker,purchases in portfolio.items():
        print("---- {} -----".format(ticker))
        total_portfolio_stock_value = 0
        for purchase in purchases:
            total_portfolio_stock_value += purchase[1] * purchase[3]
        print("    {}".format(purchase))
    print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))