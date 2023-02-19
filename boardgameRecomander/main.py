import pandas as pd
import streamlit as st
a = pd.read_csv('./bgg_db_1806.csv')

#print(pd.DataFrame(a))

st.title('welcome to my boardgame recommander')
playerNumber_min, playerNumber_max = st.slider('how many game player?', 1, 12, (1,4))
playtime = st.number_input('how many have a time?(min)', 0, 600)
classic = st.checkbox('do you wanna classic game?(before year2000 games')
weight_low, weight_high = st.slider('weight range',0.0, 5.0, (1.0, 4.0))
search = st.button('search!')
if search:
    a = pd.DataFrame(a.iloc[:,[0,1,3,4,5,6,9,10,-1]])
    # 0 순위 1 링크 3 이름 4최소플레이어 5 최대플레이어 6 평균플탐 9 출시년도 10 게임평가레이팅 -1 웨이트
    a = a[a['min_players']>=playerNumber_min]
    a = a[a['max_players']<=playerNumber_max]
    a = a[a['avg_time']<=int(playtime+30)]
    a = a[a['avg_time'] >= int(playtime-30)]
    if classic:
        a = a[2000<=a['year']]
    a = a[a['weight']<=weight_high]
    a = a[a['weight']>=weight_low]
    a = a[0:3]

    name = a.values.tolist()
    st.write(f'당신의 추천게임은 {name[0][2]}입니다!')
    st.write(f'자세한 정보는 이곳을 참고하세요. -> {name[0][1]}')
    st.write(f'그외의 추천 게임으로는 {name[1][2]}, {name[2][2]}가 있습니다.')
    st.write(f'이 게임들이 궁금하시다면 각각의 주소를 참고하세요.')
    st.write(f'{name[1][2]} -> {name[1][1]}')
    st.write(f'{name[2][2]} -> {name[2][1]}')
#streamlit run main.py