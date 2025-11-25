import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
st.set_page_config(layout="wide")
st.set_page_config(page_title="NBA teams comparison", title= "NBA teams comparison")
data = pd.read_csv("nba.csv")
teamnames = sorted(data["hometeamName"].unique())

col1,col2 = st.columns(2)

with col1:
    
    selectedteam1 = st.selectbox("team 1",teamnames)
    teamdata1 = data.loc[(data["hometeamName"]==selectedteam1)|(data["awayteamName"]==selectedteam1)] 
    id1 = data.loc[data["hometeamName"]==selectedteam1]
    id1 = id1["hometeamId"]
    id1 = id1.iloc[0]
    selectmatches1 = data.loc[data["hometeamName"]==id1]
    gameswon1 = teamdata1.loc[teamdata1["winner"]==id1]
    gameswon1 = len(gameswon1)
    
    len1 = len(teamdata1)
    
    st.subheader(selectedteam1)

    c1,c2,c3 = st.columns(3)
    c1.metric("total games",len1)
    c2.metric("Matches won",gameswon1)
    winrate1 = gameswon1/len1*100
    c3.metric("winrate",(f"{winrate1:.1f}%"))
    teamlower1 = selectedteam1.lower()
    st.image(f"https://raw.githubusercontent.com/klunn91/team-logos/refs/heads/master/NBA/{teamlower1}.png")
    gameslost1 = len1-gameswon1
    winratepie1 = pd.Series([gameswon1,gameslost1],["won","lost"])

    winratepie1.plot(kind="pie",autopct="%.1f%%",startangle=90,textprops={'fontsize':16,'color':'green','fontweight':'bold','fontstyle':'italic'})

    st.pyplot(plt,width=450)
    
    
    

    

    #st.write(teamdata1)
with col2:
    selectedteam2 = st.selectbox("team 2",teamnames)
    teamdata2 = data.loc[(data["hometeamName"]==selectedteam2)|(data["awayteamName"]==selectedteam2)]
    id2 = data.loc[data["hometeamName"]==selectedteam2]
    id2 = id2["hometeamId"]
    id2 = id2.iloc[0]
    gameswon2 = teamdata2.loc[teamdata2["winner"]==id2]
    gameswon2 = len(gameswon2)
    
    len2 = len(teamdata2)
    
    st.subheader(selectedteam2)
    c4,c5,c6 = st.columns(3)
    c4.metric("total games",len2)
    c5.metric("Matches won",gameswon2)
    winrate2 = gameswon2/len2*100
    c6.metric("winrate",(f"{winrate2:.1f}%"))
    teamlower2 = selectedteam2.lower()
    st.image(f"https://raw.githubusercontent.com/klunn91/team-logos/refs/heads/master/NBA/{teamlower2}.png")
    gameslost2 = len2-gameswon2
    winratepie2 = pd.Series([gameswon2,gameslost2],["won","lost"])
    plt.figure(figsize=(4,4))
    winratepie2.plot(kind="pie",autopct="%.1f%%",startangle=90,textprops={'fontsize':16,'color':'green','fontweight':'bold','fontstyle':'italic'})
    st.pyplot(plt,width=450)


    #st.write(teamdata2)
    

compare = data.loc[((data["hometeamName"]==selectedteam1) & (data["awayteamName"]==selectedteam2))|((data["hometeamName"]==selectedteam2) & (data["awayteamName"]==selectedteam1))]

compgameswon1 = compare.loc[compare["winner"]==id1]
comparelen1 = len(compgameswon1)



compgameswon2 = compare.loc[compare["winner"]==id2]
comparelen2 = len(compgameswon2)

c7,c8,c9 = st.columns(3)

totalen = len(compare)
c7.metric("matches played by each team",totalen)
c8.metric(f"games won by {selectedteam1:}",comparelen1)
c9.metric(f"games won by {selectedteam2:}",comparelen2)
plt.legend()

plt.figure(figsize=(4,4))
pychart = pd.Series([comparelen1,comparelen2],[selectedteam1,selectedteam2])
if totalen != 0:
    
    pychart.plot(kind="pie",autopct="%.1f%%",startangle=90,textprops={'fontsize':16,'color':'green','fontweight':'bold','fontstyle':'italic'})
    st.pyplot(plt,width=450)
    
else:
    st.write("no games found")

