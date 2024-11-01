import pandas as pd
import streamlit as st
a = pd.read_csv('https://raw.githubusercontent.com/oga8867/AI/blob/main/boardgameRecomander/bgg_db_1806.csv')

#print(pd.DataFrame(a))

st.title('welcome to my boardgame recommander')
#playerNumber_min, playerNumber_max = st.slider('how many game player?', 1, 12, (1,4))
Players =st.slider('how many game player?', 1, 12)
playtime = st.number_input('how many have a time?(min) if you want ignore about playtime. set 0', 0, 600)
classic = st.checkbox('do you wanna classic game?(before year2000 games)')
weight_low, weight_high = st.slider('weight range',0.0, 5.0, (1.0, 4.0))

search = st.button('search!')
if search:
    a = pd.DataFrame(a.iloc[:,[0,1,3,4,5,6,9,10,-1]])
    # 0 순위 1 링크 3 이름 4최소플레이어 5 최대플레이어 6 평균플탐 9 출시년도 10 게임평가레이팅 -1 웨이트
    b = a[a['min_players']<=Players]#playerNumber_min]
    b = b[b['max_players']>=Players]#playerNumber_max]
    if playtime != 0:
        b = b[b['avg_time']<=int(playtime+30)]
        b = b[b['avg_time'] >= int(playtime-30)]
    if classic:
        b = b[b['year']<=2000]
    b = b[b['weight']<=weight_high]
    b = b[b['weight']>=weight_low]
    b = b[0:3]
    name = b.values.tolist()
    if len(name)==0:
        st.write('이런... 조건에 맞는 게임은 없군요. 까다로우시네요, 대신 가장 비슷한 게임을 찾아드리겠습니다.')
        b = a[a['min_players'] <=Players] #playerNumber_min]
        b = b[b['max_players'] >=Players] #playerNumber_max]
        b = b[0:3]
        name = b.values.tolist()
        # if classic:
        #     b = b[b['year'] <= 2000]
    if len(name)==0:
        st.write('음... 그래도 게임이 없네요. 혹시 12명이서 600시간동안 게임을 하시려는건 아니겠죠?')
    st.write(f'당신의 추천게임은 {name[0][2]}입니다!')

    st.write(f'자세한 정보는 이곳을 참고하세요. -> {name[0][1]}')
    if len(name) >= 3:
        st.write(f'그외의 추천 게임으로는 {name[1][2]}, {name[2][2]}가 있습니다.')
        st.write(f'이 게임들이 궁금하시다면 각각의 주소를 참고하세요.')
        st.write(f'{name[1][2]} -> {name[1][1]}')
        st.write(f'{name[2][2]} -> {name[2][1]}')
    else:
        st.write(f'이런...추가적인 게임정보가 없네요. 조건에 맞진 않지만 이런건 어떤가요?')
        b = a[a['min_players'] <=Players] #playerNumber_min]
        b = b[b['max_players'] >=Players] #playerNumber_max]
        b = b[0:3]
        name = b.values.tolist()
        st.write(f'조건에 맞진 않지만 추천 게임으로는 {name[1][2]}, {name[2][2]}가 있습니다.')
        st.write(f'이 게임들이 궁금하시다면 각각의 주소를 참고하세요.')
        st.write(f'{name[1][2]} -> {name[1][1]}')
        st.write(f'{name[2][2]} -> {name[2][1]}')
