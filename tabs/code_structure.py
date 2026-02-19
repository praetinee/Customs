import streamlit as st

def render():
    st.header("สรุปโครงสร้างรหัสใบขนสินค้า (14 หลัก)")
    
    # ใช้ st.markdown แบบ unsafe_allow_html เพื่อฉีด CSS ที่รองรับ Theme ของ Streamlit โดยตรง
    # ไม่ใช้ iframe แล้ว เพื่อให้สีพื้นหลังและตัวอักษรปรับตาม Dark/Light Mode อัตโนมัติ
    st.markdown("""
    <style>
        /* Container Card ที่ปรับสีตาม Theme */
        .visual-map-card {
            background-color: var(--secondary-background-color); /* เปลี่ยนสีตามโหมด */
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(128, 128, 128, 0.2); /* เส้นขอบจางๆ */
            overflow-x: auto; /* เลื่อนแนวนอนได้ในมือถือ */
        }
        
        /* Layout */
        .vm-container {
            min-width: 700px; /* ความกว้างขั้นต่ำเพื่อไม่ให้เลขเบียดกัน */
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            font-family: 'Sarabun', sans-serif;
        }
        .vm-group {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 0 2px;
        }
        .vm-digits {
            display: flex;
            gap: 4px;
        }
        
        /* กล่องตัวเลข */
        .vm-digit {
            width: 2.5rem;
            height: 3rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-family: monospace;
            font-size: 1.25rem;
            border-radius: 6px;
            
            /* ใช้สีพื้นหลังหลักของ Theme และสีตัวอักษรหลัก */
            background-color: var(--background-color); 
            color: var(--text-color);
            border: 2px solid rgba(128, 128, 128, 0.3);
            
            position: relative;
            transition: transform 0.2s;
        }
        .vm-digit:hover {
            transform: translateY(-2px);
            border-color: var(--primary-color);
        }

        /* เส้นเชื่อมโยง */
        .vm-line {
            width: 2px;
            height: 16px;
            background-color: rgba(128, 128, 128, 0.4);
            margin-top: 4px;
            margin-bottom: 2px;
        }
        
        /* คำอธิบายด้านล่าง */
        .vm-label {
            font-size: 0.85rem;
            font-weight: 600;
            white-space: nowrap;
            color: var(--text-color);
            opacity: 0.8;
        }

        /* --- Color Variants (Theme Safe) --- */
        /* ใช้สีที่สว่างพอใน Dark mode และเข้มพอใน Light mode */
        
        /* วันที่ (Green) */
        .h-green .vm-digit { border-color: #22c55e; color: #22c55e; }
        .h-green .vm-line { background-color: #22c55e; }
        .h-green .vm-label { color: #22c55e; }

        /* ประเภท (Red) - ทำให้เด่นพิเศษ */
        .h-red .vm-digit { border-color: #ef4444; color: #ef4444; border-width: 2px; background-color: rgba(239, 68, 68, 0.1); }
        .h-red .vm-line { background-color: #ef4444; }
        .h-red .vm-label { color: #ef4444; }

        /* ปี (Yellow/Orange) */
        .h-yellow .vm-digit { border-color: #eab308; color: #eab308; }
        .h-yellow .vm-line { background-color: #eab308; }
        .h-yellow .vm-label { color: #eab308; }

        /* เดือน (Purple) */
        .h-purple .vm-digit { border-color: #a855f7; color: #a855f7; }
        .h-purple .vm-line { background-color: #a855f7; }
        .h-purple .vm-label { color: #a855f7; }

        /* Running (Blue) */
        .h-blue .vm-digit { border-color: #3b82f6; color: #3b82f6; }
        .h-blue .vm-line { background-color: #3b82f6; }
        .h-blue .vm-label { color: #3b82f6; }

    </style>

    <div class="visual-map-card">
        <div class="vm-container">
            <!-- Group 1-2: Ref -->
            <div class="vm-group">
                <div class="vm-digits">
                    <div class="vm-digit">A</div>
                    <div class="vm-digit">1</div>
                </div>
                <div class="vm-line"></div>
                <div class="vm-label">หลัก 1-2</div>
            </div>

            <!-- Group 3-4: Day (Green) -->
            <div class="vm-group h-green">
                <div class="vm-digits">
                    <div class="vm-digit">1</div>
                    <div class="vm-digit">5</div>
                </div>
                <div class="vm-line"></div>
                <div class="vm-label">วันที่</div>
            </div>

            <!-- Group 5: Type (Red) -->
            <div class="vm-group h-red">
                <div class="vm-digits">
                    <div class="vm-digit">0</div>
                </div>
                <div class="vm-line"></div>
                <div class="vm-label">ประเภท</div>
            </div>
            
            <!-- Group 6-7: Year (Yellow) -->
            <div class="vm-group h-yellow">
                <div class="vm-digits">
                    <div class="vm-digit">6</div>
                    <div class="vm-digit">8</div>
                </div>
                <div class="vm-line"></div>
                <div class="vm-label">ปี (พ.ศ.)</div>
            </div>

            <!-- Group 8-9: Month (Purple) -->
            <div class="vm-group h-purple">
                <div class="vm-digits">
                    <div class="vm-digit">0</div>
                    <div class="vm-digit">1</div>
                </div>
                <div class="vm-line"></div>
                <div class="vm-label">เดือน</div>
            </div>

            <!-- Group 10-14: Running (Blue) -->
            <div class="vm-group h-blue">
                <div class="vm-digits">
                    <div class="vm-digit">0</div>
                    <div class="vm-digit">0</div>
                    <div class="vm-digit">0</div>
                    <div class="vm-digit">0</div>
                    <div class="vm-digit">1</div>
                </div>
                <div class="vm-line"></div>
                <div class="vm-label">เลข Running</div>
            </div>

        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- ส่วนเนื้อหาอธิบาย ---
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("คำอธิบายทั่วไป")
        with st.container(border=True):
            st.markdown("""
            **หลักที่ 1-2 (หมวดอักษร)**
            * หลักแรก: ตัวอักษร (A-Z)
            * หลักที่ 2: เลข 0-9 (เปลี่ยนเมื่อเลข Running ครบ 9999)
            """)
        
        with st.container(border=True):
            st.markdown("""
            **วันที่ / เดือน / ปี**
            * :green[**หลัก 3-4**] : วันที่
            * :orange[**หลัก 6-7**] : ปี (พ.ศ.)
            * :violet[**หลัก 8-9**] : เดือน
            """)

    with col2:
        st.subheader("⚠️ ประเภทใบขน (หลักที่ 5)")
        with st.expander("ดูรหัสประเภทใบขนทั้งหมด", expanded=True):
            st.markdown("""
            | รหัส | ความหมาย |
            | :---: | :--- |
            | **0** | ใบขนสินค้าขาเข้า |
            | **1** | ใบขนสินค้าขาออก |
            | **2** | ใบขนสินค้าผ่านแดน |
            | **3** | คำร้องรับของไปก่อน |
            | **4** | คำร้องขอส่งออกของไปก่อน |
            | **5** | ใบขนสินค้าขาเข้าปากระวาง |
            | **6** | ใบขนสินค้าพิเศษผ่านแดนขาออก |
            | **7** | ใบขนสินค้าพิเศษผ่านแดนขาเข้า |
            | **8** | ใบขนสินค้าถ่ายลำ |
            | **A** | ขาเข้าโอนย้ายภายในประเทศ |
            | **B** | ขาออกโอนย้ายภายในประเทศ |
            | **C** | ขาเข้าโอนย้ายจากเขตปลอดอากร |
            | **D** | ขาออกโอนย้ายเข้าเขตปลอดอากร |
            | **E** | คำร้องขอนำของไปแสดงนิทรรศการ |
            | **F** | คำร้องขอทำลาย |
            | **G** | คำร้องขอนำเข้าในเขตอารักขาฯ |
            | **H** | คำร้องขอนำของออกนอกเขตอารักขาฯ |
            """)

    st.divider()

    # --- ส่วน HS Code ---
    st.header("หลักการจำ: พิกัดศุลกากร (HS Code)")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.info("**6 หลักแรก**\n\nมาตรฐานสากล (ใช้เหมือนกันทั่วโลก)")
    with c2:
        st.success("**2 หลักท้าย**\n\nระบบอาเซียน (AHTN) / ไทย")
    with c3:
        st.warning("**รวม 8 หลัก**\n\nที่ใช้สำแดงในใบขนฯ ของไทย")

    st.markdown("""
    > **💡 ข้อควรจำ:** ประเทศไทยใช้รหัสพิกัดแบบ **8 หลัก** (6 หลักสากล + 2 หลักอาเซียน)
    """)
