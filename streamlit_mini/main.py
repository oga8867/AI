import streamlit as st
import trend
import search_stock
import bugfixer
import QNA
import SDstreamlit
from streamlit_option_menu import option_menu
import streamlit.config
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import io
import os
from riffusion.streamlit import playground

os.makedirs('./news', exist_ok=True)
os.makedirs('./wordcloud', exist_ok=True)
os.makedirs('./stylecloud', exist_ok=True)

# [theme]
# primaryColor="#FFFFFF"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#FFFFFF"
# textColor="#262730"
# font="sans serif"

# st.set_page_config(
#     page_title="GPT's NEWS",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     # menu_items={
#     #     'Get Help': '도움!',
#     #     'Report a bug': "버그낫다고? 내 알바 아니야~",
#     #     'About': "몰라 내 알바 아니야"
#    # }
# )


with st.sidebar:
    choose = option_menu("GPT's News", ["Trends", "Stock search","Bugfixer",'Q&A','image maker'],
                         icons=['house', 'binoculars',"bug","question",'camera'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "7!important", "background-color": "#fafafa"},
        "icon": {"color": "blue", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    })
if choose == "Stock search":
    search_stock.run_home()
elif choose == "Trends":
    trend.trend()
elif choose == "Bugfixer":
    bugfixer.bugfixer()
elif choose =="Q&A":
    QNA.QNA()
elif choose =='image maker':
    SDstreamlit.IM()

#실행   streamlit run main.py
