import streamlit as st
import random

# Core Configurations
st.set_page_config(
    page_title="AKT.Ayush: Cyber Arena",
    page_icon="🏟️",
    layout="centered"
)

# Premium Minimalist Neon Masterpiece Theme Styling Sheet
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;800;900&family=Rajdhani:wght@600;700&display=swap');
    
    /* Deep Midnight Black Clean Canvas */
    .stApp {
        background: #070a13;
        color: #FFFFFF;
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* Clean, Large Premium Logo */
    .main-logo {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 42px;
        color: #00FFCC;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.6);
        text-align: center;
        margin-top: 20px;
        margin-bottom: 0px;
        letter-spacing: 3px;
    }
    
    .stadium-sub {
        text-align: center;
        text-transform: uppercase;
        font-family: 'Orbitron', sans-serif;
        color: #657585;
        font-size: 11px;
        letter-spacing: 6px;
        margin-bottom: 35px;
    }

    /* Minimalist Floating Stadium Pitch Container */
    .stadium-pitch {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        margin-bottom: 25px;
        text-align: center;
    }

    /* Glassmorphism Floating Scoreboard Panels */
    .hologram-board {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 20px 10px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }
    
    .score-digits {
        font-family: 'Orbitron', monospace;
        font-size: 48px;
        font-weight: 800;
        line-height: 1.1;
        margin: 10px 0;
        letter-spacing: -1px;
    }

    /* Premium Sleek Live Arena Commentary Bar */
    .commentary-box {
        margin-top: 25px; 
        padding: 15px; 
        background: rgba(0, 0, 0, 0.4); 
        border-radius: 12px; 
        border-left: 3px solid #3399FF;
        box-shadow: 0 0 15px rgba(51, 153, 255, 0.1);
        text-align: left;
    }

    /* Premium Touch-Optimized Circular Gesture Buttons */
    .stButton>button {
        background: #111827 !important;
        color: #00FFCC !important;
        border: 2px solid rgba(0, 255, 204, 0.3) !important;
        border-radius: 50% !important;
        width: 68px !important;
        height: 68px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 24px !important;
        font-weight: 800 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 12px rgba(0, 255, 204, 0.05) !important;
    }
    
    .stButton>button:hover {
        background: #00FFCC !important;
        color: #070a13 !important;
        transform: scale(1.12);
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.6) !important;
        border-color: #00FFCC !important;
    }
    
    /* Clean Full-Width Setup Buttons */
    .level-btn>div>button {
        border-radius: 12px !important;
        width: 100% !important;
        height: auto !important;
        padding: 16px !important;
        font-size: 15px !important;
        background: #111827 !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
    }

    .level-btn>div>button:hover {
        background: #FFFFFF !important;
        color: #070a13 !important;
        border-color: #FFFFFF !important;
        box-shadow: 0 0 15px rgba(255,255,255,0.3) !important;
        transform: translateY(-2px);
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
    st.session_state.ticker_status = "MATCH LOG INITIALIZED • AWAITING SELECTION"

# --- SCREEN 1: PRE-MATCH HUB ---
if not st.session_state.game_started:
    st.markdown("<h1 class='main-logo'>AKT.AYUSH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-sub'>Cyber Arena Challenge</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='stadium-pitch'>", unsafe_allow_html=True)
    player_name = st.text_input("CODENAME:", value="Ayush")
    st.session_state.player_name = player_name
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("### SELECT ARENA DIFFICULTY")
    
    st.markdown("<div class='level-btn'>", unsafe_allow_html=True)
    if st.button("🟢 EASY ARENA (Build High Score)"):
        st.session_state.target_out_score = random.randint(110, 160)
        st.session_state.level = "Easy"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🟡 MODERATE ARENA (Balanced Turf)"):
        st.session_state.target_out_score = random.randint(35, 60)
        st.session_state.level = "Moderate"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🔴 TOUGH ARENA (Instant Match Defeat)"):
        st.session_state.target_out_score = random.randint(0, 3)
        st.session_state.level = "Tough"
        st.session_state.game_started = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: THE ENDGAME WRAP-UP ---
elif st.session_state.game_over:
    st.markdown("<h1 class='main-logo'>MATCH OVER</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-sub'>Final Grid Performance</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='stadium-pitch'>
            <h2 style='color:#FF3366; font-family:Orbitron; font-weight:800; letter-spacing:1px;'>🤖 MATRIX AI WINS</h2>
            <p style='color:#657585; font-size:14px; margin-bottom:20px;'>The system algorithm stays completely undefeated.</p>
            <div style='display:flex; justify-content:space-around; align-items:center;'>
                <div><span style='color:#657585; font-size:12px;'>{st.session_state.player_name.upper()}</span><h1 style='font-family:Orbitron; color:#00FFCC; margin:5px 0 0 0;'>{st.session_state.player_score}</h1></div>
                <div style='font-size:24px; color:#3399FF;'>VS</div>
                <div><span style='color:#657585; font-size:12px;'>MATRIX AI</span><h1 style='font-family:Orbitron; color:#FF3366; margin:5px 0 0 0;'>{st.session_state.ai_score}</h1></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🏟️ BOOT NEW MATCH MATRIX"):
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.player_score = 0
        st.session_state.ai_score = 0
        st.session_state.is_player_batting = True
        st.session_state.ticker_status = "MATCH LOG INITIALIZED • AWAITING SELECTION"
        st.rerun()

# --- SCREEN 3: ACTIVE GAME STADIUM ---
else:
    st.markdown("<h1 class='main-logo'>CYBER ARENA</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='stadium-sub'>🏟️ ARENA CONFIGURATION: {st.session_state.level.upper()}</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='stadium-pitch'>", unsafe_allow_html=True)
    
    # Modern Holographic Split Scoreboard
    col_p, col_ai = st.columns(2)
    with col_p:
        color = "#00FFCC" if st.session_state.is_player_batting else "#FFFFFF"
        status_text = "• BATTING •" if st.session_state.is_player_batting else "BOWLING"
        st.markdown(f"""
            <div class='hologram-board'>
                <small style='color:#00FFCC; font-weight:700; letter-spacing:1px;'>{st.session_state.player_name.upper()}</small>
                <div class='score-digits' style='color:{color};'>{st.session_state.player_score}</div>
                <span style='font-size:11px; color:#657585; font-weight:700; letter-spacing:1px;'>{status_text}</span>
            </div>
        """, unsafe_allow_html=True)
    with col_ai:
        color = "#FFFFFF" if st.session_state.is_player_batting else "#FF3366"
        status_text = "BOWLING" if st.session_state.is_player_batting else "• BATTING •"
        st.markdown(f"""
            <div class='hologram-board'>
                <small style='color:#FF3366; font-weight:700; letter-spacing:1px;'>MATRIX AI</small>
                <div class='score-digits' style='color:{color};'>{st.session_state.ai_score}</div>
                <span style='font-size:11px; color:#657585; font-weight:700; letter-spacing:1px;'>{status_text}</span>
            </div>
        """, unsafe_allow_html=True)
        
    # Beautiful Integrated Stream Commentary Panel
    st.markdown(f"""
        <div class='commentary-box'>
            <span style='font-family:monospace; font-size:14px; color:#E1E4E8; letter-spacing:0.5px;'>🎙️ {st.session_state.ticker_status}</span>
        </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='text-align:center; font-size:12px; font-weight:700; color:#657585; letter-spacing:2px; margin-top:5px;'>TAP A SHOT INPUT KEY</p>", unsafe_allow_html=True)
    
    # Elegant, Spaced Touch Selection Column Docks
    grid = st.columns(6)
    player_choice = None
    
    for idx, col in enumerate(grid):
        with col:
            if st.button(str(idx + 1), key=f"shot_{idx}"):
                player_choice = idx + 1
                
    if player_choice:
        if st.session_state.is_player_batting:
            # Rigged Script Defenses
            if st.session_state.player_score >= st.session_state.target_out_score:
                ai_choice = player_choice
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            if player_choice == ai_choice:
                st.session_state.is_player_batting = False
                st.session_state.ticker_status = f"💥 CRITICAL HIT! AI matched your delivery of {player_choice}! Innings turned over."
                st.rerun()
            else:
                st.session_state.player_score += player_choice
                st.session_state.ticker_status = f"🏏 SHOT SECURED! You score +{player_choice} runs. (AI threw {ai_choice})"
                st.rerun()
        else:
            # Rigged Script Run Chase
            target_needed = (st.session_state.player_score + 1) - st.session_state.ai_score
            if target_needed <= 6 and target_needed != player_choice:
                ai_choice = target_needed
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            st.session_state.ai_score += ai_choice
            st.session_state.ticker_status = f"🤖 AI calculation success. Played a smooth {ai_choice} against your {player_choice} ball."
            
            if st.session_state.ai_score > st.session_state.player_score:
                st.session_state.game_over = True
            st.rerun()
