import tkinter as tk
from tkinter import messagebox
import random
import time

class CyberCricketGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AKT.Ayush: Cyber Cricket (The Unbeatable Matrix)")
        self.root.geometry("700x550")
        self.root.configure(bg="#0D1117") # Deep Space Dark
        self.root.resizable(False, False)
        
        # Game State Variables
        self.player_name = "Player"
        self.level = "Easy"
        self.max_num = 6
        self.player_score = 0
        self.ai_score = 0
        self.is_player_batting = True
        self.target_out_score = 0
        
        self.create_welcome_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_welcome_screen(self):
        self.clear_screen()
        
        # Title Banner
        title_frame = tk.Frame(self.root, bg="#0D1117")
        title_frame.pack(pady=30)
        
        title_label = tk.Label(title_frame, text="AKT.Ayush", font=("Courier New", 32, "bold"), fg="#00FFCC", bg="#0D1117")
        title_label.pack()
        subtitle_label = tk.Label(title_frame, text="CYBER CRICKET AI CHALLENGE", font=("Century Gothic", 14, "bold"), fg="#8B949E", bg="#0D1117")
        subtitle_label.pack(pady=5)
        
        # Name Input
        name_frame = tk.Frame(self.root, bg="#0D1117")
        name_frame.pack(pady=15)
        tk.Label(name_frame, text="ENTER YOUR CODENAME:", font=("Century Gothic", 11), fg="#FFFFFF", bg="#0D1117").pack(side=tk.LEFT, padx=10)
        self.name_entry = tk.Entry(name_frame, font=("Century Gothic", 12), width=18, bg="#161B22", fg="#FFFFFF", insertbackground="white", bd=1, relief="solid")
        self.name_entry.insert(0, "Ayush")
        self.name_entry.pack(side=tk.LEFT)
        
        # Level Select Header
        tk.Label(self.root, text="CHOOSE DIFFICULTY LEVEL", font=("Century Gothic", 12, "bold"), fg="#FFFFFF", bg="#0D1117").pack(pady=15)
        
        # Level Buttons
        btn_style = {"font": ("Century Gothic", 11, "bold"), "width": 24, "height": 2, "bd": 0, "cursor": "hand2"}
        
        easy_btn = tk.Button(self.root, text="🟢 EASY MODE\n(Build your High Score!)", bg="#1f8555", fg="#FFFFFF", activebackground="#2ea86d", activeforeground="#FFFFFF", **btn_style, command=lambda: self.start_game("Easy"))
        easy_btn.pack(pady=8)
        
        mod_btn = tk.Button(self.root, text="🟡 MODERATE MODE\n(Test your strategy skills)", bg="#d47a13", fg="#FFFFFF", activebackground="#f59322", activeforeground="#FFFFFF", **btn_style, command=lambda: self.start_game("Moderate"))
        mod_btn.pack(pady=8)
        
        tough_btn = tk.Button(self.root, text="🔴 TOUGH MODE\n(Instant Glitch Out)", bg="#b82525", fg="#FFFFFF", activebackground="#db3535", activeforeground="#FFFFFF", **btn_style, command=lambda: self.start_game("Tough"))
        tough_btn.pack(pady=8)
        
        # Footer
        tk.Label(self.root, text="The system always algorithms a path to victory.", font=("Courier New", 9, "italic"), fg="#58A6FF", bg="#0D1117").pack(side=tk.BOTTOM, pady=15)

    def start_game(self, level):
        self.player_name = self.name_entry.get().strip() or "Challenger"
        self.level = level
        self.player_score = 0
        self.ai_score = 0
        self.is_player_batting = True
        
        # Unbeatable script parameter assignments
        if level == "Easy":
            self.target_out_score = random.randint(110, 160)
        elif level == "Moderate":
            self.target_out_score = random.randint(35, 60)
        else:
            self.target_out_score = random.randint(0, 3)
            
        self.create_match_screen()

    def create_match_screen(self):
        self.clear_screen()
        
        # Status Matrix Header
        status_frame = tk.Frame(self.root, bg="#161B22", height=70, bd=1, relief="solid")
        status_frame.pack(fill=tk.X, padx=20, pady=15)
        status_frame.pack_propagate(False)
        
        self.innings_label = tk.Label(status_frame, text=f"🏏 {self.player_name.upper()} IS BATTING", font=("Century Gothic", 12, "bold"), fg="#00FFCC", bg="#161B22")
        self.innings_label.pack(side=tk.LEFT, padx=20)
        
        self.mode_tag = tk.Label(status_frame, text=f"MODE: {self.level.upper()}", font=("Courier New", 11, "bold"), fg="#FFC72C", bg="#161B22")
        self.mode_tag.pack(side=tk.RIGHT, padx=20)

        # Main Arena Scoreboards
        arena_frame = tk.Frame(self.root, bg="#0D1117")
        arena_frame.pack(pady=10, fill=tk.BOTH)
        
        # Left Panel: Player
        self.p_card = tk.Frame(arena_frame, bg="#1F242C", width=220, height=140, bd=2, relief="groove")
        self.p_card.pack(side=tk.LEFT, padx=40, expand=True)
        self.p_card.pack_propagate(False)
        tk.Label(self.p_card, text=self.player_name.upper(), font=("Century Gothic", 11, "bold"), fg="#FFFFFF", bg="#1F242C").pack(pady=10)
        self.p_score_lbl = tk.Label(self.p_card, text="0", font=("Courier New", 36, "bold"), fg="#00FFCC", bg="#1F242C")
        self.p_score_lbl.pack()
        self.p_status_lbl = tk.Label(self.p_card, text="Current Batter", font=("Century Gothic", 9, "italic"), fg="#8B949E", bg="#1F242C")
        self.p_status_lbl.pack(pady=5)
        
        # Right Panel: System AI
        self.ai_card = tk.Frame(arena_frame, bg="#1F242C", width=220, height=140, bd=2, relief="groove")
        self.ai_card.pack(side=tk.RIGHT, padx=40, expand=True)
        self.ai_card.pack_propagate(False)
        tk.Label(self.ai_card, text="MATRIX AI", font=("Century Gothic", 11, "bold"), fg="#FFFFFF", bg="#1F242C").pack(pady=10)
        self.ai_score_lbl = tk.Label(self.ai_card, text="0", font=("Courier New", 36, "bold"), fg="#FF3366", bg="#1F242C")
        self.ai_score_lbl.pack()
        self.ai_status_lbl = tk.Label(self.ai_card, text="Waiting...", font=("Century Gothic", 9, "italic"), fg="#8B949E", bg="#1F242C")
        self.ai_status_lbl.pack(pady=5)
        
        # Live Visual Gameplay Visualizer
        self.visual_ticker = tk.Label(self.root, text="CHOOSE YOUR DIGITAL DIGIT TO THROW", font=("Century Gothic", 13, "bold"), fg="#FFFFFF", bg="#0D1117")
        self.visual_ticker.pack(pady=25)
        
        # Dynamic Target / Match log bar
        self.log_lbl = tk.Label(self.root, text="Game Commencing... Match Matrix stabilized.", font=("Courier New", 10), fg="#8B949E", bg="#0D1117")
        self.log_lbl.pack(pady=5)

        # Digit Interactive Button Grid
        btn_grid = tk.Frame(self.root, bg="#0D1117")
        btn_grid.pack(side=tk.BOTTOM, pady=30)
        
        for i in range(1, 7):
            b = tk.Button(btn_grid, text=str(i), font=("Courier New", 16, "bold"), width=4, height=1, bg="#161B22", fg="#00FFCC", 
                          activebackground="#00FFCC", activeforeground="#161B22", bd=1, relief="solid", cursor="hand2",
                          command=lambda num=i: self.play_turn(num))
            b.pack(side=tk.LEFT, padx=8)

    def play_turn(self, player_move):
        if self.is_player_batting:
            # Rigged Defense Logic: Track run cap threshold
            if self.player_score >= self.target_out_score:
                ai_move = player_move # Script matches choice to trigger OUT
            else:
                ai_move = random.choice([x for x in range(1, 7) if x != player_move])
                
            self.log_lbl.config(text=f"⚡ You chose {player_move} | Matrix AI calculated {ai_move}")
            
            if player_move == ai_move:
                self.visual_ticker.config(text="💥 OUT!!! THE MATRIX READ YOUR MIND!", fg="#FF3366")
                self.p_status_lbl.config(text="💥 ALL OUT", fg="#FF3366")
                self.root.update()
                time.sleep(2)
                
                # Switch To AI Batting
                self.is_player_batting = False
                self.innings_label.config(text="🤖 MATRIX AI IS BATTING", fg="#FF3366")
                self.p_status_lbl.config(text=f"Final Score: {self.player_score}", fg="#00FFCC")
                self.ai_status_lbl.config(text="Chasing Target...", fg="#FF3366")
                self.visual_ticker.config(text=f"TARGET: OVERTAKE {self.player_score} RUNS", fg="#FFFFFF")
                self.log_lbl.config(text="AI takes the crease. Defeat calculation initialized.")
            else:
                self.player_score += player_move
                self.p_score_lbl.config(text=str(self.player_score))
                self.visual_ticker.config(text=f"🟢 WRONG GUESS BY AI! +{player_move} RUNS", fg="#00FFCC")
                
        else:
            # Rigged Chase Logic: AI looks inside player selection and guarantees safety or win
            target_needed = (self.player_score + 1) - self.ai_score
            
            if target_needed <= 6:
                if target_needed != player_move:
                    ai_move = target_needed
                else:
                    ai_move = random.choice([x for x in range(1, 7) if x != player_move])
            else:
                ai_move = random.choice([x for x in range(1, 7) if x != player_move])
                
            self.ai_score += ai_move
            self.ai_score_lbl.config(text=str(self.ai_score))
            self.log_lbl.config(text=f"⚡ You bowled {player_move} | Matrix AI played {ai_move}")
            self.visual_ticker.config(text=f"🤖 AI advances smoothly! (+{ai_move} Runs)", fg="#FF5555")
            
            if self.ai_score > self.player_score:
                self.root.update()
                time.sleep(1.5)
                self.trigger_endgame()

    def trigger_endgame(self):
        self.clear_screen()
        
        # Cyber Victory Screen
        vic_frame = tk.Frame(self.root, bg="#0D1117")
        vic_frame.pack(expand=True)
        
        tk.Label(vic_frame, text="🤖 AI WINS! UNBEATABLE SYSTEM!", font=("Century Gothic", 22, "bold"), fg="#FF3366", bg="#0D1117").pack(pady=10)
        tk.Label(vic_frame, text="AKT.Ayush Cyber Core Grid intact.", font=("Courier New", 11, "italic"), fg="#8B949E", bg="#0D1117").pack(pady=5)
        
        # Score recap box
        box = tk.Frame(vic_frame, bg="#161B22", bd=1, relief="solid", width=340, height=120)
        box.pack(pady=25)
        box.pack_propagate(False)
        
        tk.Label(box, text=f"{self.player_name.upper()}: {self.player_score} runs ({self.level})", font=("Courier New", 12), fg="#00FFCC", bg="#161B22").pack(pady=15)
        tk.Label(box, text=f"MATIX SYSTEM AI: {self.ai_score} runs", font=("Courier New", 12), fg="#FF3366", bg="#161B22").pack()
        
        # Restart
        restart_btn = tk.Button(vic_frame, text="⚡ RETRY SYSTEM MATRIX", font=("Century Gothic", 12, "bold"), bg="#1F242C", fg="#FFFFFF",
                               bd=1, relief="solid", width=22, height=2, cursor="hand2", command=self.create_welcome_screen)
        restart_btn.pack(pady=10)

if __name__ == "__main__":
    window = tk.Tk()
    game = CyberCricketGame(window)
    window.mainloop()
