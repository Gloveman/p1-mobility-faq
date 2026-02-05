import streamlit as st
from streamlit_folium import st_folium
import folium
import mysql.connector
import pandas as pd
import os
import json

from dotenv import load_dotenv

# 1. 페이지 설정

st.set_page_config(layout="wide", page_title="Parking Mate")

# 2. 세션 상태 초기화 (데이터 바구니 생성)
if 'results' not in st.session_state:
    st.session_state['results'] = pd.DataFrame()

# DB 설정
load_dotenv()
DB_CONFIG = json.loads(os.getenv("DB_CONFIG"))

# 3. DB 연결 및 조회 함수
def get_parking_data(search_query):
    print(f'search_query: {search_query}')
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        query = """
            SELECT name, lat, lng, full_address, space_no
            FROM parking_lot
            WHERE full_address LIKE %s OR name LIKE %s
        """
        search_val = f"%{search_query}%"
        df = pd.read_sql(query, conn, params=(search_val, search_val))
        conn.close()
        return df
    except Exception as e:
        st.error(f"DB 연결 오류: {e}")
        return pd.DataFrame()

# --- 레이아웃 시작 ---

# 4. 상단 로고 (검색바는 아래 right_col로 이동)
st.title("🚗 Parking Mate")
st.write("---")

# 5. 메인 레이아웃 분할: 왼쪽(리스트) | 오른쪽(검색창 + 지도)
left_col, right_col = st.columns([1, 2])

# 현재 세션 데이터 가져오기
df = st.session_state['results']

# --- 왼쪽 영역: 검색 결과 리스트 ---
with left_col:
    st.subheader(f"🔍 검색 결과 ({len(df)}건)")
    sort_option = st.radio("정렬", ["가까운순 ▼", "가격순 ▼", "공영"], horizontal=True)
    st.write("---")

    if not df.empty:
        for i, row in df.iterrows():
            with st.container():
                st.markdown(f"""
                <div style="border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:10px; background-color:white;">
                    <h4 style="margin:0; color:black;">{row['name']}</h4>
                    <p style="margin:5px 0; font-size:14px; color:#666;">📍 {row['full_address']}</p>
                    <p style="margin:0; color:#007BFF; font-weight:bold;">🅿️ 주차면수: {row['space_no']}면</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("오른쪽 검색창에서 가고 싶은 곳을 검색해 보세요!")

# --- 오른쪽 영역: 검색창(상단) + 지도(하단) ---
with right_col:
    # 지도 너비에 맞춘 단일 검색 폼
    with st.form(key='main_search_form'):
        search_input_col, search_btn_col = st.columns([5, 1])
        with search_input_col:
            target_location = st.text_input(
                label="검색어 입력",
                placeholder="어디로 가시나요? (예: 강남역, 서초동)",
                label_visibility="collapsed"
            )
        with search_btn_col:
            search_submit = st.form_submit_button(label="검색")

    # 검색 로직 실행
    if search_submit:
        print("버튼클릭")
        if target_location:
            with st.spinner('데이터를 불러오는 중...'):
                df_results = get_parking_data(target_location)
                # print("========================")
                # print(df_results)

                st.session_state['results'] = df_results
                st.rerun()  # 데이터를 세션에 넣은
                # 후 화면 즉시 갱신
        else:
            st.warning("검색어를 입력해 주세요.")

    # 지도 표시 로직
    if not df.empty:
        # 데이터가 있을 때 첫 번째 검색 결과 위치로 이동
        center_lat = df.iloc[0]['lat']
        center_lng = df.iloc[0]['lng']
        zoom_level = 14
    else:
        center_lat, center_lng = 37.5665, 126.9780  # 서울 기본 위치
        zoom_level = 12

    m = folium.Map(location=[center_lat, center_lng], zoom_start=zoom_level)

    # 마커 추가
    for i, row in df.iterrows():
        folium.Marker(
            location=[row['lat'], row['lng']],
            popup=f"<b>{row['name']}</b><br>{row['full_address']}<br>면수: {row['space_no']}",
            tooltip=row['name'],
            icon=folium.Icon(color='orange', icon='info-sign')
        ).add_to(m)

    st_folium(m, width="100%", height=600, key="main_map")