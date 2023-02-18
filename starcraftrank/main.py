import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt                          ## plot 그릴때 사용
a = pd.read_csv('./starcraft_player_data.csv')


from sklearn import datasets                             ## iris와 같은 내장 데이터 사용
from sklearn.model_selection import train_test_split     ## train, test 데이터 분할

from sklearn.linear_model import LinearRegression        ## 선형 회귀분석
from sklearn.linear_model import LogisticRegression      ## 로지스틱 회귀분석
from sklearn.naive_bayes import GaussianNB               ## 나이브 베이즈
from sklearn import svm                                  ## 서포트 벡터 머신
from sklearn import tree                                 ## 의사결정나무
from sklearn.ensemble import RandomForestClassifier      ## 랜덤포레스트

from sklearn.preprocessing import StandardScaler
import streamlit as st
import joblib
from rankshoot import rankshoots
#print(pd.DataFrame(a))
def starcraft_model():
    cause = pd.DataFrame(a.iloc[:,[2,3,4,5,6,13]]) #-1이 스킬사용인데, 데이터가 적어서 인지 정확하지 않아서 제외하기로 함
    consequence = pd.DataFrame(a.LeagueIndex)
    # print(cause)
    # print(consequence)

    df = pd.concat([cause, consequence], axis=1)

    # df['Age'] = df['Age'].replace('?', df['Age'].mean())
    # df['HoursPerWeek'] = df['HoursPerWeek'].replace('?', df['HoursPerWeek'].mean())
    # df['HTotalHours'] = df['TotalHours'].replace('?', df['TotalHours'].mean())

    df = df.replace('?', np.nan)
    df = df.dropna()


    # 시각화
    # sns.pairplot(df[["Age", "HoursPerWeek", "TotalHours", "APM","SelectByHotkeys","ActionLatency","LeagueIndex"]])
    #plt.show()


    # scaler = StandardScaler()
    # df = scaler.fit_transform(df)

    x = df[["Age", "HoursPerWeek", "TotalHours", "APM","SelectByHotkeys","ActionLatency"]]
    y = df[["LeagueIndex"]]
    #x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=0) #스플릿해야하면 이걸 넣어야함 그리고 나서 핏에 트레인들을 넣어주고 예측에 x테스트를 넣어줘야함

    # print(x_train.describe())
    # print(y_train.describe())
    # exit()



    LR = LinearRegression()
    LR.fit(x,y)  # 모수 추정
    # clf.coef_                 # 추정 된 모수 확인(상수항 제외)
    # clf.intercept_            # 추정 된 상수항 확인
    #LR.predict(x_test)        # 예측
    # clf.score(x_test, y_test) # 모형 성능 평가

    joblib.dump(LR, './starcraft.pkl')
#starcraft_model()  #위에 모델 실행
model_from_joblib = joblib.load('./starcraft.pkl')
#print(model_from_joblib.predict(x_test)) 모델 불러와서 예측

st.write('Most objects') # df, err, func, keras!


def linear_streamlit():
    age = float(st.number_input('pick your age', 0, 99))
    apm=float(st.number_input('apm of this game', 0, 1000))
    wholePT=float(st.number_input('playtime of all your life', 0, 100000))
    weekPT=float(st.number_input('playtime of this week', 0, 168))
    selectkey= float(st.number_input('how many use selectkey(단축키) of this game?', 0, 10000)/88.5)
    AL=float(st.number_input('your actionlatency(ms)', 0, 1000000))
    enterBT = st.button('Click me')
    if enterBT:
        x = pd.DataFrame([["Age", "HoursPerWeek", "TotalHours", "APM","SelectByHotkeys","ActionLatency"]])
        x.loc[0] = [age,apm,wholePT,weekPT,selectkey,AL]
        anw = model_from_joblib.predict(x)
        #st.write(model_from_joblib.predict(x))  # see *
        predict = int(round(float(anw[[0],[0]]),0))
        st.write('당신의 예측결과 : ',rankshoots(predict))
        if rankshoots(predict):
            if predict == 1:
                images = './images/bronze.png'
            elif predict == 2:
                images = './images/silver.png'
            elif predict == 3:
                images = './images/gold.png'
            elif predict == 4:
                images = './images/platinum.png'
            elif predict == 5:
                images = './images/diamond.png'
            elif predict == 6:
                images = './images/master.png'
            elif predict == 7:
                images = './images/GM.png'
            elif predict == 8:
                images = './images/progamer.png'
        st.image(f'{images}')
        #round(model_from_joblib.predict(x),1)
linear_streamlit()

# def run_home() :
#     st.subheader("predict your stacraft RANK!")
#     tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
#     tab1.write("Linear Regression")
#     if tab1:
#
#     tab2.write("this is tab 2")
#
#     number_of_news = st.slider('number of news to you want know', min_value=1, max_value=10)
#     name = st.text_input('Search your stock!')


