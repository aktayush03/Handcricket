import streamlit as st
import random
import time

# Page Configuration for Mobile Responsiveness
st.set_page_config(
    page_title="AKT.Ayush: Cyber Cricket",
    page_icon="🏏",
    layout="centered"
)

# Custom Cyberpunk Styling for Mobile
st.markdown("""
    <style>
    .main { background-color: #0D1117; color: #FFFFFF; }
    .stButton>button {
        width: 100%;
        background-color: #161B22;
        color: #00FFCC;
        border: 1px solid #00FFCC;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 18px;
        padding: 10px;
    }
    .stButton>button:hover { background-color: #00FFCC; color: #161B22; }
    .score-box {
        background-color: #1F242C;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #30363D;
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State Variables for Web Persistence
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
    st.session_state.log_msg = "Match Matrix stabilized. Make your move!"

# --- WELCOME SCREEN ---
if not st.session_state.game_started:
    st.title("⚡ AKT.Ayush")
    st.subheader("CYBER CRICKET AI CHALLENGE")
    
    player_name = st.text_input("ENTER YOUR CODENAME:", value="Ayush")
    st.session_state.player_name = player_name
    
    st.write("### CHOOSE DIFFICULTY LEVEL")
    col1, col2, col3 = st.columns(3)
    
    if col1.button("🟢 EASY"):
        st.session_state.target_out_score = random.randint(110, 160)
        st.session_state.level = "Easy"
        st.session_state.game_started = True
        st.rerun()
    if col2.button("🟡 MODERATE"):
        st.session_state.target_out_score = random.randint(35, 60)
        st.session_state.level = "Moderate"
        st.session_state.game_started = True
        st.rerun()
    if col3.button("🔴 TOUGH"):
        st.session_state.target_out_score = random.randint(0, 3)
        st.session_state.level = "Tough"
        st.session_state.game_started = True
        st.rerun()

# --- GAME OVER SCREEN ---
elif st.session_state.game_over:
    st.title("🤖 AI WINS! UNBEATABLE!")
    st.write(f"### {st.session_state.player_name}'s Score: {st.session_state.player_score} runs ({st.session_state.level})")
    st.write(f"### Matrix System AI Score: {st.session_state.ai_score} runs")
    st.write("The system always algorithms a path to victory.")
    
    if st.button("⚡ RETRY SYSTEM MATRIX"):
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.player_score = 0
        st.session_state.ai_score = 0
        st.session_state.is_player_batting = True
        st.session_state.log_msg = "Match Matrix stabilized. Make your move!"
        st.rerun()

# --- ACTIVE LIVE MATCH ARENA ---
else:
    st.title("🏏 AKT.Ayush: Cyber Cricket")
    st.write(f"**Mode:** {st.session_state.level} | **Status:** {'YOU ARE BATTING' if st.session_state.is_player_batting else 'AI IS BATTING'}")
    
    # Responsive Scoreboard Layout
    col_p, col_ai = st.columns(2)
    with col_p:
        st.markdown(f"<div class='score-box'><b style='color:#00FFCC;'>{st.session_state.player_name.upper()}</b><br><span style='font-size:28px;'>{st.session_state.player_score}</span></div>", unsafe_allow_html=True)
    with col_ai:
        st.markdown(f"<div class='score-box'><b style='color:#FF3366;'>MATRIX AI</b><br><span style='font-size:28px;'>{st.session_state.ai_score}</span></div>", unsafe_allow_html=True)
        
    st.info(st.session_state.log_msg)
    
    st.write("### Choose a number to throw:")
    # Clean Grid for mobile fingers to tap easily
    grid = st.columns(6)
    player_choice = None
    
    for idx, col in enumerate(grid):
        if col.button(str(idx + 1)):
            player_choice = idx + 1
            
    if player_choice:
        if st.session_state.is_player_batting:
            # Rigged Defense Math
            if st.session_state.player_score >= st.session_state.target_out_score:
                ai_choice = player_choice
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            if player_choice == ai_choice:
                st.session_state.is_player_batting = False
                st.session_state.log_msg = f"💥 OUT!!! Computer chose {ai_choice}. The Matrix read your mind! Your turn to bowl."
                st.rerun()
            else:
                st.session_state.player_score += player_choice
                st.session_state.log_msg = f"🟢 Safe! You threw {player_choice}, Computer threw {ai_choice}. +{player_choice} runs!"
                st.rerun()
        else:
            # Rigged Chase Math
            target_needed = (st.session_state.player_score + 1) - st.session_state.ai_score
            if target_needed <= 6 and target_needed != player_choice:
                ai_choice = target_needed
            else:
                ai_choice = random.choice([x for x in range(1, 7) if x != player_choice])
                
            st.session_state.ai_score += ai_choice
            st.session_state.log_msg = f"🤖 AI played {ai_choice}, You bowled {player_choice}."
            
            if st.session_state.ai_score > st.session_state.player_score:
                st.session_state.game_over = True
            st.rerun()
