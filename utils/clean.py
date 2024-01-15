import re


# Remove all non-ASCII characters
def clean(text):
    cleaned_text = text.replace('\r', '').replace('\n', '')
    # Check if non-ASCII characters are present
    if any(ord(char) > 127 for char in cleaned_text):
        cleaned_text_ascii = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)
        return cleaned_text_ascii
    else:
        return cleaned_text