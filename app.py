import streamlit as st
# นำเข้าโมดูล Tab 1-10
from tabs import code_structure, incoterms, time_limits, warehouses, other_time_limits, core_values, brokerage, jda, trade_knowledge, current_events

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
        
        /* บังคับใช้ฟอนต์ Sarabun ทั้งแอพ และทุก Element อย่างเคร่งครัด */
        html, body, [class*="css"], [class*="st-"], div, h1, h2, h3, h4, h5, h6, p, span, button, input, select, textarea, label, a, li, ul, table, th, td {
            font-family: 'Sarabun', sans-serif !important;
        }

        /* --- ปรับแต่ง Tabs ให้รองรับ Responsive --- */
        /* จัดการกล่องครอบ Tab ให้เลื่อนซ้ายขวาได้บนหน้าจอขนาดเล็ก โดยไม่เสียทรง */
        .stTabs [data-baseweb="tab-list"] {
            gap: 6px;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch; /* เลื่อนลื่นไหลบนมือถือ iOS */
            scrollbar-width: none; /* ซ่อน Scrollbar สำหรับ Firefox */
            -ms-overflow-style: none; /* ซ่อน Scrollbar สำหรับ IE/Edge */
        }
        
        /* ซ่อน Scrollbar สำหรับ Chrome/Safari/Opera */
        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
            display: none; 
        }

        /* ปรับตัว Tab แต่ละอันให้ยืดหยุ่น */
        .stTabs [data-baseweb="tab"] {
            height: auto; 
            min-height: 50px;
            white-space: normal; /* ให้ข้อความยาวๆ ขึ้นบรรทัดใหม่ได้ถ้าหน้าจอเล็ก */
            word-wrap: break-word;
            text-align: center;
            background-color: var(--secondary-background-color); /* ดึงสีพื้นหลังของ Theme (Dark/Light) มาใช้ */
            color: var(--text-color); /* ดึงสีข้อความของ Theme มาใช้ */
            border-radius: 8px 8px 0 0; /* ความโค้งมนมุมบน */
            border: 1px solid transparent;
            padding: 10px 14px;
            transition: all 0.3s ease; /* เพิ่มความนุ่มนวลเวลาเปลี่ยนสถานะ */
        }

        /* Effect เมื่อเอาเมาส์ไปชี้ */
        .stTabs [data-baseweb="tab"]:hover {
            color: var(--primary-color);
            border-color: var(--primary-color);
            background-color: transparent; /* โปร่งใสเพื่อให้กลืนกับพื้นหลังของ Theme */
        }

        /* Tab ที่ถูกเลือก (Active) */
        .stTabs [aria-selected="true"] {
            background-color: var(--primary-color) !important;
            color: #ffffff !important; /* บังคับใช้สีขาวเพื่อให้ตัดกับสีหลักของระบบเสมอ */
            font-weight: 700;
            border-color: var(--primary-color) !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📄 ระบบคลังความรู้ศุลกากร")
st.caption("Customs Knowledge Center - สรุปเนื้อหาและแนวข้อสอบ")

# --- สร้าง Tabs หลัก (เพิ่ม Tab 10 เข้าไปในลิสต์) ---
tab_titles = [
    "1. โครงสร้างรหัสใบขน & HS Code", 
    "2. Incoterms 2020",
    "3. ระยะเวลา (Time Limits)",
    "4. คลังสินค้า & เขตปลอดอากร",
    "5. อายุความ & ประเมินอากร",
    "6. ค่านิยมองค์กร (DRIVE)",
    "7. ตัวแทนออกของ (Broker & AEO)",
    "8. พื้นที่พัฒนาร่วม (JDA)",
    "9. ความรู้การค้าระหว่างประเทศ",
    "10. เหตุการณ์ปัจจุบัน & เก็งข้อสอบ"
]
tabs = st.tabs(tab_titles)

# --- Tab 1: Code Structure ---
with tabs[0]:
    code_structure.render()

# --- Tab 2: Incoterms ---
with tabs[1]:
    incoterms.render()

# --- Tab 3: Time Limits ---
with tabs[2]:
    time_limits.render()

# --- Tab 4: Warehouses ---
with tabs[3]:
    warehouses.render()

# --- Tab 5: Other Time Limits ---
with tabs[4]:
    other_time_limits.render()

# --- Tab 6: Core Values ---
with tabs[5]:
    core_values.render()

# --- Tab 7: Brokerage ---
with tabs[6]:
    brokerage.render()

# --- Tab 8: JDA ---
with tabs[7]:
    jda.render()

# --- Tab 9: Trade Knowledge ---
with tabs[8]:
    trade_knowledge.render()

# --- Tab 10: Current Events & Exam Focus ---
with tabs[9]:
    current_events.render()
