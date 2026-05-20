import streamlit as st
import random

# Core Configurations
st.set_page_config(
    page_title="AKT.Ayush: Cyber Arena",
    page_icon="🏟️",
    layout="centered"
)

# Premium Masterpiece UI Styling Sheet
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;900&family=Rajdhani:wght@600;700&display=swap');
    
    /* Deep Stadium Night Canvas */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #0c192e 0%, #050a14 100%);
        color: #FFFFFF;
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* Background Particle Animation Elements */
    .stadium-lights {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        background-image: 
            radial-gradient(circle at 10% 10%, rgba(0, 255, 204, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 90% 10%, rgba(255, 51, 102, 0.08) 0%, transparent 40%);
        z-index: 0;
    }

    /* Main Virtual Stadium Pitch Container */
    .stadium-pitch {
        background: linear-gradient(180deg, rgba(16, 28, 48, 0.6) 0%, rgba(10, 18, 32, 0.8) 100%);
        border: 2px solid rgba(0, 255, 204, 0.3);
        border-radius: 24px;
        padding: 25px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 0 20px rgba(0, 255, 204, 0.1);
        backdrop-filter: blur(12px);
        margin-bottom: 20px;
        text-align: center;
    }
    
    .pitch-batting { border-color: rgba(0, 255, 204, 0.6); box-shadow: 0 0 25px rgba(0, 255, 204, 0.2); }
    .pitch-bowling { border-color: rgba(255, 51, 102, 0.6); box-shadow: 0 0 25px rgba(255, 51, 102, 0.2); }

    /* Elegant Typography */
    .main-logo {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 38px;
        background: linear-gradient(135deg, #00FFCC 0%, #3399FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        letter-spacing: 2px;
    }
    
    .stadium-sub {
        text-align: center;
        text-transform: uppercase;
        font-family: 'Orbitron', sans-serif;
        color: #8B949E;
        font-size: 11px;
        letter-spacing: 5px;
        margin-bottom: 30px;
    }

    /* Glassmorphism Dynamic Score Displays */
    .hologram-board {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 15px;
        text-align: center;
    }
    
    .score-digits {
        font-family: 'Orbitron', monospace;
        font-size: 42px;
        font-weight: 700;
        line-height: 1;
        margin: 8px 0;
    }

    /* Premium Tactile Digital Gesture Controls */
    .stButton>button {
        background: rgba(22, 27, 34, 0.5) !important;
        color: #00FFCC !important;
        border: 2px solid rgba(0, 255, 204, 0.4) !important;
        border-radius: 50% !important;
        width: 65px !important;
        height: 65px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 22px !important;
        font-weight: bold !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
    }
    
    .stButton>button:hover {
        background: #00FFCC !important;
        color: #050a14 !important;
        transform: scale(1.15);
        box-shadow: 0 0 20px #00FFCC !important;
        border-color: #00FFCC !important;
    }
    
    /* Level Selection Master Blocks */
    .level-btn>div>button {
        border-radius: 14px !important;
        width: 100% !important;
        height: auto !important;
        padding: 15px !important;
        font-size: 16px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }
    </style>
    
    <!-- Injected Animated Stadium Backdrop -->
    <div class="stadium-lights"></div>
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
    st.session_state.ticker_status = "STADIUM ACTIVE • READY FOR KICKOFF"

# --- SCREEN 1: PRE-MATCH HUB ---
if not st.session_state.game_started:
    st.markdown("<h1 class='main-logo'>AKT.Ayush</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-sub'>Grand Virtual Arena</p>", unsafe_allow_html=True)
    
    # Beautiful Form container
    st.markdown("<div class='stadium-pitch'>", unsafe_allow_html=True)
    player_name = st.text_input("CODENAME:", value="Ayush")
    st.session_state.player_name = player_name
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("### 🏟️ CHOOSE YOUR ARENA GRANDSTAND")
    
    st.markdown("<div class='level-btn'>", unsafe_allow_html=True)
    if st.button("🟢 CLUB STAND (Easy Difficulty • Heavy Outfield)"):
        st.session_state.target_out_score = random.randint(110, 160)
        st.session_state.level = "Easy"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🟡 PAVILION END (Moderate Difficulty • Standard Turf)"):
        st.session_state.target_out_score = random.randint(35, 60)
        st.session_state.level = "Moderate"
        st.session_state.game_started = True
        st.rerun()
    if st.button("🔴 GRAND STAND (Tough Difficulty • Precision Grid)"):
        st.session_state.target_out_score = random.randint(0, 3)
        st.session_state.level = "Tough"
        st.session_state.game_started = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCREEN 2: THE ENDGAME WRAP-UP ---
elif st.session_state.game_over:
    st.markdown("<h1 class='main-logo'>MATCH CONCLUDED</h1>", unsafe_allow_html=True)
    st.markdown("<p class='stadium-sub'>Final Arena Statistics</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='stadium-pitch' style='border-color: #FF3366; box-shadow: 0 0 30px rgba(255,51,102,0.3);'>
            <h2 style='color:#FF3366; font-family:Orbitron;'>🤖 MATRIX AI WINS</h2>
            <p style='color:#8B949E;'>The algorithm stays undefeated in the {st.session_state.level} Arena.</p>
            <hr style='border-color:rgba(255,255,255,0.1);'>
            <div style='display:flex; justify-content:space-around; margin-top:15px;'>
                <div><h5>{st.session_state.player_name.upper()}</h5><h2 style='font-family:Orbitron; color:#00FFCC;'>{st.session_state.player_score}</h2></div>
                <div><h5>MATRIX AI</h5><h2 style='font-family:Orbitron; color:#FF3366;'>{st.session_state.ai_score}</h2></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🏟️ RESET ARENA MATRIX"):
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.player_score = 0
        st.session_state.ai_score = 0
        st.session_state.is_player_batting = True
        st.session_state.ticker_status = "STADIUM ACTIVE • READY FOR KICKOFF"
        st.rerun()

# --- SCREEN 3: ACTIVE GAME STADIUM ---
else:
    st.markdown("<h1 class='main-logo'>CYBER ARENA</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='stadium-sub'>🏟️ STADIUM ENCLOSURE: {st.session_state.level.upper()}</p>", unsafe_allow_html=True)
    
    # Active Dynamic Stadium Card wrapper
    pitch_class = "pitch-batting" if st.session_state.is_player_batting else "pitch-bowling"
    st.markdown(f"<div class='stadium-pitch {pitch_class}'>", unsafe_allow_html=True)
    
    # Holographic Scoreboard Layout
    col_p, col_ai = st.columns(2)
    with col_p:
        st.markdown(f"""
            <div class='hologram-board'>
                <small style='color:#00FFCC; font-weight:700; letter-spacing:1px;'>{st.session_state.player_name.upper()}</small>
                <div class='score-digits' style='color:#FFFFFF;'>{st.session_state.player_score}</div>
                <span style='font-size:12px; color:#8B949E;'>{'• CURRENT BATTER •' if st.session_state.is_player_batting else 'FIELDING'}</span>
            </div>
        """, unsafe_allow_html=True)
    with col_ai:
        st.markdown(f"""
            <div class='hologram-board'>
                <small style='color:#FF3366; font-weight:700; letter-spacing:1px;'>MATRIX AI</small>
                <div class='score-digits' style='color:#FFFFFF;'>{st.session_state.ai_score}</div>
                <span style='font-size:12px; color:#8B949E;'>{'FIELDING' if st.session_state.is_player_batting else '• CURRENT BATTER •'}</span>
            </div>
        """, unsafe_allow_html=True)
        
    # Live Action Stadium Commentary Bar
    st.markdown(f"""
        <div style='margin-top:20px; padding:12px; background:rgba(0,0,0,0.3); border-radius:10px; border-left:4px solid #3399FF;'>
            <span style='font-family:monospace; font-size:14px; color:#E1E4E8;'>🎙️ {st.session_state.ticker_status}</span>
        </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='text-align:center; font-weight:700; color:#8B949E; margin-top:10px;'>TAP RUN INPUT DELIVERY</p>", unsafe_allow_html=True)
    
    # Beautifully-spaced Circular Shot Grid
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
                st.session_state.ticker_status = f"💥 OUT STRIKE! AI anticipated the delivery and matches your {player_choice}! Turning over innings."
                st.rerun()
            else:
                st.session_state.player_score += player_choice
                st.session_state.ticker_status = f"🏏 BOUNDARY SPLIT! You timed a {player_choice} (AI bowled {ai_choice}). Score ticking up!"
                st.rerun()
        else:
            # Rigged Script Run Chase
            target_needed = (st.session_state.player_score + 1) - st.session_state.ai_score
            if target_needed <= 6 and target_needed != player_choice:
                ai_choice = target_needed
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            st.session_state.ai_score += ai_choice
            st.session_state.ticker_status = f"🤖 AI drives a clean {ai_choice} past your cover delivery of {player_choice}."
            
            if st.session_state.ai_score > st.session_state.player_score:
                st.session_state.game_over = True
            st.rerun()
