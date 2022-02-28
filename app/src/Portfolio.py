#Create a portfolio class that has the following three attributes:
#1. ID: unique numerical identifier of the porfoltio
#2. Description: description of the porfoltio (e.g., Finance/Real Estate/Tech)
#3. Stocks: List of stocks in the portfolio


class Portfolio():
    def __init__(self, ID, Description, Stocks):
        self.ID= ID
        self.Description = Description
        self.Stocks = Stocks
