import json
from email import policy
from email.parser import BytesParser
from utils import extract_links, phishing_score
from virus_total import scan_url
from header_check import validate_headers
from attachment_scan import scan_attachment


def analyze_email(file_path):
with open(file_path, 'rb') as f:
msg = BytesParser(policy=policy.default).parse(f)


subject = msg['subject']
sender = msg['from']
body = msg.get_body(preferencelist=('plain')).get_content()
links = extract_links(body)
score = phishing_score(body, len(links))


vt_results = {url: scan_url(url) for url in links}


headers_status = validate_headers(sender)


attachments_results = []
for attachment in msg.iter_attachments():
file_path = f"samples/{attachment.get_filename()}"
with open(file_path, "wb") as f:
f.write(attachment.get_content())
attachments_results.append(scan_attachment(file_path))


analysis_result = {
"subject": subject,
"sender": sender,
"link_count": len(links),
"phishing_score": score,
"is_suspicious": score > 3,
"virus_total_results": vt_results,
"header_checks": headers_status,
"attachments_scan": attachments_results
}


with open("reports/analysis_report.json", "w") as f:
json.dump(analysis_result, f, indent=4)


return analysis_result


if __name__ == "__main__":
import pprint
result = analyze_email("samples/phishing_sample.eml")
pprint.pprint(result)
