import streamlit as st
import datetime
import time
import numpy as np
import pandas as pd
from pytrends.request import TrendReq

end = datetime.date.today()
start = datetime.date(2017,1,1)
#pytrends_12m = TrendReq(hl='JP')
pytrend = TrendReq(hl='JP')

tf=str(start)+str(" ")+str(end)
print("------------------------------------------")

dummy=pd.date_range(start=start,end=end, freq='D')
data2=pd.DataFrame(index=dummy,columns=["初期データ","データエラー"])
data2["初期データ"]=0
data2["データエラー"]=0
#print(data2.head(2).append(data2.tail(2)))
keyword=["ワールドカップ"]
#print(keyword,tf)

pdPF=data2["初期データ"].copy()
#print("pdPF",pdPF.head(2).append(pdPF.tail(2)))

pdPF_out=pdPF
#print("c",(pd.DataFrame(pdPF_out)).columns[0],pdPF_out.head(1))
#print("pdPF_out",pdPF_out.head(2).append(pdPF_out.tail(2)))
    
with st.form("my_form", clear_on_submit=False):
    name = st.text_input('検索キーワード',value=str(keyword[0]))
    ST = st.date_input('From', value=start)
    ED = st.date_input('To', value=end)
    submitted = st.form_submit_button("調査")
    tf=str(ST)+str(" ")+str(ED)
     
if submitted:
    keyword[0]=name
    st.subheader(name)
    with st.spinner("調査中です..."):
        time.sleep(3)
        #pytrend.build_payload(kw_list=keyword, timeframe='2020-02-26 2023-01-1', geo='JP',gprop='')
        pytrend.build_payload(kw_list=keyword, timeframe=tf, geo='JP',gprop='')
        #print("a",pytrend)
        output1=pytrend.interest_over_time()
        #print("b",output1.tail(2))
        try :
           pdPF_out=output1.iloc[:,0].copy()
           st.line_chart(data = pdPF_out)
           print(pdPF_out)
        except:
           print(type(pdPF_out),"error")

    #st.text(st)
