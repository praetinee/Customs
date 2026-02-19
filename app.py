import streamlit as st
# นำเข้าโมดูล Tab 1: code_structure (โครงสร้างรหัส)
from tabs import code_structure

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Customs Knowledge Hub", # เปลี่ยน Title ให้ดูเป็นศูนย์รวมความรู้
    layout="wide",
    page_icon="📄"
)

# Inject CSS
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Sarabun', sans-serif;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #f0f2f6;
            border-radius: 4px 4px 0 0;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #4f46e5;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📄 ระบบคลังความรู้ศุลกากร")
st.caption("Customs Knowledge Center")

# --- สร้าง Tabs หลัก ---
tab_titles = [
    "1. โครงสร้างรหัสใบขน & HS Code", 
    "2. (รอข้อมูลใหม่...)",
    "3. (รอข้อมูลใหม่...)"
]
tabs = st.tabs(tab_titles)

# --- Tab 1: Code Structure ---
with tabs[0]:
    code_structure.render()

# --- Tab 2 ---
with tabs[1]:
    st.info("พื้นที่สำหรับโมดูลถัดไป (เช่น พิธีการศุลกากร, กฎหมาย ฯลฯ)")

# --- Tab 3 ---
with tabs[2]:
    st.info("พื้นที่สำหรับโมดูลถัดไป")
