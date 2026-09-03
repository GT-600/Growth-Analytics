import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path).drop_duplicates()
    df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")
    for c in ["registrations","attendance","feedback_score"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
    for c in ["event_name","event_type","college","marketing_source"]:
        df[c] = df[c].astype(str).str.strip()
    df["attendance_rate"] = (df["attendance"]/df["registrations"].replace(0,pd.NA)*100).fillna(0)
    return df
