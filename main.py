import pandas as pd
import plotly.express as px
import streamlit as st

# 앱 제목
st.title("Google Drive CSV 데이터 시각화 웹앱")

# Google Drive CSV URL
csv_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

# 데이터 로드
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data(csv_url)

# 데이터 확인
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 컬럼 선택
st.subheader("Plotly 시각화")
numeric_columns = df.select_dtypes(include='number').columns.tolist()

if len(numeric_columns) >= 2:
    x_axis = st.selectbox("X축", numeric_columns)
    y_axis = st.selectbox("Y축", numeric_columns, index=1)
    
    fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    st.plotly_chart(fig)
else:
    st.warning("시각화를 위해 숫자형 컬럼이 2개 이상 필요합니다.")
