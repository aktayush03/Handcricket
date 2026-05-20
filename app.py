import streamlit as st
import random

# Core Configurations
st.set_page_config(
    page_title="AKT.Ayush: Neon Matrix",
    page_icon="⚡",
    layout="centered"
)

# Light Futuristic Masterpiece Layout StyleSheet
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@500;700&display=swap');
    
    /* Clean Futuristic Light Base Canvas */
    .stApp {
        background: linear-gradient(145deg, #f3f7fa 0%, #e2ebf0 100%);
        color: #1a202c;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Asymmetrical Branding Header */
    .main-logo {
        font-family: 'Syncopate', sans-serif;
        font-weight: 700;
        font-size: 32px;
        letter-spacing: 6px;
        background: linear-gradient(135deg, #2b6cb0 0%, #4299e1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 5px;
    }
    
    .stadium-sub {
        text-align: center;
        text-transform: uppercase;
        font-family: 'Syncopate', sans-serif;
        color: #718096;
        font-size: 9px;
        letter-spacing: 4px;
        margin-bottom: 35px;
    }

    /* Ultra-Premium Frosted Glass Arena Board */
    .stadium-pitch {
        background: rgba(255, 255, 255, 0.45);
        border: 1px solid rgba(255, 255, 255, 0.7);
        border-radius: 24px;
        padding: 25px;
        box-shadow: 0 20px 40px rgba(165, 180, 200, 0.2);
        backdrop-filter: blur(15px);
        margin-bottom: 25px;
    }

    /* Floating Holographic Split Panels */
    .hologram-board {
        background: rgba(255, 255, 255, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 16px;
        padding: 18px 10px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(165, 180, 200, 0.15);
    }
    
    .score-digits {
        font-family: 'Syncopate', monospace;
        font-size: 38px;
        font-weight: 700;
        line-height: 1.2;
        margin: 6px 0;
        color: #2d3748;
    }

    /* Minimalist Live Tech Stream Panel */
    .commentary-box {
        margin-top: 20px; 
        padding: 15px; 
        background: rgba(255, 255, 255, 0.9); 
        border-radius: 14px; 
        border-left: 4px solid #4299e1;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        text-align: left;
    }

    /* Isolated Control Pod to prevent button collision */
    .control-dock {
        background: rgba(255, 255, 255, 0.35);
        border-radius: 20px;
        padding: 20px 15px;
        margin-top: 20px;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    /* High-End Tactile Interface Node Keys */
    .stButton>button {
        background: rgba(255, 255, 255, 0.9) !important;
        color: #2b6cb0 !important;
        border: 1px solid rgba(66, 153, 225, 0.25) !important;
        border-radius: 50% !important;
        width: 64px !important;
        height: 64px !important;
        font-family: 'Syncopate', sans-serif !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 10px rgba(165, 180, 200, 0.2) !important;
    }
    
    .stButton>button:hover {
        background: #2b6cb0 !important;
        color: #ffffff !important;
        transform: scale(1.1) translateY(-2px);
        box-shadow: 0 8px 20px rgba(43, 108, 176, 0.35) !important;
        border-color: #2b6cb0 !important;
    }

    /* Setup/Config Buttons */
    .level-btn>div>button {
        border-radius: 14px !important;
        width: 100% !important;
        height: auto !important;
        padding: 16px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        background: #ffffff !important;
        color: #2d3748 !important;
        border: 1px solid rgba(0,0,0,0.05) !important;
    }

    .level-btn>div>button:hover {
        background: #2b6cb0 !important;
        color: #ffffff !important;
        border-color: #2b6cb0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# State Management Logic Initialization
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
if 'ai_score' not in st.session_state:
    st.session_state.ai_score = 0
if 'is_player_batting' not in st.session_state:
    st.session_state.is_player_batting = True
if 'target_out_score' not in st.session_state:
    st.session_state.target_out_score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'ticker_status' not in st.session_state:
    st.session_state.ticker_status = "INTERFACE READY • INITIATE FIRST DELIVERY"

# --- SCREEN 1: PRE-MATCH HUB ---
if not st.session_state.game_started:
    st.markdown("<h1 class='main-logo'>AKT.AYUSH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-sub'>SYSTEM PANEL v3.0</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='stadium-pitch'>", unsafe_allow_html=True)
    player_name = st.text_input("PLAYER SIGNATURE:", value="Ayush")
    st.session_state.player_name = player_name
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("### CHOOSE INTERFACE GRID")
    
    st.markdown("<div class='level-btn'>", unsafe_allow_html=True)
    if st.button("⚡ ALPHA MATCH (Easy Sector • Open Outfield)"):
        st.session_state.target_out_score = random.randint(110, 160)
        st.session_state.level = "Alpha"
        st.session_state.game_started = True
        st.rerun()
    if st.button("💎 BETA MATCH (Moderate Sector • Synced Turf)"):
        st.session_state.target_out_score = random.randint(35, 60)
        st.session_state.level = "Beta"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🔮 OMEGA MATCH (Tough Sector • AI Direct Defeat)"):
        st.session_state.target_out_score = random.randint(0, 3)
        st.session_state.level = "Omega"
        st.session_state.game_started = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: THE ENDGAME WRAP-UP ---
elif st.session_state.game_over:
    st.markdown("<h1 class='main-logo'>TERMINATED</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-sub'>Matrix Sync Complete</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='stadium-pitch' style='border-top: 5px solid #e53e3e;'>
            <h2 style='color:#e53e3e; font-family:Syncopate; font-weight:700;'>🤖 MATRIX AI OVERRIDE</h2>
            <p style='color:#718096; font-size:14px; margin-bottom:25px;'>The core system logic remains unbreached.</p>
            <div style='display:flex; justify-content:space-around; align-items:center;'>
                <div><span style='color:#718096; font-size:11px; font-weight:bold;'>{st.session_state.player_name.upper()}</span><h1 style='font-family:Syncopate; color:#2b6cb0; margin:5px 0 0 0;'>{st.session_state.player_score}</h1></div>
                <div style='font-size:18px; color:#a0aec0; font-family:Syncopate;'>VS</div>
                <div><span style='color:#718096; font-size:11px; font-weight:bold;'>MATRIX AI</span><h1 style='font-family:Syncopate; color:#e53e3e; margin:5px 0 0 0;'>{st.session_state.ai_score}</h1></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 REBOOT SYSTEM MATRIX"):
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.player_score = 0
        st.session_state.ai_score = 0
        st.session_state.is_player_batting = True
        st.session_state.ticker_status = "INTERFACE READY • INITIATE FIRST DELIVERY"
        st.rerun()

# --- SCREEN 3: ACTIVE GAME STADIUM ---
else:
    st.markdown("<h1 class='main-logo'>CYBER ARENA</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='stadium-sub'>MATRIX LAYER: {st.session_state.level.upper()}</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='stadium-pitch'>", unsafe_allow_html=True)
    
    # Asymmetrical Tech Scoreboards
    col_p, col_ai = st.columns(2)
    with col_p:
        status_text = "• ACTIVE BAT •" if st.session_state.is_player_batting else "FIELDING"
        lbl_color = "#2b6cb0" if st.session_state.is_player_batting else "#718096"
        st.markdown(f"""
            <div class='hologram-board' style='border-bottom: 3px solid {lbl_color};'>
                <small style='color:#2b6cb0; font-weight:700; letter-spacing:1px;'>{st.session_state.player_name.upper()}</small>
                <div class='score-digits'>{st.session_state.player_score}</div>
                <span style='font-size:10px; color:{lbl_color}; font-weight:700; letter-spacing:1px;'>{status_text}</span>
            </div>
        """, unsafe_allow_html=True)
    with col_ai:
        status_text = "FIELDING" if st.session_state.is_player_batting else "• ACTIVE BAT •"
        lbl_color = "#718096" if st.session_state.is_player_batting else "#e53e3e"
        st.markdown(f"""
            <div class='hologram-board' style='border-bottom: 3px solid {lbl_color};'>
                <small style='color:#e53e3e; font-weight:700; letter-spacing:1px;'>MATRIX AI</small>
                <div class='score-digits'>{st.session_state.ai_score}</div>
                <span style='font-size:10px; color:{lbl_color}; font-weight:700; letter-spacing:1px;'>{status_text}</span>
            </div>
        """, unsafe_allow_html=True)
        
    # Floating Tech Feed Window
    st.markdown(f"""
        <div class='commentary-box'>
            <span style='font-family:monospace; font-size:13px; color:#4a5568; font-weight:600;'>📟 SYSTEM FEED // {st.session_state.ticker_status}</span>
        </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Fully Spaced 3x2 Circular Input Grid to rule out colliding options
    st.markdown("<div class='control-dock'><p style='text-align:center; font-size:10px; font-weight:700; color:#718096; letter-spacing:3px; margin-top:0px; margin-bottom:15px;'>SELECT INTERFACE DELIVERY</p>", unsafe_allow_html=True)
    
    row1_c1, row1_c2, row1_c3 = st.columns(3)
    row2_c1, row2_c2, row2_c3 = st.columns(3)
    
    player_choice = None
    
    with row1_c1:
        if st.button("1", key="btn_1"): player_choice = 1
    with row1_c2:
        if st.button("2", key="btn_2"): player_choice = 2
    with row1_c3:
        if st.button("3", key="btn_3"): player_choice = 3
        
    with row2_c1:
        if st.button("4", key="btn_4"): player_choice = 4
    with row2_c2:
        if st.button("5", key="btn_5"): player_choice = 5
    with row2_c3:
        if st.button("6", key="btn_6"): player_choice = 6
        
    st.markdown("</div>", unsafe_allow_html=True)
                
    if player_choice:
        if st.session_state.is_player_batting:
            if st.session_state.player_score >= st.session_state.target_out_score:
                ai_choice = player_choice
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            if player_choice == ai_choice:
                st.session_state.is_player_batting = False
                st.session_state.ticker_status = f"CRITICAL COLLISION. AI intercepted choice [{player_choice}]. Switching roles."
                st.rerun()
            else:
                st.session_state.player_score += player_choice
                st.session_state.ticker_status = f"SUCCESS. Node registered +{player_choice} runs. AI vector was [{ai_choice}]."
                st.rerun()
        else:
            target_needed = (st.session_state.player_score + 1) - st.session_state.ai_score
            if target_needed <= 6 and target_needed != player_choice:
                ai_choice = target_needed
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            st.session_state.ai_score += ai_choice
            st.session_state.ticker_status = f"COMPILING. AI logged a smooth [{ai_choice}] play against your delivery grid."
            
            if st.session_state.ai_score > st.session_state.player_score:
                st.session_state.game_over = True
            st.rerun()
