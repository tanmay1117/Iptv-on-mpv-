# 📺 IPTV Controller Pro (Python + MPV)
[![Build and Release](https://github.com/tanmay1117/Iptv-on-mpv-/actions/workflows/build.yml/badge.svg)](https://github.com/tanmay1117/Iptv-on-mpv-/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance, cross-platform IPTV browser built with **Python** and the **MPV** engine. Access over 30,000+ global channels instantly with hardware acceleration and quality control.

---

## 🚀 Key Features
* **Auto-Playlist:** Dynamically fetches thousands of channels from `iptv-org`.
* **Searchable UI:** Filter through 30k+ channels in milliseconds.
* **Quality Management:** Force streams to 1080p, 720p, or 480p to save bandwidth.
* **Engineered with MPV:** Zero-lag playback using the industry-standard media engine.
* **Standalone Binaries:** No Python installation required for end-users.

---

## 📥 Installation & Usage

### 🪟 Windows Users (Easiest)
1.  **Download:** Go to the [Releases](https://github.com/tanmay1117/Iptv-on-mpv-/releases) section on the right sidebar.
2.  **Run:** Download and open `IPTV-Controller-Windows.zip`, then run `main.exe`.
3.  **Requirement:** Ensure you have [MPV Player](https://mpv.io/installation/) installed on your system.

### 🐧 Linux Users (Ubuntu/Debian)
1.  Download the Linux binary from the [Releases](https://github.com/tanmay1117/Iptv-on-mpv-/releases) page.
2.  Give it execution permissions:
    ```bash
    chmod +x main_linux
    ./main_linux
    ```

### 🏹 Arch Linux / Advanced Users (Source Method)
If you prefer running from source or are on Arch Linux, follow these steps:

1.  **Install System Dependencies:**
    ```bash
    sudo pacman -S mpv python-pip
    ```
2.  **Clone & Setup Environment:**
    ```bash
    git clone [https://github.com/tanmay1117/Iptv-on-mpv-.git](https://github.com/tanmay1117/Iptv-on-mpv-.git)
    cd Iptv-on-mpv-
    python -m venv venv
    source venv/bin/activate.fish  # Use .fish for Arch/Fish shell users
    ```
3.  **Install Requirements & Run:**
    ```bash
    pip install -r requirements.txt
    python src/main.py
    ```

---

## 🛠️ Tech Stack
* **Frontend:** CustomTkinter (Modern Python UI)
* **Backend:** MPV Media Engine via Subprocess
* **API:** iptv-org/api integration
* **CI/CD:** GitHub Actions for automated multi-OS builds

---

## 🤝 Contributing
Contributions are welcome! If you want to add features like "Favorites" or "EPG Support":
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License
Distributed under the **MIT License**. See `LICENSE` for more information.

**Author:** [tanmay1117](https://github.com/tanmay1117)
