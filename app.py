import streamlit as st
import random

# Core Configurations
st.set_page_config(
    page_title="HandCricket.io",
    page_icon="🏏",
    layout="centered"
)

# HandCricket.io Spaced Light Futuristic Stylesheet
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Syne:wght@700;800&display=swap');
    
    /* Clean Light Futuristic Background Canvas */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4ecf2 100%);
        color: #2D3748;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* HandCricket.io Signature Branding */
    .game-title {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 40px;
        background: linear-gradient(135deg, #00b5d8 0%, #3182ce 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    
    .game-subtitle {
        text-align: center;
        text-transform: uppercase;
        font-family: 'Space Grotesk', sans-serif;
        color: #718096;
        font-size: 11px;
        key-spacing: 3px;
        font-weight: 700;
        margin-bottom: 25px;
    }

    /* Main Match Workspace Card */
    .main-arena-card {
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 24px;
        padding: 20px;
        box-shadow: 0 15px 35px rgba(160, 174, 192, 0.15);
        backdrop-filter: blur(12px);
    }

    /* Scoreboard Box Layouts */
    .score-panel {
        background: #ffffff;
        border-radius: 16px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        border: 1px solid rgba(255,255,255,0.8);
    }
    
    .score-num {
        font-family: 'Syne', sans-serif;
        font-size: 46px;
        font-weight: 800;
        color: #1A202C;
        line-height: 1;
        margin: 5px 0;
    }

    /* Dynamic Battle Circle Nodes (No Collision) */
    .battle-node {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Syne', sans-serif;
        font-size: 32px;
        font-weight: 800;
        margin: 10px auto;
        box-shadow: 0 8px 20px rgba(49, 130, 206, 0.15);
    }
    
    .node-player { border: 3px solid #00b5d8; color: #00b5d8; }
    .node-ai { border: 3px solid #e53e3e; color: #e53e3e; }

    /* Streamlined Commentary Strip */
    .ticker-banner {
        background: #1A202C;
        color: #ffffff;
        border-radius: 12px;
        padding: 12px 15px;
        font-size: 13px;
        font-weight: 500;
        margin: 15px 0;
        text-align: center;
    }

    /* Isolated Button Tray: Generous Spacing for Touch Targets */
    .button-tray {
        background: rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.6);
        margin-top: 15px;
    }

    /* Custom Input Tokens */
    .stButton>button {
        background: #ffffff !important;
        color: #3182ce !important;
        border: 1px solid rgba(49, 130, 206, 0.2) !important;
        border-radius: 16px !important;
        width: 100% !important;
        height: 58px !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.02) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton>button:hover {
        background: #3182ce !important;
        color: #ffffff !important;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(49, 130, 206, 0.3) !important;
    }

    /* Lobby Interface Action Formatting */
    .lobby-btn>div>button {
        border-radius: 12px !important;
        width: 100% !important;
        height: auto !important;
        padding: 14px !important;
        font-size: 15px !important;
        font-family: 'Space Grotesk', sans-serif !important;
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
if 'last_player_move' not in st.session_state:
    st.session_state.last_player_move = "-"
if 'last_ai_move' not in st.session_state:
    st.session_state.last_ai_move = "-"
if 'ticker_status' not in st.session_state:
    st.session_state.ticker_status = "MATCH READY • CHOOSE YOUR MOVE"

# --- SCREEN 1: THE LOBBY ---
if not st.session_state.game_started:
    st.markdown("<h1 class='game-title'>handcricket.io</h1>", unsafe_allow_html=True)
    st.markdown("<p class='game-subtitle'>Multiplayer Casual Engine</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='main-arena-card'>", unsafe_allow_html=True)
    player_name = st.text_input("PLAYER TAG:", value="Ayush")
    st.session_state.player_name = player_name
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("### SELECT GAME MODALITY")
    st.markdown("<div class='lobby-btn'>", unsafe_allow_html=True)
    if st.button("🟢 CASUAL MATCH (Easy Settings)"):
        st.session_state.target_out_score = random.randint(110, 160)
        st.session_state.level = "Casual"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🟡 RANKED DUEL (Moderate Settings)"):
        st.session_state.target_out_score = random.randint(35, 60)
        st.session_state.level = "Ranked"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🔴 TOURNAMENT FINALS (Extreme Difficulty)"):
        st.session_state.target_out_score = random.randint(0, 3)
        st.session_state.level = "Tournament"
        st.session_state.game_started = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: GAME OVER STATISTICS ---
elif st.session_state.game_over:
    st.markdown("<h1 class='game-title'>MATCH OVER</h1>", unsafe_allow_html=True)
    st.markdown("<p class='game-subtitle'>Server Session Terminated</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='main-arena-card' style='text-align:center;'>
            <h2 style='color:#e53e3e; font-family:Syne; font-weight:800; margin-bottom:5px;'>🤖 MATRIX AI WINS</h2>
            <p style='color:#718096; font-size:14px; margin-bottom:20px;'>Better luck next inning, player.</p>
            <hr style='border-color:rgba(0,0,0,0.05);'>
            <div style='display:flex; justify-content:space-around; margin-top:20px;'>
                <div><span style='color:#718096; font-size:12px; font-weight:bold;'>{st.session_state.player_name.upper()}</span><h1 style='font-family:Syne; color:#00b5d8; margin:0;'>{st.session_state.player_score}</h1></div>
                <div><span style='color:#718096; font-size:12px; font-weight:bold;'>MATRIX AI</span><h1 style='font-family:Syne; color:#e53e3e; margin:0;'>{st.session_state.ai_score}</h1></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 BACK TO SERVER LOBBY"):
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.player_score = 0
        st.session_state.ai_score = 0
        st.session_state.last_player_move = "-"
        st.session_state.last_ai_move = "-"
        st.session_state.is_player_batting = True
        st.session_state.ticker_status = "MATCH READY • CHOOSE YOUR MOVE"
        st.rerun()

# --- SCREEN 3: HANDCRICKET.IO LIVING ARENA ---
else:
    st.markdown("<h1 class='game-title'>handcricket.io</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='game-subtitle'>🏟️ LEAGUE ROOM: {st.session_state.level.upper()}</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='main-arena-card'>", unsafe_allow_html=True)
    
    # 1. Spaced Out Live Score Cards
    col_p, col_ai = st.columns(2)
    with col_p:
        status = "• BATTING •" if st.session_state.is_player_batting else "BOWLING"
        st.markdown(f"""
            <div class='score-panel' style='border-top: 4px solid #00b5d8;'>
                <small style='color:#00b5d8; font-weight:700;'>{st.session_state.player_name.upper()}</small>
                <div class='score-num'>{st.session_state.player_score}</div>
                <span style='font-size:11px; color:#718096; font-weight:700;'>{status}</span>
            </div>
        """, unsafe_allow_html=True)
    with col_ai:
        status = "BOWLING" if st.session_state.is_player_batting else "• BATTING •"
        st.markdown(f"""
            <div class='score-panel' style='border-top: 4px solid #e53e3e;'>
                <small style='color:#e53e3e; font-weight:700;'>MATRIX AI</small>
                <div class='score-num'>{st.session_state.ai_score}</div>
                <span style='font-size:11px; color:#718096; font-weight:700;'>{status}</span>
            </div>
        """, unsafe_allow_html=True)
        
    # 2. Side-By-Side Visual Delivery Nodes (Identical to handcricket.io gameplay)
    st.markdown("<p style='text-align:center; font-size:11px; font-weight:700; color:#A0AEC0; margin-top:20px; margin-bottom:5px;'>LAST DELIVERY SHOWDOWN</p>", unsafe_allow_html=True)
    col_move1, col_move2 = st.columns(2)
    with col_move1:
        st.markdown(f"<div class='battle-node node-player'>{st.session_state.last_player_move}</div>", unsafe_allow_html=True)
    with col_move2:
        st.markdown(f"<div class='battle-node node-ai'>{st.session_state.last_ai_move}</div>", unsafe_allow_html=True)
        
    # 3. Live Match Action Bar
    st.markdown(f"""
        <div class='ticker-banner'>
            {st.session_state.ticker_status.upper()}
        </div>
        </div>
    """, unsafe_allow_html=True)
    
    # 4. Spaced Out Touch Grid - 3 Columns Over 2 Rows (Zero Thumb Collisions)
    st.markdown("<div class='button-tray'>", unsafe_allow_html=True)
    
    row1_1, row1_2, row1_3 = st.columns(3)
    row2_1, row2_2, row2_3 = st.columns(3)
    
    player_choice = None
    
    with row1_1:
        if st.button("1", key="num_1"): player_choice = 1
    with row1_2:
        if st.button("2", key="num_2"): player_choice = 2
    with row1_3:
        if st.button("3", key="num_3"): player_choice = 3
        
    with row2_1:
        if st.button("4", key="num_4"): player_choice = 4
    with row2_2:
        if st.button("5", key="num_5"): player_choice = 5
    with row2_3:
        if st.button("6", key="num_6"): player_choice = 6
        
    st.markdown("</div>", unsafe_allow_html=True)
                
    if player_choice:
        st.session_state.last_player_move = player_choice
        
        if st.session_state.is_player_batting:
            if st.session_state.player_score >= st.session_state.target_out_score:
                ai_choice = player_choice
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
            
            st.session_state.last_ai_move = ai_choice
                
            if player_choice == ai_choice:
                st.session_state.is_player_batting = False
                st.session_state.ticker_status = f"💥 OUT! Both players threw {player_choice}. Innings switched!"
                st.rerun()
            else:
                st.session_state.player_score += player_choice
                st.session_state.ticker_status = f"🏏 Clear hit! You score +{player_choice} runs."
                st.rerun()
        else:
            target_needed = (st.session_state.player_score + 1) - st.session_state.ai_score
            if target_needed <= 6 and target_needed != player_choice:
                ai_choice = target_needed
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            st.session_state.last_ai_move = ai_choice
            st.session_state.ai_score += ai_choice
            st.session_state.ticker_status = f"🤖 AI drives a clean shot scoring +{ai_choice} runs."
            
            if st.session_state.ai_score > st.session_state.player_score:
                st.session_state.game_over = True
            st.rerun()
