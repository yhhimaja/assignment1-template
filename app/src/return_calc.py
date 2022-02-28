def calculate_return(portfolios):
    '''
        Given a list of portfolio objects return a
        dictionary from a portfolio ID to average stock returns 
        in the portfolio
    '''
    pass


def avg_return(stocks):
    '''
        Given a list of stocks return the average return 
        return 0.0  if the list is empty
    '''
    pass



from Portfolio import Portfolios
from Stock import stock
from EmptyStockList import Emptystock

def returncalculation(Portfolios):
    try:
      returncalculation={}
      for Portfolio in Portfolios:
          average = average_return(Portfolio.Stock)
          if returncalculation.get(Portfolio.ID) is None:
              returncalculation[Portfolio.ID] =average
    except Exception as e:
                  print("Exception occurred while calculating return by portfolio:"+str('e'))
    finally:
        return returncalculation


def average_return(stock):
    try:
        if len(stock)==0:
            raise Emptystock
            Total_Return=0
            for Stock in stock:
                    ReturnTotal=Total_Return+stock.Stockrateofreturn
                    return ReturnTotal/len(stock)
    except Exception as e:
        print('error while getting an avgreturn of stocks'+str("e"))
