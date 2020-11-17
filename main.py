import backtrader as bt
from strategy.SmaCrross import SmaCross
from datetime import datetime


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    data = bt.feeds.YahooFinanceData(dataname='AAPL',
                                     fromdate=datetime(2019, 1, 1),
                                     todate=datetime(2019, 12, 31))
    cerebro.adddata(data)

    cerebro.addstrategy(SmaCross)
    cerebro.run()
    cerebro.plot()
