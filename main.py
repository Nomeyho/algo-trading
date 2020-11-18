import os
import sys
import backtrader as bt
from strategy.SmaCross import SmaCross
from datetime import datetime

INITIAL_EQUITY = 1000
COMMISSION = 0.0001

def load_data():
    mod_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    data_path = os.path.join(mod_path, 'data/EURUSD_M15_5K.csv')
    return bt.feeds.GenericCSVData(
        dataname=data_path,
        nullvalue=0.0,
        dtformat=('%Y-%m-%d %H:%M'),
        timeframe=bt.TimeFrame.Minutes,
        compression=15,
#        fromdate=datetime(2020, 1, 1, 00, 00, 00),
#        todate=datetime(2020, 1, 31, 23, 59, 00),
        open=1,
        high=2,
        low=3,
        close=4,
        openinterest=-1
    )


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    data = load_data()

    cerebro.broker.setcash(INITIAL_EQUITY)
    cerebro.broker.setcommission(commission=COMMISSION)
    cerebro.adddata(data)
    cerebro.addstrategy(SmaCross)

    # strats = cerebro.optstrategy(SmaCross, maperiod=range(10, 31))

    print('Starting Portfolio Value: %.4f' % cerebro.broker.getvalue())
    cerebro.run()
    cerebro.plot(style='candlestick')
    print('Final Portfolio Value: %.4f' % cerebro.broker.getvalue())
