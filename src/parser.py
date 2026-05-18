import re

def parse_report(text):
    def extract(pattern):
        match = re.search(pattern, text)
        return float(match.group(1)) if match else None

    return {
        "fast_res": extract(r"OK: t < 800.*?\(([\d\.]+)%\)"),
        "request_ko": extract(r"KO.*?\(([\d\.]+)%\)")
    }
    