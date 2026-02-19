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
        
        /* บังคับใช้ฟอนต์ Sarabun ทั้งแอพ */
        html, body, [class*="css"] {
            font-family: 'Sarabun', sans-serif;
        }

        /* ปรับแต่ง Tabs ให้รองรับ Responsive และ Theme (Dark/Light) อัตโนมัติ */
        .stTabs [data-baseweb="tab-list"] {
            gap: 4px;
        }

        .stTabs [data-baseweb="tab"] {
            height: auto; /* ให้ความสูงยืดหดตามเนื้อหา (สำหรับมือถือ) */
            min-height: 50px;
            white-space: pre-wrap; /* ให้ข้อความขึ้นบรรทัดใหม่ได้ */
            background-color: var(--secondary-background-color); /* ใช้สีพื้นหลังรองของ Theme */
            color: var(--text-color); /* ใช้สีตัวอักษรของ Theme */
            border-radius: 8px 8px 0 0; /* ความโค้งมน */
            border: 1px solid transparent;
            padding: 10px 16px;
            transition: all 0.3s ease;
        }

        /* Effect เมื่อเอาเมาส์ไปชี้ */
        .stTabs [data-baseweb="tab"]:hover {
            color: var(--primary-color);
            border-color: var(--primary-color);
            background-color: var(--background-color);
        }

        /* Tab ที่ถูกเลือก (Active) */
        .stTabs [aria-selected="true"] {
            background-color: var(--primary-color) !important;
            color: white !important; /* บังคับสีขาวเพื่อให้ตัดกับสี Primary เสมอ */
            font-weight: bold;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
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
