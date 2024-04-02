from pandas import *

#
data_1 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/1.csv")
data_1['P/E ratios'] = data_1['Monthly Closing Price'] / data_1[' Earnings per Share - TTM1']
data_1['P/B ratios'] = data_1['Monthly Closing Price'] / data_1['Net Assets per Share']
data_1_ans = data_1[['Stock Code', 'Trading Month', 'P/E ratios', 'P/B ratios']]
data_1_ans.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/updated_1.csv", index=False)

data_2 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/2.csv")
data_2['R&D expense/total asset ratios'] = data_2[' R&D Expenses'] / data_2['Total Assets']
data_2_ans = data_2[['Stock Code', 'Ending Date of Statistics', 'R&D expense/total asset ratios']]
data_2_ans.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/updated_2.csv", index=False)

data_3 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/3.csv")
data_3['Estbdt'] = to_datetime(data_3['Estbdt'])
data_3_subset = data_3[['Stkcd', 'Estbdt', 'Markettype']]
merged_data = merge(data_2, data_3_subset, left_on='Stock Code', right_on='Stkcd', how='left')
merged_data['Ending Date of Statistics'] = to_datetime(merged_data['Ending Date of Statistics'])
merged_data['firm ages'] = (merged_data['Ending Date of Statistics'] - merged_data['Estbdt']) / 365
data_3_ans = merged_data[['Stock Code', 'Ending Date of Statistics', 'Estbdt', 'firm ages', 'Markettype']]
data_3_ans.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/updated_3.csv", index=False)
