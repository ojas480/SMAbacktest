from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG


# STRATEGY

class MySMAStrategy(Strategy):

    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10) # 10 day simple moving average
        self.ma2 = self.I(SMA, price, 20) # 10 day simple moving average
    
    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

# BACKTEST
backtest = Backtest(GOOG, MySMAStrategy, commission=0.002, exclusive_orders=True)
stats = backtest.run()

print(stats)

backtest.plot()