from pandas import *

data_1 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/1.csv")
data_update_1 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/updated_1.csv")
data_2 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/2.csv")
data_update_2 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/updated_2.csv")


data_update_3 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/updated_3.csv")
data_Monthly = data_1['Monthly Return Without Cash Dividend Reinvested']
data_PE = data_update_1['P/E ratios']
data_PB = data_update_1['P/B ratios']
print(data_Monthly.describe())
print(data_PE.describe())
print(data_PB.describe())


data_ROA = data_2['Return on Total Assets - A']
data_ROE = data_2['Return on Equity - A']
data_RD_total = data_update_2['R&D expense/total asset ratios']
data_age = data_update_3[['firm ages', 'Markettype']]
data_age_main = data_age[(data_age['Markettype'] == 1) | (data_age['Markettype'] == 4) | (data_age['Markettype'] == 64)]
data_age_gem = data_age[(data_age['Markettype'] == 16) | (data_age['Markettype'] == 32)]

print(data_ROA.describe())
print(data_ROE.describe())
print(data_RD_total.describe())
print(data_age_main.describe())
print(data_age_gem.describe())
