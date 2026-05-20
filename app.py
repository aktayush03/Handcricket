import streamlit as st
import random

# Core Configurations
st.set_page_config(
    page_title="AKT.Ayush: Cyber Arena",
    page_icon="🏟️",
    layout="centered"
)

# Light Futuristic Premium Theme Styling Sheet
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;900&family=Rajdhani:wght@600;700&display=swap');
    
    /* Clean Light Futuristic Backdrop */
    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #e6eef5 100%);
        color: #2D3748;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Clean Futuristic Title branding */
    .main-logo {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 38px;
        background: linear-gradient(135deg, #3182ce 0%, #00b5d8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 0px;
        letter-spacing: 2px;
    }
    
    .stadium-sub {
        text-align: center;
        text-transform: uppercase;
        font-family: 'Orbitron', sans-serif;
        color: #718096;
        font-size: 10px;
        letter-spacing: 5px;
        margin-bottom: 30px;
    }

    /* Frosted Glass Floating Arena Board */
    .stadium-pitch {
        background: rgba(255, 255, 255, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(160, 174, 192, 0.25);
        backdrop-filter: blur(10px);
        margin-bottom: 25px;
        text-align: center;
    }

    /* White Glassmorphism Score Split Boxes */
    .hologram-board {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 14px;
        padding: 15px 5px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(160, 174, 192, 0.1);
    }
    
    .score-digits {
        font-family: 'Orbitron', monospace;
        font-size: 44px;
        font-weight: 900;
        line-height: 1.1;
        margin: 5px 0;
        color: #1A202C;
    }

    /* Clean Light Stream Commentary Dock */
    .commentary-box {
        margin-top: 20px; 
        padding: 14px; 
        background: rgba(255, 255, 255, 0.9); 
        border-radius: 12px; 
        border-left: 4px solid #3182ce;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        text-align: left;
    }

    /* Spaced Control Dock to Prevent Touch Button Collision */
    .control-dock {
        background: rgba(255, 255, 255, 0.5);
        border-radius: 16px;
        padding: 15px 10px;
        margin-top: 15px;
        border: 1px solid rgba(255, 255, 255, 0.6);
    }

    /* Light Matte Blue Touch Grid Nodes */
    .stButton>button {
        background: #FFFFFF !important;
        color: #3182ce !important;
        border: 1px solid rgba(49, 130, 206, 0.3) !important;
        border-radius: 12px !important;
        width: 100% !important;
        height: 52px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 2px 5px rgba(160, 174, 192, 0.1) !important;
    }
    
    .stButton>button:hover {
        background: #3182ce !important;
        color: #FFFFFF !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(49, 130, 206, 0.3) !important;
        border-color: #3182ce !important;
    }

    /* Setup Window Main Actions */
    .level-btn>div>button {
        border-radius: 12px !important;
        width: 100% !important;
        height: auto !important;
        padding: 14px !important;
        font-size: 15px !important;
        background: #FFFFFF !important;
        color: #2D3748 !important;
        border: 1px solid rgba(0,0,0,0.08) !important;
    }

    .level-btn>div>button:hover {
        background: #3182ce !important;
        color: #FFFFFF !important;
        border-color: #3182ce !important;
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
    st.session_state.ticker_status = "ARENA ONLINE • AWAITING FIRST BATTER SHOT"

# --- SCREEN 1: PRE-MATCH HUB ---
if not st.session_state.game_started:
    st.markdown("<h1 class='main-logo'>AKT.AYUSH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-sub'>Light Cloud Arena</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='stadium-pitch'>", unsafe_allow_html=True)
    player_name = st.text_input("CODENAME:", value="Ayush")
    st.session_state.player_name = player_name
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("### CHOOSE ARENA GRANDSTAND")
    
    st.markdown("<div class='level-btn'>", unsafe_allow_html=True)
    if st.button("🔵 CLUB SECTOR (Easy Mode • High Run Multiplier)"):
        st.session_state.target_out_score = random.randint(110, 160)
        st.session_state.level = "Easy"
        st.session_state.game_started = True
        st.rerun()
    if st.button("⚪ PAVILION TURF (Moderate Mode • Standard Play)"):
        st.session_state.target_out_score = random.randint(35, 60)
        st.session_state.level = "Moderate"
        st.session_state.game_started = True
        st.rerun()
    if st.button("💎 SKYBOX SUITE (Tough Mode • Instant AI Shutout)"):
        st.session_state.target_out_score = random.randint(0, 3)
        st.session_state.level = "Tough"
        st.session_state.game_started = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: THE ENDGAME WRAP-UP ---
elif st.session_state.game_over:
    st.markdown("<h1 class='main-logo'>MATCH OVER</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-sub'>Arena Recap Registry</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='stadium-pitch' style='border-top: 4px solid #e53e3e;'>
            <h2 style='color:#e53e3e; font-family:Orbitron; font-weight:900;'>🤖 MATRIX AI WINS</h2>
            <p style='color:#718096; font-size:14px; margin-bottom:25px;'>The cloud matrix stays completely undefeated.</p>
            <div style='display:flex; justify-content:space-around; align-items:center;'>
                <div><span style='color:#718096; font-size:12px; font-weight:bold;'>{st.session_state.player_name.upper()}</span><h1 style='font-family:Orbitron; color:#3182ce; margin:5px 0 0 0;'>{st.session_state.player_score}</h1></div>
                <div style='font-size:20px; color:#A0AEC0; font-weight:bold;'>VS</div>
                <div><span style='color:#718096; font-size:12px; font-weight:bold;'>MATRIX AI</span><h1 style='font-family:Orbitron; color:#e53e3e; margin:5px 0 0 0;'>{st.session_state.ai_score}</h1></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🏟️ BOOT NEXT MATCH RECON"):
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.player_score = 0
        st.session_state.ai_score = 0
        st.session_state.is_player_batting = True
        st.session_state.ticker_status = "ARENA ONLINE • AWAITING FIRST BATTER SHOT"
        st.rerun()

# --- SCREEN 3: ACTIVE GAME STADIUM ---
else:
    st.markdown("<h1 class='main-logo'>CYBER ARENA</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='stadium-sub'>🏟️ ARENA: {st.session_state.level.upper()}</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='stadium-pitch'>", unsafe_allow_html=True)
    
    # Modern Light Holographic Scoreboard Split Panels
    col_p, col_ai = st.columns(2)
    with col_p:
        status_text = "• BATTING •" if st.session_state.is_player_batting else "FIELDING"
        lbl_color = "#3182ce" if st.session_state.is_player_batting else "#718096"
        st.markdown(f"""
            <div class='hologram-board'>
                <small style='color:#3182ce; font-weight:700; letter-spacing:1px;'>{st.session_state.player_name.upper()}</small>
                <div class='score-digits'>{st.session_state.player_score}</div>
                <span style='font-size:11px; color:{lbl_color}; font-weight:bold; letter-spacing:1px;'>{status_text}</span>
            </div>
        """, unsafe_allow_html=True)
    with col_ai:
        status_text = "FIELDING" if st.session_state.is_player_batting else "• BATTING •"
        lbl_color = "#718096" if st.session_state.is_player_batting else "#e53e3e"
        st.markdown(f"""
            <div class='hologram-board'>
                <small style='color:#e53e3e; font-weight:700; letter-spacing:1px;'>MATRIX AI</small>
                <div class='score-digits'>{st.session_state.ai_score}</div>
                <span style='font-size:11px; color:{lbl_color}; font-weight:bold; letter-spacing:1px;'>{status_text}</span>
            </div>
        """, unsafe_allow_html=True)
        
    # Commentary panel integration
    st.markdown(f"""
        <div class='commentary-box'>
            <span style='font-family:monospace; font-size:14px; color:#4A5568; font-weight:600;'>🎙️ {st.session_state.ticker_status}</span>
        </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Clean Padded Control Dock container block to isolate the interactive rows
    st.markdown("<div class='control-dock'><p style='text-align:center; font-size:11px; font-weight:700; color:#718096; letter-spacing:2px; margin-top:0px; margin-bottom:12px;'>TAP TO RUN SHOT DELIVERY</p>", unsafe_allow_html=True)
    
    # 3x2 Grid Setup for perfect structural safety against overlap on small phones
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row2_col1, row2_col2, row2_col3 = st.columns(3)
    
    player_choice = None
    
    with row1_col1:
        if st.button("1", key="s_1"): player_choice = 1
    with row1_col2:
        if st.button("2", key="s_2"): player_choice = 2
    with row1_col3:
        if st.button("3", key="s_3"): player_choice = 3
        
    with row2_col1:
        if st.button("4", key="s_4"): player_choice = 4
    with row2_col2:
        if st.button("5", key="s_5"): player_choice = 5
    with row2_col3:
        if st.button("6", key="s_6"): player_choice = 6
        
    st.markdown("</div>", unsafe_allow_html=True)
                
    if player_choice:
        if st.session_state.is_player_batting:
            # Rigged Defense AI Logic
            if st.session_state.player_score >= st.session_state.target_out_score:
                ai_choice = player_choice
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            if player_choice == ai_choice:
                st.session_state.is_player_batting = False
                st.session_state.ticker_status = f"💥 DISMISSED! AI matched your delivery of {player_choice}! Target fixed at {st.session_state.player_score + 1}."
                st.rerun()
            else:
                st.session_state.player_score += player_choice
                st.session_state.ticker_status = f"🏏 SHOT DRIVEN! You score +{player_choice} runs. (AI bowled {ai_choice})"
                st.rerun()
        else:
            # Rigged Chase AI Logic
            target_needed = (st.session_state.player_score + 1) - st.session_state.ai_score
            if target_needed <= 6 and target_needed != player_choice:
                ai_choice = target_needed
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            st.session_state.ai_score += ai_choice
            st.session_state.ticker_status = f"🤖 AI execution sequence success. Played {ai_choice} against your {player_choice} ball."
            
            if st.session_state.ai_score > st.session_state.player_score:
                st.session_state.game_over = True
            st.rerun()
