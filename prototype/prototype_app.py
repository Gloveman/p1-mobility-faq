import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import math

from findloc import find_address_and_point
from calculate_distance import calculate_distance

ITEMS_PER_PAGE = 4

# 목적지에서 일정 거리 안에 있는 주차장만 반환
# SQL query로 대체 예정
def filter_parking_by_distance(dest_lat, dest_lng, df, radius_km=1.0):
    # 모든 주차장과의 거리 계산 (NumPy 벡터 연산)
    df['distance'] = calculate_distance(dest_lat, dest_lng, df['위도'], df['경도'])
    
    # 반경 이내 데이터만 필터링 및 정렬
    filtered_df = df[df['distance'] <= radius_km].sort_values(by='distance')
    
    return filtered_df

# csv 파일에서 데이터 불러오기
# SQL로 대체 예정
@st.cache_data
def load_total_data(file_path):
    target_columns = ['주차장명', '경도', '위도', '주차장도로명주소', '요금정보']
    
    # csv 파일 읽기
    df = pd.read_csv(file_path, low_memory=False, encoding='euc-kr')
    
    # 프로토타입을 위해 서울특별시 데이터만 필터링
    # 결측치로 인한 에러 방지를 위해 na=False 설정
    seoul_df = df[df['주차장도로명주소'].str.contains('서울특별시', na=False)].copy()
    
    # 필요한 컬럼만 추출
    seoul_df = seoul_df[target_columns]
    
    # 4. 위경도 숫자 변환 및 결측치 제거
    seoul_df['위도'] = pd.to_numeric(seoul_df['위도'], errors='coerce')
    seoul_df['경도'] = pd.to_numeric(seoul_df['경도'], errors='coerce')
    seoul_df = seoul_df.dropna(subset=['위도', '경도'])
    
    return seoul_df

total_parking_df = load_total_data("korea_parkinglots.csv") # 불러온 서울시 전체 데이터

if "current_page" not in st.session_state: #현재 검색중인 페이지
    st.session_state.current_page = 1

if "search_result" not in st.session_state: #검색 결과
    st.session_state.search_result = None

if "selected_parking" not in st.session_state: #선택된 주차장 (아직 구현 못함)
    st.session_state.selected_parking = None

# 페이지 설정
st.set_page_config(layout="wide", page_title="주차장 검색 프로토타입")

# 페이지 제목
st.title("🚗 목적지 주변 주차장 찾기")

# 1. 입력부: 검색바와 버튼
# 검색창과 버튼을 나란히 배치하기 위해 컬럼 사용
col1, col2 = st.columns([4, 1])
with col1:
    target_loc = st.text_input("목적지를 입력하세요", placeholder="예시: 신대방삼거리역")
with col2:
    search_btn = st.button("검색", use_container_width=True)

st.divider() # 구분선

# 2. 메인 화면 구성 (지도 2 : 리스트 1 비율)
main_col2, main_col1 = st.columns([1, 2])

# 검색 시도
if search_btn and target_loc:
    with st.spinner("검색 중..."): # 사용자 경험(UX)을 위한 스피너
        res = find_address_and_point(target_loc, 1)
        if res:
            st.session_state.search_result = res
            nearby_parking = filter_parking_by_distance(res[0][1][0], res[0][1][1], total_parking_df)
            st.session_state.parking_df = nearby_parking
            st.session_state.dest_coord = (res[0][1][0], res[0][1][1])
        else:
            st.error("검색 결과가 없습니다.")


if st.session_state.search_result: # 검색 결과가 나온경우
    # [논리] 여기서 DB 세션을 열고 검색 로직을 수행합니다.
   
    result = st.session_state.search_result
    with main_col1: #지도탭
        st.subheader("📍 주변 지도")
        # 지도 생성
        m = folium.Map(location=[result[0][1][0], result[0][1][1]], zoom_start=15)
        for addr, points in result:
            folium.Marker(
            [points[0], points[1]],
            popup=addr,
            tooltip='테스트',
            icon=folium.Icon(color="red", icon="info-sign")
            ).add_to(m)
        # 데이터 마커 추가
        for row in st.session_state.parking_df.itertuples():
            folium.Marker(
                location=[row.위도, row.경도],
                popup=row.주차장명,
                tooltip=row.주차장명,
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(m)
        
        # 지도 렌더링
        clicked_place = st_folium(m, width='100%', height=800)
        if clicked_place and clicked_place.get("last_object_clicked_tooltip"):
            clicked_name = clicked_place["last_object_clicked_tooltip"]
            st.session_state.selected_parking = clicked_name
            # 페이지 리런을 통해 리스트 색상을 즉시 반영
            st.rerun()

    with main_col2: #리스트탭       
        df = st.session_state.parking_df
        total_items = len(st.session_state.parking_df)
        total_pages = math.ceil(total_items / ITEMS_PER_PAGE)
        start_idx = (st.session_state.current_page - 1) * ITEMS_PER_PAGE
        end_idx = start_idx + ITEMS_PER_PAGE
        page_data = df.iloc[start_idx:end_idx]

        st.subheader(f"📋 검색 결과 ({total_items}개)")
        for index, row in page_data.iterrows():
            with st.container():
                st.markdown(f"### {row['주차장명']}")
                st.write(f'주소: {row['주차장도로명주소']}')
                st.caption(f"요금: {row['요금정보']}")
                if st.button(f"상세보기", key=f"btn_{index}"):
                    st.write(f"{row['주차장명']}의 추가적인 정보나 리뷰 정보 등이 표시됩니다")
                st.divider()
        col_prev, col_page, col_next = st.columns([1, 2, 1])
        with col_prev:
            if st.button("이전") and st.session_state.current_page > 1:
                st.session_state.current_page -= 1
                st.rerun()

        with col_page:
            st.write(f"{st.session_state.current_page} / {total_pages}")

        with col_next:
            if st.button("다음") and st.session_state.current_page < total_pages:
                st.session_state.current_page += 1
                st.rerun()
        

else:
    st.info("목적지를 입력하고 검색 버튼을 눌러주세요.")