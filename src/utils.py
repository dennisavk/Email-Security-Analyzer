import re


SUSPICIOUS_PHRASES = ['password', 'verify your account', 'click here', 'urgent', 'login']


def extract_links(text):
return re.findall(r'http[s]?://\S+', text)


def phishing_score(text, links_count):
score = 0
if any(word.lower() in text.lower() for word in SUSPICIOUS_PHRASES):
score += 5
score += links_count
return score
