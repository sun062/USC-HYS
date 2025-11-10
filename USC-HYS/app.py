import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 애플리케이션 설정
st.set_page_config(
    page_title="Brainlink EEG 데이터 분석기",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 현재 스크립트 파일의 디렉토리를 기준으로 'htmls/index.html' 파일 경로 설정
# 실제 Streamlit 환경에서는 'htmls' 폴더를 app.py와 같은 레벨에 생성해야 합니다.
try:
    # app.py와 동일한 위치에 htmls 폴더가 있다고 가정
    html_file_path = os.path.join(os.path.dirname(__file__), "htmls", "index.html")
    
    # HTML 파일 읽기
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_data = f.read()

except FileNotFoundError:
    st.error(f"""
    **오류: 'htmls/index.html' 파일을 찾을 수 없습니다.**
    
    이 애플리케이션을 실행하려면, 아래 단계를 따르세요:
    1. 'app.py' 파일과 동일한 위치에 'htmls' 폴더를 생성합니다.
    2. 생성된 'htmls' 폴더 안에 'index.html' 파일을 저장합니다.
    """)
    st.stop()
except Exception as e:
    st.error(f"HTML 파일 로딩 중 예기치 않은 오류가 발생했습니다: {e}")
    st.stop()


# Streamlit에 HTML 컴포넌트 삽입
# height는 HTML 컨텐츠가 스크롤 없이 충분히 표시될 수 있도록 넉넉하게 설정
components.html(
    html_data,
    height=850, 
    scrolling=True 
)

st.markdown("""
<div style='text-align: center; margin-top: 20px; color: #555;'>
    <p>💡 이 분석기는 모든 데이터 처리(파일 업로드/분석/다운로드)를 <b>사용자 브라우저</b>에서 실행합니다.</p>
    <p>따라서 대용량 파일도 빠르고 안전하게 처리할 수 있습니다.</p>
</div>
""", unsafe_allow_html=True)
