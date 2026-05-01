🛡️ AI Phish-Tank

A Multi-Modal Security Pipeline for Automated Phishing Detection
📖 Description

AI Phish-Tank is an automated security orchestrator that bridges the gap between traditional OSINT and modern Computer Vision. Unlike standard scanners that rely on static blacklists, AI Phish-Tank "analyzes" a website through the eyes of a SOC analyst. By correlating visual brand identity with technical metadata, it identifies sophisticated impersonation attacks in real-time.
🚀 Key Features

    📸 Automated Evidence Collection: Orchestrates Playwright to navigate dynamic, JavaScript-heavy sites and capture high-fidelity forensic screenshots.

    🧠 AI Vision Reasoning: Leverages a Vision-Language Model (Llava) via Ollama to perform heuristic brand recognition and intent analysis.

    ⏳ Domain Age Enrichment: Integrates Whois OSINT to verify the "birth certificate" of a domain, instantly flagging "newborn" sites masquerading as established entities.

    ⚖️ Contextual Mismatch Detection: Cross-references visual cues (e.g., a "Reddit" logo) against the actual root domain to detect visual-technical inconsistencies.

🛠️ Technical Pipeline

The system operates as a modular, three-stage pipeline designed for privacy and speed by running entirely on local hardware.
1. The Sensor (Playwright)

A headless browser engine that visits the target URL. This stage bypasses basic bot detection and captures the "victim's perspective," rendering the site exactly as it appears in a standard browser.
2. The Detective (Whois/OSINT)

The system extracts the domain and queries its registration history. In phishing defense, the Domain Age is a high-confidence trust signal; a discrepancy between a global brand and a 24-hour-old domain is treated as a critical "Red Flag."
3. The Brain (Llava VLM)

The "Thinking" layer. Using a Vision-Language Model (VLM), the system performs OCR and logo detection. It doesn't just see pixels; it understands context, allowing it to realize that a site looking like a login page hosted on an unrelated domain is a high-risk threat.
💻 Technical Stack

    Language: Python 3.10+

    Automation: Playwright (Chromium)

    AI Inference: Ollama (Llava 7b/13b)

    OS/Environment: Kali Linux / Virtual Environment (venv)

    Data Sources: python-whois (OSINT)

🔧 Installation & Usage
Bash

# Clone the repo
git clone https://github.com/mohamedbennour31/ai-phish-tank.git

# Install dependencies
pip install -r requirements.txt

# Run a security audit
python3 phish_shield.py
