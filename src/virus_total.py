import requests


API_KEY = "YOUR_VIRUSTOTAL_API_KEY"


def scan_url(url):
headers = {"x-apikey": API_KEY}
data = {"url": url}
response = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data=data)
if response.status_code == 200:
result = response.json()
analysis_id = result['data']['id']
report = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=headers)
return report.json()
else:
return {"error": f"VirusTotal API error: {response.status_code}"}
