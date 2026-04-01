import re

def clean_text(text):
   
    text = re.sub(r'\$\$\$.*?\$\$\$', '', text)
    text = re.sub(r'###|!!!|\?\?\?', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_email_body(text):
   
    if "Subject:" in text:
        return text.split("Subject:")[-1]
    return text