import streamlit as st

def rankshoots(predict):
    global teeext
    teeext =''
    if predict <= 0:
        teeext = '당신은... 언랭이신것 같습니다. 아마도요'
    elif predict == 1:
        teeext = '뭐... 뭐라고? 내가 브론즈라고? 내가 브론즈라니... 내가 브론즈라니 어헣헣 말도안돼... 말도 안됀다고!'
    elif predict == 2:
        teeext = '당신은 멋진 실딱이. 스타2는 이제부터 시작이다!'
    elif predict == 3:
        teeext = '브실골의 골이시네요. 오랜시간 플레이해서 골드라면 아마 여기가 한계일겁니다 ㅠㅠ'
    elif predict == 4:
        teeext = '플레티넘이네요. 진정한 스타크래프트는 이제 시작이죠. 슬슬 어려워질겁니다.'
    elif predict == 5:
        teeext = '다이아. 요즘엔 다이아도 잡금취급을 받죠? 플레이어가 너무 적어져서 그렇습니다.'
    elif predict == 6:
        teeext = '마스터. 스타크래프트의 고수에 도달했습니다. 왠만하면 주변에 당신보다 스타 잘하는 사람은 적을 겁니다.'
    elif predict == 7:
        teeext = '그마라니 ㄷㄷ 이 정도면 대회 예선을 나가봐도 괜찮겠네요. 조만간 GSL에서 보죠'
    elif predict >= 8:
        teeext = '귀하신분이 이런 누추한곳에 오시다니... 이번 게임에서 적은 내역이 사실이라면 당신은 프로게이머가 틀림없습니다.'
    return(teeext)