import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt                          ## plot 그릴때 사용

import pickle

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

from pathlib import Path



#a = pd.read_csv('./starcraft_player_data.csv')
#print(pd.DataFrame(a))
# def starcraft_model():
#     cause = pd.DataFrame(a.iloc[:,[2,3,4,5,6,13]]) #-1이 스킬사용인데, 데이터가 적어서 인지 정확하지 않아서 제외하기로 함
#     consequence = pd.DataFrame(a.LeagueIndex)
#     # print(cause)
#     # print(consequence)
#
#     df = pd.concat([cause, consequence], axis=1)
#
#     # df['Age'] = df['Age'].replace('?', df['Age'].mean())
#     # df['HoursPerWeek'] = df['HoursPerWeek'].replace('?', df['HoursPerWeek'].mean())
#     # df['HTotalHours'] = df['TotalHours'].replace('?', df['TotalHours'].mean())
#
#     df = df.replace('?', np.nan)
#     df = df.dropna()
#
#
#     # 시각화
#     # sns.pairplot(df[["Age", "HoursPerWeek", "TotalHours", "APM","SelectByHotkeys","ActionLatency","LeagueIndex"]])
#     #plt.show()
#
#
#     # scaler = StandardScaler()
#     # df = scaler.fit_transform(df)
#
#     x = df[["Age", "HoursPerWeek", "TotalHours", "APM","SelectByHotkeys","ActionLatency"]]
#     y = df[["LeagueIndex"]]
#     #x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=0) #스플릿해야하면 이걸 넣어야함 그리고 나서 핏에 트레인들을 넣어주고 예측에 x테스트를 넣어줘야함
#
#     # print(x_train.describe())
#     # print(y_train.describe())
#     # exit()
#
#
#
#     LR = LinearRegression()
#     LR.fit(x,y)  # 모수 추정
#     # clf.coef_                 # 추정 된 모수 확인(상수항 제외)
#     # clf.intercept_            # 추정 된 상수항 확인
#     #LR.predict(x_test)        # 예측
#     # clf.score(x_test, y_test) # 모형 성능 평가
#
#     joblib.dump(LR, './starcraft.pkl')
#
#
# def logistic_model():
#     cause = pd.DataFrame(a.iloc[:,[2,3,4,5,6,13]]) #-1이 스킬사용인데, 데이터가 적어서 인지 정확하지 않아서 제외하기로 함
#     consequence = pd.DataFrame(a.LeagueIndex)
#     # print(cause)
#     # print(consequence)
#
#     df = pd.concat([cause, consequence], axis=1)
#
#     # df['Age'] = df['Age'].replace('?', df['Age'].mean())
#     # df['HoursPerWeek'] = df['HoursPerWeek'].replace('?', df['HoursPerWeek'].mean())
#     # df['HTotalHours'] = df['TotalHours'].replace('?', df['TotalHours'].mean())
#
#     df = df.replace('?', np.nan)
#     df = df.dropna()
#
#
#     # 시각화
#     # sns.pairplot(df[["Age", "HoursPerWeek", "TotalHours", "APM","SelectByHotkeys","ActionLatency","LeagueIndex"]])
#     #plt.show()
#
#
#     # scaler = StandardScaler()
#     # df = scaler.fit_transform(df)
#
#     x = df[["Age", "HoursPerWeek", "TotalHours", "APM","SelectByHotkeys","ActionLatency"]]
#     y = df[["LeagueIndex"]]
#     #x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=0) #스플릿해야하면 이걸 넣어야함 그리고 나서 핏에 트레인들을 넣어주고 예측에 x테스트를 넣어줘야함
#
#     # print(x_train.describe())
#     # print(y_train.describe())
#     # exit()
#
#
#
#     LR = LogisticRegression()
#     LR.fit(x,y)  # 모수 추정
#     # clf.coef_                 # 추정 된 모수 확인(상수항 제외)
#     # clf.intercept_            # 추정 된 상수항 확인
#     #LR.predict(x_test)        # 예측
#     # clf.score(x_test, y_test) # 모형 성능 평가
#
#     joblib.dump(LR, './starcraft_logistic.pkl')


BASE = Path(__file__).resolve().parent
FEATURES = ["Age", "HoursPerWeek", "TotalHours", "APM", "SelectByHotkeys", "ActionLatency"]
RANK_IMAGES = {1: 'bronze.png', 2: 'silver.png', 3: 'gold.png', 4: 'platinum.png',
               5: 'diamond.png', 6: 'master.png', 7: 'GM.png'}


@st.cache_resource
def load_models():
    # 저장해 둔 모델을 먼저 쓰고, 라이브러리 버전 차이로 못 읽으면 같은 데이터로 다시 학습한다
    try:
        linear = joblib.load(BASE / 'starcraft.pkl')
        logistic = joblib.load(BASE / 'starcraft_logistic.pkl')
    except Exception:
        df = pd.read_csv(BASE / 'starcraft_player_data.csv').replace('?', np.nan).dropna()
        x = df[FEATURES].astype(float)
        y = df['LeagueIndex']
        linear = LinearRegression().fit(x, y)
        logistic = LogisticRegression(max_iter=1000).fit(x, y)
    return linear, logistic


model_from_joblib, Logimodel_from_joblib = load_models()


def rank_input(key):
    age = float(st.number_input('pick your age', 0, 99, key=f'{key}_age'))
    apm = float(st.number_input('apm of this game', 0, 1000, key=f'{key}_apm'))
    wholePT = float(st.number_input('playtime of all your life', 0, 100000, key=f'{key}_whole'))
    weekPT = float(st.number_input('playtime of this week', 0, 168, key=f'{key}_week'))
    selectkey = float(st.number_input('how many use selectkey(단축키) of this game?', 0, 10000, key=f'{key}_select') / 88.5)
    AL = float(st.number_input('your actionlatency(ms)', 0, 1000000, key=f'{key}_al'))
    # 모델을 학습시킨 열 순서(FEATURES)에 맞춰 넣는다
    return pd.DataFrame([[age, weekPT, wholePT, apm, selectkey, AL]], columns=FEATURES)


def show_rank(model, x):
    predict = int(round(float(np.ravel(model.predict(x))[0]), 0))
    st.write('당신의 예측결과 : ', rankshoots(predict))
    if predict <= 0:
        return
    st.image(str(BASE / 'images' / RANK_IMAGES.get(predict, 'progamer.png')))


def linear_streamlit():
    x = rank_input('linear')
    if st.button('Scan!', key='linear_scan'):
        show_rank(model_from_joblib, x)


def logistic_streamlit():
    x = rank_input('logistic')
    if st.button('Oracle! predict my rank!', key='logistic_scan'):
        show_rank(Logimodel_from_joblib, x)


def run_home():
    st.subheader("predict your stacraft RANK!")
    tab1, tab2 = st.tabs(["Linear", "Logistic"])
    with tab1:
        st.write("Linear Regression")
        linear_streamlit()
    with tab2:
        st.write("Logistic")
        logistic_streamlit()


run_home()
