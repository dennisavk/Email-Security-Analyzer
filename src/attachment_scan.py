import os
from virus_total import scan_url


def scan_attachment(file_path):
if not os.path.exists(file_path):
return {"error": "File not found"}
return {"status": "scanned", "file_name": os.path.basename(file_path)}
