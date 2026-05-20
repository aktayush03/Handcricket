import streamlit as st
import random

# Page Configuration for Mobile Responsiveness
st.set_page_config(
    page_title="AKT.Ayush: Cyber Cricket Stadium",
    page_icon="🏟️",
    layout="centered"
)

# Advanced CSS & JS for a Moving, High-Tech Virtual Stadium Feel
st.markdown("""
    <style>
    /* Virtual Stadium Deep Dark Background with Moving Gradient */
    .stApp {
        background: linear-gradient(135deg, #050811 0%, #0d1527 50%, #050811 100%);
        background-size: 400% 400%;
        animation: stadiumLights 15s ease infinite;
        color: #FFFFFF;
        font-family: 'Century Gothic', sans-serif;
    }

    @keyframes stadiumLights {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Cyber Stadium Glowing Headers */
    .stadium-title {
        text-align: center;
        font-family: 'Courier New', monospace;
        font-weight: 900;
        color: #00FFCC;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.6), 0 0 20px rgba(0, 255, 204, 0.3);
        margin-bottom: 0px;
    }
    
    .stadium-subtitle {
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #8B949E;
        font-size: 12px;
        margin-bottom: 25px;
    }

    /* Neon Hologram Scoreboards */
    .scoreboard-card {
        background: rgba(22, 27, 34, 0.7);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    
    .player-card {
        border: 2px solid #00FFCC;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
    }
    
    .ai-card {
        border: 2px solid #FF3366;
        box-shadow: 0 0 15px rgba(255, 51, 102, 0.2);
    }

    /* Interactive Game Ticker */
    .stAlert {
        background: rgba(31, 38, 52, 0.8) !important;
        border: 1px solid #58A6FF !important;
        box-shadow: 0 0 10px rgba(88, 166, 255, 0.2);
        border-radius: 10px;
    }

    /* Styled Cyber Hand Input Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #161B22 0%, #21262D 100%);
        color: #00FFCC !important;
        border: 1px solid #00FFCC !important;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 22px;
        padding: 15px 0px;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        background: #00FFCC !important;
        color: #161B22 !important;
        box-shadow: 0 0 15px #00FFCC;
    }
    
    .stButton>button:active {
        transform: translateY(1px);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State Variables for Persistent App Flow
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
if 'log_msg' not in st.session_state:
    st.session_state.log_msg = "Stadium Matrix Online. Click a digit below to throw your shot!"

# --- STADIUM WELCOME SCREEN ---
if not st.session_state.game_started:
    st.markdown("<h1 class='stadium-title'>⚡ AKT.Ayush</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-subtitle'>VIRTUAL STADIUM CHALLENGE</p>", unsafe_allow_html=True)
    
    player_name = st.text_input("ENTER CODENAME:", value="Ayush")
    st.session_state.player_name = player_name
    
    st.write("### 🏟️ SELECT STADIUM TURF DIFFICULTY")
    
    if st.button("🟢 EASY STADIUM (High Run Multiplier)"):
        st.session_state.target_out_score = random.randint(110, 160)
        st.session_state.level = "Easy"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🟡 MODERATE STADIUM (Balanced Matrix)"):
        st.session_state.target_out_score = random.randint(35, 60)
        st.session_state.level = "Moderate"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🔴 TOUGH STADIUM (Instant Annihilation Grid)"):
        st.session_state.target_out_score = random.randint(0, 3)
        st.session_state.level = "Tough"
        st.session_state.game_started = True
        st.rerun()

# --- STADIUM GAME OVER SCREEN ---
elif st.session_state.game_over:
    st.markdown("<h1 class='stadium-title'>🤖 MATCH OVER</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-subtitle'>AI MAINTAINS ITS UNBEATABLE STREAK</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='scoreboard-card ai-card' style='max-width: 400px; margin: 0 auto 20px auto;'>
            <h3 style='color:#FF3366;'>🏆 SYSTEM AI VICTORIOUS</h3>
            <p style='font-size: 18px;'><b>{st.session_state.player_name}</b>: {st.session_state.player_score} runs</p>
            <p style='font-size: 18px;'><b>Matrix AI</b>: {st.session_state.ai_score} runs</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("⚡ REBOOT STADIUM MATRIX"):
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.player_score = 0
        st.session_state.ai_score = 0
        st.session_state.is_player_batting = True
        st.session_state.log_msg = "Stadium Matrix Online. Click a digit below to throw your shot!"
        st.rerun()

# --- ACTIVE LIVE MATCH ARENA ---
else:
    st.markdown("<h1 class='stadium-title'>🏟️ CYBER STADIUM</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='stadium-subtitle'>MODE: {st.session_state.level.upper()} | {'YOU ARE BATTING' if st.session_state.is_player_batting else 'AI IS BATTING'}</p>", unsafe_allow_html=True)
    
    # Grid Scoreboards
    col_p, col_ai = st.columns(2)
    with col_p:
        st.markdown(f"""
            <div class='scoreboard-card player-card'>
                <span style='color:#00FFCC; font-weight:bold; letter-spacing:1px;'>{st.session_state.player_name.upper()}</span>
                <h1 style='color:#FFFFFF; margin:10px 0px; font-family:monospace;'>{st.session_state.player_score}</h1>
                <small style='color:#8B949E;'>{'BATTING' if st.session_state.is_player_batting else 'BOWLING'}</small>
            </div>
        """, unsafe_allow_html=True)
    with col_ai:
        st.markdown(f"""
            <div class='scoreboard-card ai-card'>
                <span style='color:#FF3366; font-weight:bold; letter-spacing:1px;'>MATRIX AI</span>
                <h1 style='color:#FFFFFF; margin:10px 0px; font-family:monospace;'>{st.session_state.ai_score}</h1>
                <small style='color:#8B949E;'>{'BOWLING' if st.session_state.is_player_batting else 'BATTING'}</small>
            </div>
        """, unsafe_allow_html=True)
        
    st.info(st.session_state.log_msg)
    
    st.write("### Tap a Number to Swing:")
    
    # 6-Column Mobile Layout Touch Targets
    grid = st.columns(6)
    player_choice = None
    
    for idx, col in enumerate(grid):
        if col.button(str(idx + 1), key=f"hand_{idx}"):
            player_choice = idx + 1
            
    if player_choice:
        if st.session_state.is_player_batting:
            # Rigged Defense AI Logic
            if st.session_state.player_score >= st.session_state.target_out_score:
                ai_choice = player_choice
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            if player_choice == ai_choice:
                st.session_state.is_player_batting = False
                st.session_state.log_msg = f"💥 OUT!!! The Stadium flashlights turn red. Computer bowled {ai_choice}. The Matrix read your swing!"
                st.rerun()
            else:
                st.session_state.player_score += player_choice
                st.session_state.log_msg = f"🟢 BOUNDARY! You threw {player_choice}, Computer threw {ai_choice}. Added +{player_choice} runs to your score!"
                st.rerun()
        else:
            # Rigged Chase AI Logic
            target_needed = (st.session_state.player_score + 1) - st.session_state.ai_score
            if target_needed <= 6 and target_needed != player_choice:
                ai_choice = target_needed
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            st.session_state.ai_score += ai_choice
            st.session_state.log_msg = f"🤖 AI easily tracks the delivery! AI played {ai_choice}, You bowled {player_choice}."
            
            if st.session_state.ai_score > st.session_state.player_score:
                st.session_state.game_over = True
            st.rerun()
