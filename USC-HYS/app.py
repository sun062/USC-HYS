import streamlit as st
import os

# Streamlit 페이지 설정
st.set_page_config(
    page_title="Brainlink 데이터 정리 프로그램",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 현재 스크립트 파일의 디렉토리 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 사이드바에 버튼 추가
st.sidebar.header("페이지 이동")
if st.sidebar.button("Brainlink 데이터 정리 프로그램"):
    st.session_state.page = "index1"

if st.sidebar.button("카페인 유무 데이터 분리 프로그램"):
    st.session_state.page = "index2"

# 새로운 버튼 추가: "평균값 정리 프로그램"
if st.sidebar.button("평균값 정리 프로그램"):
    st.session_state.page = "index3"

# 새로운 버튼 추가: "새로운 페이지 (index4)"
if st.sidebar.button("분석 프로그램 (T-검정)"):
    st.session_state.page = "index4"

# 새로운 버튼 추가: "새로운 페이지 (index5)"
if st.sidebar.button("분석 프로그램 (ANOVA-검정)"):
    st.session_state.page = "index5"

# 초기 페이지 상태 설정
if "page" not in st.session_state:
    st.session_state.page = "index1"

# 선택된 페이지에 따라 HTML 파일 표시
if st.session_state.page == "index1":
    html_file_path = os.path.join(current_dir, "htmls", "index.html")
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=2000, scrolling=True)
    except FileNotFoundError:
        st.error(f"오류: HTML 파일을 찾을 수 없습니다. '{html_file_path}' 경로를 확인해 주세요.")
    except Exception as e:
        st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")

elif st.session_state.page == "index2":
    html_file_path = os.path.join(current_dir, "htmls", "index2.html")
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=2000, scrolling=True)
    except FileNotFoundError:
        st.error(f"오류: HTML 파일을 찾을 수 없습니다. '{html_file_path}' 경로를 확인해 주세요.")
    except Exception as e:
        st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")

# 기존 페이지 경로 (index3)
elif st.session_state.page == "index3":
    html_file_path = os.path.join(current_dir, "htmls", "index3.html")
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=2000, scrolling=True)
    except FileNotFoundError:
        st.error(f"오류: HTML 파일을 찾을 수 없습니다. '{html_file_path}' 경로를 확인해 주세요.")
    except Exception as e:
        st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")

# 새로 추가된 페이지 경로 (index4)
elif st.session_state.page == "index4":
    html_file_path = os.path.join(current_dir, "htmls", "index4.html")
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=2000, scrolling=True)
    except FileNotFoundError:
        st.error(f"오류: HTML 파일을 찾을 수 없습니다. '{html_file_path}' 경로를 확인해 주세요.")
    except Exception as e:
        st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")

# 새로 추가된 페이지 경로 (index5)
elif st.session_state.page == "index5":
    html_file_path = os.path.join(current_dir, "htmls", "index4.html")
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=2000, scrolling=True)
    except FileNotFoundError:
        st.error(f"오류: HTML 파일을 찾을 수 없습니다. '{html_file_path}' 경로를 확인해 주세요.")
    except Exception as e:
        st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")

