# Streamlit 활용한 이미지 생성 AI 앱 구현
# 사전 준비 : streamlit 설치
# 01 가상환경을 만들어서 진행해보기
#  conda create --name st_test01 python=3.10
#  conda activate st_test01
#  pip install streamlit
#  pip install openai
# 
# 02. secrets.toml 만들기
# 03. 프로그램 작성


import streamlit as st
from openai import OpenAI
import os

# OpenAI 클라이언트 초기화
openai_api_key = st.secrets["openai"]["api_key"]
client = OpenAI(api_key  = openai_api_key)

# Streamlit 앱 레이아웃
st.title("AI 이미지 생성기")
st.write("텍스트 프롬프트를 입력하고 AI 이미지를 생성하세요.")

# 텍스트 입력
prompt = st.text_input("프롬프트를 입력하세요:")

# 이미지 장수 선택  
num_images = st.selectbox("이미지 개수 선택", [1, 2])  

# 이미지 사이즈 선택  
image_size = st.selectbox("이미지 사이즈 선택", ["256x256", "512x512", "1024x1024"])  

if st.button("이미지 생성"):
    if prompt:
        try:
            kwargs = {
                "prompt": prompt,
                "n":num_images,
                "size":image_size
            }

            # OpenAI API를 사용하여 이미지 생성
            response = client.images.generate(**kwargs)

            # 생성된 이미지 표시  
            cols = st.columns(num_images)  
            for i, image_url in enumerate(response.data):  
                with cols[i]:  
                    st.image(image_url.url, caption=f"생성된 이미지 {i+1}", use_column_width=True)  

        except Exception as e:
            st.error(f"이미지 생성 중 오류 발생: {e}")
    else:
        st.warning("이미지를 생성하려면 프롬프트를 입력하세요.")
