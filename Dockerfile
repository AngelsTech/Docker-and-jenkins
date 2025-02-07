FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy the script and requirements
COPY convert.py send_email.py network_cheatsheet.docx ./

# Install required Python packages (excluding smtplib)
RUN pip install --no-cache-dir python-docx reportlab

# Convert DOCX to PDF and send email
CMD python convert.py network_cheatsheet.docx network_cheatsheet.pdf && python send_email.py

