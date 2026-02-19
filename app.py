import streamlit as st
# นำเข้าโมดูลของ Tab 1 ที่เราแยกไฟล์ไว้
from tabs import summary_structure

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Customs Decoder",
    layout="wide",
    page_icon="📄"
)

# Inject CSS เพื่อความสวยงามและ Font (ใช้ Tailwind และ Font Sarabun)
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Sarabun', sans-serif;
        }
        /* ปรับแต่ง Header ของ Streamlit */
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

# ส่วนหัวของแอพ
st.title("📄 ระบบตรวจสอบข้อมูลศุลกากร")
st.caption("Customs Data Structure & Decoder")

# --- สร้าง Tabs หลัก ---
# เมื่อมีหัวข้อใหม่ ให้เพิ่มชื่อ Tab ใน list นี้
tab_titles = [
    "1. โครงสร้างรหัสใบขน & HS Code", 
    "2. (รอข้อมูลใหม่...)",
    "3. (รอข้อมูลใหม่...)"
]
tabs = st.tabs(tab_titles)

# --- Tab 1: เนื้อหาที่เราทำเสร็จแล้ว ---
with tabs[0]:
    # เรียกฟังก์ชัน render() จากไฟล์ summary_structure.py
    summary_structure.render()

# --- Tab 2: ตัวอย่างสำหรับอนาคต ---
with tabs[1]:
    st.info("พื้นที่สำหรับเนื้อหาใหม่ (Tab 2)")
    # ในอนาคตคุณสามารถสร้างไฟล์ tabs/new_topic.py แล้วเรียกใช้แบบ Tab 1 ได้เลย

# --- Tab 3: ตัวอย่างสำหรับอนาคต ---
with tabs[2]:
    st.info("พื้นที่สำหรับเนื้อหาใหม่ (Tab 3)")
