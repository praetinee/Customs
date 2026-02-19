import streamlit as st

def render():
    st.header("สรุปโครงสร้างรหัสใบขนสินค้า (14 หลัก)")
    
    # ส่วนแสดงผลแผนผัง (Visual Map) 
    # ใช้ HTML/Tailwind เพื่อความสวยงามที่ Streamlit ปกติทำได้ยาก
    html_visual_map = """
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .code-digit {
            width: 2.5rem; height: 3rem;
            display: flex; align-items: center; justify-content: center;
            font-weight: bold; border-radius: 0.375rem; margin: 0 0.1rem;
            font-family: monospace; font-size: 1.25rem;
        }
    </style>
    <div style="background-color: white; padding: 20px; border-radius: 10px; border: 1px solid #e5e7eb; overflow-x: auto; margin-bottom: 20px;">
        <div class="min-w-[800px] flex flex-col items-center">
            <div class="flex mb-4">
                <!-- 1-2 -->
                <div class="flex flex-col items-center mx-1">
                    <div class="flex">
                        <div class="code-digit bg-gray-200 text-gray-700">A</div>
                        <div class="code-digit bg-gray-200 text-gray-700">1</div>
                    </div>
                    <div class="h-4 w-px bg-gray-300 mt-1"></div>
                    <span class="text-xs font-bold text-gray-500 mt-1">หลัก 1-2</span>
                </div>
                <!-- 3-4 -->
                <div class="flex flex-col items-center mx-1">
                    <div class="flex">
                        <div class="code-digit bg-green-100 text-green-700">1</div>
                        <div class="code-digit bg-green-100 text-green-700">5</div>
                    </div>
                    <div class="h-4 w-px bg-green-300 mt-1"></div>
                    <span class="text-xs font-bold text-green-600 mt-1">วัน</span>
                </div>
                <!-- 5 -->
                <div class="flex flex-col items-center mx-1">
                    <div class="flex">
                        <div class="code-digit bg-red-100 text-red-700 ring-2 ring-red-400">0</div>
                    </div>
                    <div class="h-4 w-px bg-red-300 mt-1"></div>
                    <span class="text-xs font-bold text-red-600 mt-1">ประเภท</span>
                </div>
                 <!-- 6-7 -->
                 <div class="flex flex-col items-center mx-1">
                    <div class="flex">
                        <div class="code-digit bg-yellow-100 text-yellow-700">6</div>
                        <div class="code-digit bg-yellow-100 text-yellow-700">8</div>
                    </div>
                    <div class="h-4 w-px bg-yellow-300 mt-1"></div>
                    <span class="text-xs font-bold text-yellow-600 mt-1">ปี</span>
                </div>
                <!-- 8-9 -->
                <div class="flex flex-col items-center mx-1">
                    <div class="flex">
                        <div class="code-digit bg-purple-100 text-purple-700">0</div>
                        <div class="code-digit bg-purple-100 text-purple-700">1</div>
                    </div>
                    <div class="h-4 w-px bg-purple-300 mt-1"></div>
                    <span class="text-xs font-bold text-purple-600 mt-1">เดือน</span>
                </div>
                <!-- 10-14 -->
                <div class="flex flex-col items-center mx-1">
                    <div class="flex">
                        <div class="code-digit bg-blue-50 text-blue-700">0</div>
                        <div class="code-digit bg-blue-50 text-blue-700">0</div>
                        <div class="code-digit bg-blue-50 text-blue-700">0</div>
                        <div class="code-digit bg-blue-50 text-blue-700">0</div>
                        <div class="code-digit bg-blue-50 text-blue-700">1</div>
                    </div>
                    <div class="h-4 w-px bg-blue-300 mt-1"></div>
                    <span class="text-xs font-bold text-blue-500 mt-1">เลข Running</span>
                </div>
            </div>
        </div>
    </div>
    """
    st.components.v1.html(html_visual_map, height=180, scrolling=True)

    # --- ส่วนเนื้อหาอธิบาย (Layout 2 คอลัมน์) ---
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
            * <span style='color:green'><b>หลัก 3-4</b></span> : วันที่
            * <span style='color:#ca8a04'><b>หลัก 6-7</b></span> : ปี (พ.ศ.)
            * <span style='color:purple'><b>หลัก 8-9</b></span> : เดือน
            """, unsafe_allow_html=True)

    with col2:
        st.subheader("⚠️ ประเภทใบขน (หลักที่ 5)")
        # ใช้ Expander เพื่อประหยัดพื้นที่
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
    
    # ใช้ Column ของ Streamlit ทำกล่อง 3 กล่อง
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
