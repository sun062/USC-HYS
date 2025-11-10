import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 앱 페이지 설정
st.set_page_config(
    page_title="Brainlink EEG 데이터 분석기",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML 파일이 위치한 경로를 설정합니다. (app.py와 같은 레벨의 htmls 폴더)
HTML_FILE_PATH = os.path.join("htmls", "index.html")

def load_html_content(file_path):
    """
    지정된 경로에서 HTML 파일의 내용을 읽어옵니다.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        return f"<h1>오류: HTML 파일을 찾을 수 없습니다. 경로를 확인해주세요: {file_path}</h1>"
    except Exception as e:
        return f"<h1>HTML 파일을 읽는 중 오류 발생: {e}</h1>"

# HTML 내용을 로드합니다.
html_content = load_html_content(HTML_FILE_PATH)

# Streamlit에 HTML 컴포넌트를 임베드합니다.
# height는 HTML 내용에 맞게 적절히 조정했습니다.
if "오류:" in html_content:
    st.error(html_content)
else:
    # Streamlit 컴포넌트를 사용하여 HTML 콘텐츠를 표시합니다.
    # HTML 내부에서 파일 입출력 및 다운로드가 직접 이루어지므로, Python 코드는 HTML을 표시하는 역할만 합니다.
    components.html(html_content, height=850, scrolling=True)

# 애플리케이션 실행 안내
st.sidebar.markdown("## 애플리케이션 정보")
st.sidebar.markdown("이 앱은 순수 JavaScript 기반으로 Brainlink EEG 데이터를 분석합니다.")
st.sidebar.markdown("1. 원본 CSV/XLSX 파일을 업로드하세요.")
st.sidebar.markdown("2. '데이터 처리 및 다운로드' 버튼을 누르면 정리된 `.xlsx` 파일이 다운로드됩니다.")
