import streamlit as st

def render():
    st.header("สรุปโครงสร้างรหัสใบขนสินค้า (14 หลัก)")
    
    # ส่วนแสดงผลแผนผัง (Visual Map) 
    # ใช้ HTML/Tailwind เพื่อความสวยงาม
    # ใช้ Container แบบ Card สีขาวเสมอเพื่อให้สีของโค้ด (Pastel) แสดงผลชัดเจนในทุก Theme (Dark/Light)
    html_visual_map = """
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Sarabun', sans-serif; margin: 0; padding: 0; background-color: transparent; }
        .code-digit {
            width: 2.5rem; height: 3rem;
            display: flex; align-items: center; justify-content: center;
            font-weight: bold; border-radius: 0.375rem; margin: 0 0.1rem;
            font-family: monospace; font-size: 1.25rem;
            flex-shrink: 0; /* ป้องกันการหดตัวบนจอเล็ก */
        }
        /* Custom Scrollbar */
        ::-webkit-scrollbar { height: 8px; }
        ::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb { background: #c1c1c1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #a8a8a8; }
    </style>
    
    <!-- Wrapper Card -->
    <div class="w-full bg-white rounded-xl border border-gray-200 shadow-sm p-4 md:p-6 overflow-x-auto">
        <!-- Inner Container with min-width to ensure layout integrity -->
        <div class="min-w-[750px] flex flex-col items-center mx-auto">
            <div class="flex mb-2">
                <!-- 1-2 -->
                <div class="flex flex-col items-center mx-1 md:mx-2">
                    <div class="flex">
                        <div class="code-digit bg-gray-100 text-gray-700 border border-gray-200">A</div>
                        <div class="code-digit bg-gray-100 text-gray-700 border border-gray-200">1</div>
                    </div>
                    <div class="h-4 w-px bg-gray-300 mt-2"></div>
                    <span class="text-xs font-bold text-gray-500 mt-1 whitespace-nowrap">หลัก 1-2</span>
                </div>
                <!-- 3-4 -->
                <div class="flex flex-col items-center mx-1 md:mx-2">
                    <div class="flex">
                        <div class="code-digit bg-green-50 text-green-700 border border-green-200">1</div>
                        <div class="code-digit bg-green-50 text-green-700 border border-green-200">5</div>
                    </div>
                    <div class="h-4 w-px bg-green-300 mt-2"></div>
                    <span class="text-xs font-bold text-green-600 mt-1">วัน</span>
                </div>
                <!-- 5 -->
                <div class="flex flex-col items-center mx-1 md:mx-2">
                    <div class="flex">
                        <div class="code-digit bg-red-50 text-red-700 border-2 border-red-400 font-extrabold shadow-sm">0</div>
                    </div>
                    <div class="h-4 w-px bg-red-300 mt-2"></div>
                    <span class="text-xs font-bold text-red-600 mt-1">ประเภท</span>
                </div>
                 <!-- 6-7 -->
                 <div class="flex flex-col items-center mx-1 md:mx-2">
                    <div class="flex">
                        <div class="code-digit bg-yellow-50 text-yellow-700 border border-yellow-200">6</div>
                        <div class="code-digit bg-yellow-50 text-yellow-700 border border-yellow-200">8</div>
                    </div>
                    <div class="h-4 w-px bg-yellow-300 mt-2"></div>
                    <span class="text-xs font-bold text-yellow-600 mt-1">ปี</span>
                </div>
                <!-- 8-9 -->
                <div class="flex flex-col items-center mx-1 md:mx-2">
                    <div class="flex">
                        <div class="code-digit bg-purple-50 text-purple-700 border border-purple-200">0</div>
                        <div class="code-digit bg-purple-50 text-purple-700 border border-purple-200">1</div>
                    </div>
                    <div class="h-4 w-px bg-purple-300 mt-2"></div>
                    <span class="text-xs font-bold text-purple-600 mt-1">เดือน</span>
                </div>
                <!-- 10-14 -->
                <div class="flex flex-col items-center mx-1 md:mx-2">
                    <div class="flex">
                        <div class="code-digit bg-blue-50 text-blue-700 border border-blue-200">0</div>
                        <div class="code-digit bg-blue-50 text-blue-700 border border-blue-200">0</div>
                        <div class="code-digit bg-blue-50 text-blue-700 border border-blue-200">0</div>
                        <div class="code-digit bg-blue-50 text-blue-700 border border-blue-200">0</div>
                        <div class="code-digit bg-blue-50 text-blue-700 border border-blue-200">1</div>
                    </div>
                    <div class="h-4 w-px bg-blue-300 mt-2"></div>
                    <span class="text-xs font-bold text-blue-500 mt-1 whitespace-nowrap">เลข Running</span>
                </div>
            </div>
        </div>
    </div>
    """
    st.components.v1.html(html_visual_map, height=200, scrolling=False) 

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
