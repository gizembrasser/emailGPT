import os
import sys
import imaplib
import email
from email.header import decode_header

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from data.constants import EMAIL_SERVER, EMAIL_ADDRESS, PASSWORD
from utils.clean import remove_non_ascii


# Takes N as argument, being the number of top emails to fetch
def get_emails(N):
    # Connect to Gmail IMAP server using SSL
    mail = imaplib.IMAP4_SSL(EMAIL_SERVER)
    mail.login(EMAIL_ADDRESS, PASSWORD)

    # Select the mailbox
    _, messages = mail.select("inbox")
    # Total number of emails, convert to int to make a `for` loop
    messages = int(messages[0])
    email_details = []

    # Iterate over range of email messages IDs in reverse order
    for i in range(messages, messages-N, -1):
        # Fetch the email message by ID, which is `i`
        _, msg_data = mail.fetch(str(i), "(RFC822)")

        for response in msg_data:
            details = {}

            if isinstance(response, tuple):
                # Parse a bytes email into a message object
                msg_data = email.message_from_bytes(response[1])
                # Decode the email subject
                subject, encoding = decode_header(msg_data["Subject"])[0]

                if isinstance(subject, bytes):
                    # If it's in bytes, decode to string
                    subject = subject.decode(encoding)
                # Decode email sender
                sender, encoding = decode_header(msg_data.get("From"))[0]

                if isinstance(sender, bytes):
                    sender = sender.decode(encoding)
                details["subject"] = subject
                details["from"] = sender

                # If the email message has multiple parts
                if msg_data.is_multipart():
                    # Iterate over each email part
                    for part in msg_data.walk():
                        # Extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # Get the email body
                            body = part.get_payload(decode=True).decode("utf-8")
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # Print text/plain emails and skip attachments
                            details["body"] = remove_non_ascii(body)

                else: 
                    # Extract content type of email
                    content_type = msg_data.get_content_type()
                    # Get the email body
                    body = msg_data.get_payload(decode=True).decode("utf-8")
                    if content_type == "text/plain":
                        # Print only email parts
                        details["body"] = remove_non_ascii(body)
            
                email_details.append(details)
        
    # Close the connection and logout
    mail.close()
    mail.logout()

    return email_details


print(get_emails(2))
    