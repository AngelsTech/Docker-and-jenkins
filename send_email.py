import smtplib
import os
from email.message import EmailMessage

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "abdullahshahid984@gmail.com"
EMAIL_PASSWORD = "gagj zgls dfwv jvbd"  # Use an App Password if using Gmail
EMAIL_RECEIVER = "abdullahshahid984@gmail.com"

# Corrected Path to the PDF file
pdf_file_path = r"network_cheatsheet.pdf"  # Specify the exact file name

# Ensure the file exists
if not os.path.isfile(pdf_file_path):
    print(f"Error: The file '{pdf_file_path}' does not exist.")
    exit()

# Create Email Message
msg = EmailMessage()
msg["Subject"] = "Converted PDF File"
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg.set_content("Please find the attached PDF file.")

# Attach the PDF
with open(pdf_file_path, "rb") as f:
    file_data = f.read()
    file_name = os.path.basename(pdf_file_path)

msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

# Send Email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")

