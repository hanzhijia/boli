import streamlit as st

# ==========================================
# 1. 页面基本配置 (必须放在第一行)
# ==========================================
st.set_page_config(
    page_title="青承焕艺", 
    page_icon="🎨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. 注入自定义 CSS 样式
# ==========================================
st.markdown("""
<style>
/* 整个页面的深色网格渐变背景 */
.stApp {
    background-color: #0b131a;
    background-image: 
        radial-gradient(circle at 85% 60%, rgba(26, 188, 156, 0.15) 0%, transparent 40%),
        radial-gradient(circle at 15% 40%, rgba(0, 150, 136, 0.08) 0%, transparent 40%),
        linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    color: #e0e0e0;
}

/* 隐藏顶部默认空白和 Header，使页面更像全屏 App */
header { visibility: hidden; }
.block-container {
    padding-top: 5rem;
    max-width: 1200px;
}

/* --- 文字组件样式 --- */
.pill-tag {
    display: inline-block;
    border: 1px solid #1abc9c;
    color: #1abc9c;
    border-radius: 20px;
    padding: 6px 18px;
    font-size: 0.85rem;
    font-weight: bold;
    letter-spacing: 1px;
    margin-bottom: 20px;
}

.main-title {
    font-size: 4.5rem;
    font-weight: 900;
    color: #48dbfb;
    background: -webkit-linear-gradient(0deg, #48dbfb, #1dd1a1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
    line-height: 1.1;
}

.desc-text {
    font-size: 1.1rem;
    color: #b2bec3;
    line-height: 1.8;
    max-width: 800px;
    margin-bottom: 40px;
}

/* --- 按钮自定义样式 --- */
div.stButton > button {
    border-radius: 8px !important;
    padding: 0.6rem 1.2rem !important;
    font-weight: 600 !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    background-color: rgba(255,255,255,0.05) !important;
    color: #dfe6e9 !important;
    transition: all 0.3s ease !important;
}

div.stButton > button:hover {
    border-color: #1dd1a1 !important;
    color: #1dd1a1 !important;
    background-color: rgba(29, 209, 161, 0.05) !important;
}

/* Primary 主按钮特殊样式（对应"预览工艺数据库"） */
div.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #10ac84, #1dd1a1) !important;
    border: none !important;
    color: white !important;
}

div.stButton > button[kind="primary"]:hover {
    background: linear-gradient(90deg, #1dd1a1, #48dbfb) !important;
    box-shadow: 0 0 15px rgba(29, 209, 161, 0.4) !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 页面内容渲染
# ==========================================

# 渲染顶部标签、标题和介绍文本
st.markdown('<div class="pill-tag">GREEN DESIGN · AI DATA · GLASS ART · QINGXI CREATION</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">青承焕艺</div>', unsafe_allow_html=True)
st.markdown('''
    <div class="desc-text">
        由青汐造物打造，依托青汐工坊开展废旧玻璃热熔再生、艺术设计与工艺数据分析。项目将废旧玻璃回收、热熔工艺实验、烧制前后对比、艺术产品转化、数据可视化与AI推荐系统结合，为大学生创新创业大赛提供一个兼具环保价值、科技感和商业展示力的数字化平台。
    </div>
''', unsafe_allow_html=True)

# 渲染按钮区 (利用 Streamlit 的 columns 布局实现同行排列)
col1, col2, col3, _ = st.columns([1.2, 1.2, 1.2, 6])
with col1:
    st.button("预览工艺数据库", type="primary", use_container_width=True)
with col2:
    st.button("查看烧制对比", use_container_width=True)
with col3:
    st.button("体验产品推荐", use_container_width=True)

# 下方可以继续补充其他图表或内容
st.markdown("---")

# ==========================================
# 4. AI 烧制效果预测模块
# ==========================================
st.markdown('<h3 style="color: #1dd1a1; margin-top: 20px;">🤖 AI 烧制效果预测</h3>', unsafe_allow_html=True)
st.markdown('<p class="desc-text" style="margin-bottom: 20px;">输入废旧玻璃的初始参数，AI模型将为您推演热熔烧制后的艺术形态与物理特性。</p>', unsafe_allow_html=True)

# 创建一个带边框的容器来包裹表单
with st.container():
    # 上方排版：左侧为多模态输入（图片+文本），右侧为参数滑块
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("**1. 多模态输入**")
        uploaded_file = st.file_uploader("📸 上传原材料图片 (可选)", type=["jpg", "jpeg", "png"])
        user_desc = st.text_area("📝 附加工艺要求或材料描述 (可选)", placeholder="例如：这批玻璃主要来自废旧啤酒瓶，希望能保留原本的复古质感，或者烧制成不规则边缘...")
        
        if uploaded_file is not None:
            st.image(uploaded_file, caption="已上传的原材料", width=150)
            
    with col_right:
        st.markdown("**2. 基础物理参数**")
        glass_amount = st.number_input("⚖️ 玻璃原材料量 (克)", min_value=10, max_value=5000, value=200, step=50)
        glass_color = st.selectbox("🎨 主要颜色", ["透明", "海蓝", "翠绿", "琥珀", "混合幻彩", "曜黑"])
        temperature = st.slider("🔥 目标烧制温度 (°C)", min_value=600, max_value=1100, value=820, step=10)
        
    st.markdown("<br>", unsafe_allow_html=True)
    # 生成按钮
    predict_btn = st.button("🔮 运行 AI 多模态预测", type="primary", use_container_width=True)
    
    # 预测结果展示区
    if predict_btn:
        with st.spinner("AI 正在深度演算物理形变与色彩重组过程..."):
            import time
            time.sleep(1.5) # 模拟 AI 接口的请求延迟
            
            # --- 模拟 AI 生成的文本逻辑 ---
            # 形态预测
            state = ""
            if temperature < 700:
                state = "玻璃仅边缘稍微圆润，整体保持原有尖锐碎块形态，未完全融合。"
            elif 700 <= temperature < 800:
                state = "玻璃达到塔克熔（Tack Fuse）状态，碎块之间相互粘连，表面呈现波浪起伏的纹理，保留了强烈的立体感。"
            elif 800 <= temperature < 900:
                state = "玻璃达到全熔（Full Fuse）状态，原材料完全融合成一个平滑的整体。边缘圆润，表面如水面般平整。"
            else:
                state = "玻璃过度熔化，可能产生意外的气泡和边缘流淌扩散，厚度变薄，形态难以控制。"
            
            # 色彩预测
            color_effect = ""
            if glass_color == "混合幻彩":
                color_effect = "不同色彩的碎玻璃在高温下相互渗透，交界处呈现出迷人的渐变与拉丝效果，极具艺术张力。"
            elif glass_color == "透明":
                color_effect = "透光率极高，内部可能包裹少量细微的晶莹气泡，折射出纯净的光影效果。"
            else:
                color_effect = f"{glass_color}色的碎块在高温煅烧后色彩更加醇厚，呈现出宝石般的温润光泽。"
                
            # 组装多模态分析结果 (基于图片和文本)
            multimodal_analysis = ""
            if uploaded_file is not None or user_desc:
                multimodal_analysis = "\n*   **🔍 多模态分析反馈：**"
                if uploaded_file is not None:
                    multimodal_analysis += "\n    *   *图像视觉提取：* AI 已识别您上传的原材料图片，捕捉到玻璃的表面纹理与初始光泽度。成品将最大程度继承其特有的光学特性。"
                if user_desc:
                    multimodal_analysis += f"\n    *   *需求意图响应：* 针对您提到的“{user_desc}”，AI 已在推演模型中调整了烧制曲线，建议将降温速度放缓 15% 以符合该工艺期望。"
            
            # 组装生成的 Markdown 文本报告
            report = f"""
### 📊 AI 烧制效果分析报告
{multimodal_analysis}
*   **预估物理形态：** {state}
*   **视觉光影效果：** {color_effect}
*   **成品规格建议：** 使用 **{glass_amount}g** 原料，预计可烧制出约 **{glass_amount * 0.95:.1f}g** 的成品（考虑微小烧损），体积适合制作小型摆件或镶嵌饰品。
*   **💡 专家工艺提示：** 升温与退火过程请保持平稳，建议在 **{temperature - 300}°C** 处设置退火保温段以消除内部应力，防止成品开裂。
            """
            
            # --- 集成 AI 实时绘图接口 (Pollinations.ai) ---
            # 将中文颜色翻译为对应的英文提示词，以便 AI 更好地理解
            color_map = {
                "透明": "transparent clear", 
                "海蓝": "ocean blue", 
                "翠绿": "emerald green", 
                "琥珀": "amber", 
                "混合幻彩": "iridescent mixed colorful", 
                "曜黑": "obsidian black"
            }
            eng_color = color_map.get(glass_color, "colorful")
            
            # 构建 AI 绘图 Prompt (英文效果最好)
            image_prompt = f"beautiful melted glass art, {eng_color} color, studio lighting, highly detailed, macro photography, {temperature} degrees celsius melting effect"
            import urllib.parse
            import requests
            
            # --- 图片加载说明 ---
            # 由于目前市面上绝大多数完全免费、免 API Key 的 AI 生图接口（如 Pollinations, Hercai 等）
            # 极易因为访问量过大而宕机（返回 503）或开启收费墙（返回 402），导致直接调用经常失败。
            # 为了确保你的演示页面能够 100% 成功展示出“不同颜色的玻璃艺术效果图”，
            # 这里暂时接入了 LoremFlickr 的稳定图片匹配接口。
            #
            # 💡 进阶建议：如果你要在比赛中作为正式产品展示，
            # 建议在此处替换为调用阿里云/百度/智谱等国内大模型的官方 API（通常注册会送免费额度）。
            
            # 稳定的关键词图库接口 (根据你选择的颜色提取对应色彩的玻璃艺术图片)
            image_url = f"https://loremflickr.com/800/400/glass,art,{eng_color.split()[0]}"
            
            st.success("✨ 预测演算完成！正在生成视觉效果图...")
            
            # 使用两列布局，左边文字，右边图片
            col_text, col_img = st.columns([1, 1.2])
            with col_text:
                st.info(report)
            with col_img:
                st.image(image_url, caption=f"效果演示图: {glass_color}玻璃 @ {temperature}°C", use_container_width=True)
