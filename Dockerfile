# Use Python 3.11 base image
FROM python:3.11.9

# Set the working directory
WORKDIR /root/FallenRobot

# Copy all the files into the container
COPY . .

# Update package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y ffmpeg python3-pip curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
RUN pip install -U -r requirements.txt

# Default command to run your bot
CMD ["python3", "-m", "FallenRobot"]
