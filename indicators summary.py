from pandas import *

def get_statistics_date(trdmnt):
    if trdmnt.month in [1, 2, 3]:
        return to_datetime(f"{trdmnt.year - 1}-12-31")
    elif trdmnt.month in [4, 5, 6]:
        return to_datetime(f"{trdmnt.year}-03-31")
    elif trdmnt.month in [7, 8, 9]:
        return to_datetime(f"{trdmnt.year}-06-30")
    elif trdmnt.month in [10, 11, 12]:
        return to_datetime(f"{trdmnt.year}-09-30")
    else:
        return NaT

# read data
data_1 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/Summary of indicators/1.csv")
data_2 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/Summary of indicators/2.csv")
data_3 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/Summary of indicators/3.csv")

# preprocess data
data_1['Trading Month'] = to_datetime(data_1['Trading Month'])
data_1['Statistics Date'] = data_1['Trading Month'].apply(get_statistics_date)

data_2 = data_2[data_2['Statement Type'] != 'B']
data_2['Ending Date of Statistics'] = to_datetime(data_2['Ending Date of Statistics'])
data_2.sort_values(by=['Stock Code', 'Ending Date of Statistics'], ascending=True, inplace=True)
data_2 = data_2[data_2['Ending Date of Statistics'].dt.month != 1]

data_3['Estbdt'] = to_datetime(data_3['Estbdt'])
data_3_subset = data_3[['Stkcd', 'Estbdt', 'Markettype']]
# merge data
data_1 = data_1.merge(data_2, left_on=['Stock Code', 'Statistics Date'], right_on=['Stock Code', 'Ending Date of Statistics'], how='left')
# compute indicators
data_1['P/E ratios'] = data_1['Monthly Closing Price'] / data_1['EPS']
data_1['P/B ratios'] = data_1['Monthly Closing Price'] / data_1['Net Assets per Share']
data_1_ans = data_1[['Stock Code', 'Trading Month', 'P/E ratios', 'P/B ratios']]

data_2['R&D expense/total asset ratios'] = data_2[' R&D Expenses'] / data_2['Total Assets']
data_2_ans = data_2[['Stock Code', 'Ending Date of Statistics', 'R&D expense/total asset ratios']]

merged_data = merge(data_2, data_3_subset, left_on='Stock Code', right_on='Stkcd', how='left')
merged_data['Ending Date of Statistics'] = to_datetime(merged_data['Ending Date of Statistics'])
merged_data['firm ages'] = (merged_data['Ending Date of Statistics'] - merged_data['Estbdt']) / 365

data_3_ans = merged_data[['Stock Code', 'Ending Date of Statistics', 'Estbdt', 'firm ages', 'Markettype']]

data_Monthly = data_1['Monthly Return Without Cash Dividend Reinvested']
data_PE = data_1['P/E ratios']
data_PB = data_1['P/B ratios']
data_ROA = data_2['Return on Total Assets - A']
data_ROE = data_2['Return on Equity - A']
data_RD_total = data_2['R&D expense/total asset ratios']
data_age = data_3[['firm ages', 'Markettype']]
data_age_main = data_age[(data_age['Markettype'] == 1) | (data_age['Markettype'] == 4) | (data_age['Markettype'] == 64)]
data_age_gem = data_age[(data_age['Markettype'] == 16) | (data_age['Markettype'] == 32)]


print(data_Monthly.describe())
print(data_PE.describe())
print(data_PB.describe())
print(data_ROA.describe())
print(data_ROE.describe())
print(data_RD_total.describe())
print(data_age_main.describe())
print(data_age_gem.describe())



