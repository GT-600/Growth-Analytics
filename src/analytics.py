import pandas as pd

def kpis(df):
    r,a=df.registrations.sum(),df.attendance.sum()
    return int(r),int(a),round(a/r*100,2) if r else 0,round(df.feedback_score.mean(),2)

def grouped(df, col):
    x=df.groupby(col,as_index=False)[["registrations","attendance"]].sum()
    x["attendance_rate"]=(x.attendance/x.registrations.replace(0,pd.NA)*100).fillna(0)
    return x.sort_values("registrations",ascending=False)
