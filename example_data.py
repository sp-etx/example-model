# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas.tseries.offsets import YearBegin

def make_data():
    index = pd.DatetimeIndex(
        start='2013-01-01 00:00:00',
        end='2015-01-01 00:00:00',
        freq='h',
        tz='UTC')
    index.name = 'Time (UTC)'

    year_start = index + YearBegin(normalize=True) - YearBegin(normalize=True)
    next_year_start = index + YearBegin(normalize=True)
    year_length_values = next_year_start.values - year_start.values
    year_progression_values = index.values - year_start.values
    relative_year_progression = year_progression_values / year_length_values

    annual_cosine = np.cos(relative_year_progression * 2 * np.pi) * 0.5 + 0.5


    (pd.DataFrame
        .from_dict({
            'Renova CHP': pd.Series(data=150 + 40 * annual_cosine, index=index),
            'Other': pd.Series(data=10 + 1200 * annual_cosine, index=index)
            })
        .to_csv('data/heat_history.csv'))

    (pd.Series(
        data=180 + 0 * annual_cosine, index=index, name='Power price')
        .to_csv('data/power_price.csv', header=True))

    (pd.Series(
        data=550 + 100 * annual_cosine, index=index, name='Power demand')
        .to_csv('data/power_demand.csv', header=True))

if __name__ == '__main__':
    make_data()