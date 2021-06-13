# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:45:28 2021

This script defines three globals that are used to calculate potential gains of a portfolio
The Three variables can be thought of as Parameters recieved from a GUI.

PARAMETERS
    principle : Represents an initial investment in portfolio calculations
    
    int_rate : Estimated yearly interest gained on a portfolio
    
    monthly_cont : Monthly contributions to the extremely theoretical portfolio
    
    num_years : The numver of years for the portfolio to compound over
    
RETURNS
    total_value : Total value of the account after a number of years have gone by. Hopefully millions of dollas
    
    interest_value : Value in the final account that can be attributed to interest growth, not investment
    
    cont_value : Value in the final account that can be attributed to invester monthly contributions
    
    principle : Value in the final account that can be attributed to initial investment
    
@author: rdhurlbu
"""

import numpy as np
from datetime import datetime, timedelta
import holidays

principle = 1000.00

int_rate = 11.1

monthly_cont = 200.00

start = datetime(2021,6,12)
end = datetime(2021,6,19)

def is_market_open(day_to_check: datetime) :
    """ Returns true if the date is a market day"""
    us_holidays = holidays.US()
    # If a holiday
    if day_to_check.strftime('%Y-%m-%d') in us_holidays:
        return False
    # If it's a weekend
    if day_to_check.date().weekday() > 4:
        return False
    
    return True

def count_market_days(start: datetime, end: datetime) :
    """ Range of dates to count is inclusive! """
    num_days = (end - start).days
    all_dates = [start + timedelta(days=x) for x in range(num_days + 1)]
    open_days = [isMarketOpen(day) for day in all_dates]
    return np.count_nonzero(open_days)

num_compounding_days = count_market_days(start, end)
print(num_compounding_days)
