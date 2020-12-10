# @Author YoungMinKim
import pandas as pd
def missing_per(df):
    ms=pd.DataFrame(columns=['col','missing'])
    idx = 0
    for i in range(df.shape[1]):
        if df.isnull().sum()[i]>0:
            ms.loc[idx,'col'] = df.isnull().sum().index[i]
            ms.loc[idx,'missing'] = df.isnull().sum()[i]/df.shape[0] * 100
            idx+=1
        else:
            continue
    ms=ms.sort_values(by='missing',ascending=False)
    return ms