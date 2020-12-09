# @Author YoungMinKim
# baekjoon

import pandas as pd
from sklearn.preprocessing import OneHotEncoder # onehotencoding dataframe 변환 함수
def ohe_trans(data,col):
    ohe=OneHotEncoder()
    x= ohe.fit_transform(data[col].values.reshape(-1,1)).toarray()
    tp = []
    for i in range(data[col].unique().size): # onehot 컬럼 생성
        tp.append(col[0]+str(i)) 
    ohe_df = pd.DataFrame(x,columns = tp)
    return ohe_df