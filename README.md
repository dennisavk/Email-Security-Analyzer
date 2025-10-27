# 🧠 Email Security Analyzer (Advanced Version)

A Python-based tool that analyzes emails for phishing and security threats. It parses email metadata, validates headers, scans links and attachments using **VirusTotal**, and provides a visual interactive dashboard using **Streamlit**.  

---

## Features
- 📧 Extract email metadata (Subject, Sender)  
- 🔍 Detect suspicious keywords and calculate phishing score  
- 🛡️ Validate SPF, DKIM, and DMARC records  
- 🌐 Scan URLs via VirusTotal API  
- 📎 Scan email attachments for potential malware  
- 📊 Interactive Streamlit dashboard for visual reporting  

---

## Installation

1. **Clone the repository and install dependencies**
```bash
git clone https://github.com/dennisavk/EmailSecurityAnalyzer.git
cd EmailSecurityAnalyzer
pip install -r requirements.txt
```

2. **Setup VirusTotal API**  
- Get a free API key from [VirusTotal](https://www.virustotal.com/gui/join-us)  
- Open `src/virus_total.py` and replace `YOUR_VIRUSTOTAL_API_KEY` with your key  

3. **Ready to run!**  
- You can now run the analyzer or launch the Streamlit dashboard (see Usage section below).

---

## Usage

### 1️⃣ Command-Line
```bash
python src/analyzer.py
```
- Default example email: `samples/phishing_sample.eml`  
- Generates JSON report: `reports/analysis_report.json`  

### 2️⃣ Streamlit Dashboard
```bash
streamlit run src/dashboard.py
```
- Upload `.eml` files via the dashboard  
- View phishing score, header checks, links & attachment scans interactively  

---

## Sample Output (JSON)
```json
{
  "subject": "Your account is locked!",
  "sender": "security@fakebank.com",
  "link_count": 2,
  "phishing_score": 7,
  "is_suspicious": true,
  "virus_total_results": {
      "http://malicious-link.com": {...}
  },
  "header_checks": {
      "spf": true,
      "dkim": false,
      "dmarc": true
  },
  "attachments_scan": [
      {"file_name": "invoice.pdf", "status": "scanned"}
  ]
}
```

---

## Folder Structure
```
EmailSecurityAnalyzer/
│
├── src/                  # Core code
├── tests/                # Unit tests
├── samples/              # Sample emails and attachments
├── reports/              # JSON analysis reports
├── requirements.txt
├── README.md
└── LICENSE
```

---

## How It Works
1. Parses `.eml` files for metadata, body, and attachments  
2. Detects phishing keywords and calculates a phishing score  
3. Validates headers: SPF, DKIM, DMARC  
4. Extracts URLs and scans them via VirusTotal  
5. Scans attachments for potential malware  
6. Generates a detailed JSON report  
7. Optionally displays results in a Streamlit dashboard  

---

## License
MIT License – free to use, modify, and distribute.  
