from pandas import *

# data1
data_1 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/1.csv")
data_1['Trading Month'] = to_datetime(data_1['Trading Month'])
data_1.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/1.csv", index=False)

# data2
data_2 = read_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/2.csv")
data_2 = data_2[data_2['Statement Type'] != 'B']
data_2['Ending Date of Statistics'] = to_datetime(data_2['Ending Date of Statistics'])
data_2.sort_values(by=['Stock Code', 'Ending Date of Statistics'], ascending=True, inplace=True)
data_2 = data_2[data_2['Ending Date of Statistics'].dt.month != 1]
data_2.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/2.csv", index=False)


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

data_1['Statistics Date'] = data_1['Trading Month'].apply(get_statistics_date)
data_1 = data_1.merge(data_2, left_on=['Stock Code', 'Statistics Date'], right_on=['Stock Code', 'Ending Date of Statistics'], how='left')
data_1.to_csv("C:/Users/Charles Lee/OneDrive - CUHK-Shenzhen/FIN3080_2/1.csv", index=False)




