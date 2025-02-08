import os
import smtplib
import logging
from email.message import EmailMessage

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# SMTP Server Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email Credentials (Replace with secure environment variables)
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "your_email@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your_app_password")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "receiver_email@gmail.com")

# Path to PDF File
pdf_file_path = r"network_cheatsheet.pdf"

# Ensure the file exists
if not os.path.exists(pdf_file_path):
    logging.error(f"File not found: {pdf_file_path}")
    exit(1)

# Create Email Message
msg = EmailMessage()
msg["Subject"] = "Converted PDF File"
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg.set_content("Please find the attached PDF file.")

# Attach the PDF
try:
    with open(pdf_file_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(pdf_file_path)

    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)
except Exception as e:
    logging.error(f"Error attaching file: {e}")
    exit(1)

# Send Email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        logging.info("✅ Email sent successfully!")
except Exception as e:
    logging.error(f"❌ Failed to send email: {e}")
    exit(1)

