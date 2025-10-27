import dns.resolver


def check_spf(domain):
try:
answers = dns.resolver.resolve(domain, 'TXT')
for rdata in answers:
if "v=spf1" in str(rdata):
return True
return False
except Exception:
return False


def check_dkim(domain):
try:
selector = "default"
answers = dns.resolver.resolve(f"{selector}._domainkey.{domain}", 'TXT')
return True if answers else False
except Exception:
return False


def check_dmarc(domain):
try:
answers = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
return True if answers else False
except Exception:
return False


def validate_headers(sender_email):
domain = sender_email.split('@')[-1]
return {
"spf": check_spf(domain),
"dkim": check_dkim(domain),
"dmarc": check_dmarc(domain)
}
