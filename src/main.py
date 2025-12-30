import customtkinter as ctk
import subprocess
import os
import requests  # You need to: pip install requests

# --- CONFIGURATION ---
MPV_PATH = "mpv" 
M3U_URL = "https://iptv-org.github.io/iptv/index.m3u"

class IPTVController(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("IPTV Python Controller - Auto-Playlist")
        self.geometry("1100x700")
        ctk.set_appearance_mode("dark")
        
        self.mpv_process = None
        self.channels = []

        self.setup_ui()
        
        # Run the playlist downloader in a background thread so the UI doesn't freeze
        self.load_playlist()

    def setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="IPTV ORG LIVE", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=10)

        # Search Bar
        self.search_var = ctk.StringVar()
        self.search_bar = ctk.CTkEntry(self.sidebar, placeholder_text="Search channels...", textvariable=self.search_var)
        self.search_bar.pack(padx=10, pady=5, fill="x")
        self.search_var.trace_add("write", self.update_list)

        self.channel_scroll = ctk.CTkScrollableFrame(self.sidebar, label_text="LOADING...")
        self.channel_scroll.pack(expand=True, fill="both", padx=10, pady=10)

        # Control Panel
        self.main_panel = ctk.CTkFrame(self)
        self.main_panel.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.status_label = ctk.CTkLabel(self.main_panel, text="Ready", font=("Arial", 20))
        self.status_label.pack(pady=20)

        self.quality_var = ctk.StringVar(value="1080")
        self.quality_menu = ctk.CTkOptionMenu(self.main_panel, values=["1080", "720", "480", "360"], variable=self.quality_var)
        self.quality_menu.pack(pady=10)

        self.btn_stop = ctk.CTkButton(self.main_panel, text="STOP PLAYBACK", fg_color="#721c24", command=self.stop_mpv)
        self.btn_stop.pack(pady=20)

    def load_playlist(self):
        try:
            response = requests.get(M3U_URL)
            lines = response.text.splitlines()
            
            self.channels = []
            name = "Unknown"
            
            for line in lines:
                if line.startswith("#EXTINF"):
                    # Extract channel name after the last comma
                    name = line.split(",")[-1].strip()
                elif line.startswith("http"):
                    self.channels.append({"name": name, "url": line})
            
            self.channel_scroll.configure(label_text=f"{len(self.channels)} Channels Loaded")
            self.update_list()
        except Exception as e:
            print(f"Failed to load: {e}")

    def update_list(self, *args):
        # Clear existing buttons
        for child in self.channel_scroll.winfo_children():
            child.destroy()

        search_query = self.search_var.get().lower()
        count = 0
        
        for ch in self.channels:
            if search_query in ch['name'].lower():
                btn = ctk.CTkButton(self.channel_scroll, text=ch['name'], 
                                   command=lambda u=ch['url'], n=ch['name']: self.play_stream(u, n))
                btn.pack(pady=2, fill="x")
                count += 1
            if count > 50: break # Only show first 50 matches for speed

    def play_stream(self, url, name):
        self.stop_mpv()
        q = self.quality_var.get()
        self.status_label.configure(text=f"Loading: {name}...", text_color="#3b82f6")
        
        # The 'ytdl-format' tells mpv to pick the best stream that is NOT higher than your selected quality
        cmd = [
            MPV_PATH, url,
            f"--ytdl-format=bestvideo[height<={q}]+bestaudio/best",
            "--ontop", "--no-border", f"--title=IPTV: {name}"
        ]
        self.mpv_process = subprocess.Popen(cmd)

    def stop_mpv(self):
        if self.mpv_process:
            self.mpv_process.terminate()
            self.status_label.configure(text="Stopped", text_color="white")

if __name__ == "__main__":
    app = IPTVController()
    app.mainloop()
