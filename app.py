import streamlit as st
import requests as r

st.title('hello world!')

response = r.get('https://api.launchpencil.f5.si/zikanwari/?user=1-4&pass=tokoroten')
if response.status_code == 200:
    
    a = response.text.split(',')

    table_data = [[0 for j in range(5)] for i in range(7)]
    table_data[1][2] = 5

    for i in range(0, 35):
        table_data[i//5][i%5] = a[i]

        print ([i//5] + [i%5])

    st.table(table_data)
else:
    # エラーが発生した場合はエラーメッセージを表示する
    print("Error: {}".format(response.status_code))