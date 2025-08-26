import os
import shutil
import re


def extract_emails(input_file, output_file):
    with open(input_file, "r") as f:
        text = f.read()
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    
    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")
    print("✅ Emails extracted and saved!")




extract_emails("input.txt", "emails.txt")
