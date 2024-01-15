import re


# Takes a string as input and replaces non alphanumerical characters with an underscore
def clean(text):
    return "".join(c if c.isalnum() else "_" for c in text)


# Remove all non-ASCII characters
def remove_non_ascii(text):
    # Check if non-ASCII characters are present
    if any(ord(char) > 127 for char in text):
        cleaned_text = re.sub(r'[^\x00-\x7F]+', '', text)
        return cleaned_text
    else:
        return text