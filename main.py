import vectorbt as vbt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class TrendFollowing():

    def __init__(self, stock, startDate : datetime.now(), endDate : datetime.now(), wallet: []):
        self.stock = stock
        self.startDate = startDate
        self.endDate = endDate
        self.wallet = wallet

    def indicator(self, close, mafWindow=9, masWindow=20):
        maFast = vbt.MA.run(close, mafWindow)
        maSlow = vbt.MA.run(close, masWindow)
        # maSuperTrend = vbt.MA.run(close, matWindow)
        trendTemp = np.where(maFast.ma_crossed_below(maSlow), -1, 0)
        trend = np.where(maFast.ma_crossed_below(maSlow), 1, trendTemp)
        return trend

    def treatStock(self, stock):
        startDate = self.startDate
        endDate = self.endDate
        wallet = self.wallet

