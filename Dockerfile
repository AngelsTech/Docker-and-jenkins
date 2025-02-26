# Use an official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y libreoffice && rm -rf /var/lib/apt/lists/*

# Copy files
COPY . /app/

# Create and activate a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies inside the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV EMAIL_SENDER=""
ENV EMAIL_PASSWORD=""
ENV EMAIL_RECEIVER=""

# Default command
CMD ["sh", "-c", "if [ -f convert.py ]; then python convert.py; fi && if [ -f send_email.py ]; then python send_email.py; fi"]
