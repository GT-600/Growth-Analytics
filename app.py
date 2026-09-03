import streamlit as st
import plotly.express as px
from src.data_cleaning import load_and_clean_data
from src.analytics import kpis, grouped

st.set_page_config(page_title="Growth Analytics",page_icon="📈",layout="wide")
st.title("📈 Community & Event Growth Analytics")
st.caption("Data → Insight → Decision")

df=load_and_clean_data("data/events.csv")
r,a,rate,fb=kpis(df)
c1,c2,c3,c4=st.columns(4)
c1.metric("Registrations",f"{r:,}"); c2.metric("Attendance",f"{a:,}")
c3.metric("Attendance Rate",f"{rate}%"); c4.metric("Avg Feedback",f"{fb}/5")

events=grouped(df,"event_name")
sources=grouped(df,"marketing_source")
colleges=grouped(df,"college")

st.divider()
l,rgt=st.columns(2)
with l:
    st.subheader("Event Performance")
    st.plotly_chart(px.bar(events,x="event_name",y=["registrations","attendance"],barmode="group"),use_container_width=True)
with rgt:
    st.subheader("Acquisition Conversion")
    st.plotly_chart(px.bar(sources,x="marketing_source",y="attendance_rate",text="attendance_rate"),use_container_width=True)

st.subheader("College Participation")
st.plotly_chart(px.bar(colleges,x="college",y=["registrations","attendance"],barmode="group"),use_container_width=True)

st.subheader("Performance Table")
st.dataframe(events.round(2),use_container_width=True,hide_index=True)

st.subheader("💡 Growth Insights")
st.write(f"• Highest registration source: **{sources.iloc[0].marketing_source}**.")
best=sources.sort_values("attendance_rate",ascending=False).iloc[0]
st.write(f"• Best attendance conversion: **{best.marketing_source} ({best.attendance_rate:.1f}%)**.")
st.write(f"• Top event by registrations: **{events.iloc[0].event_name}**.")
st.write("• Decision focus: compare **reach and conversion**, not registrations alone.")
