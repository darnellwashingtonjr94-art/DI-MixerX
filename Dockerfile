# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the honeypot files into the container
COPY . /app/

# Install any required dependencies (if added to requirements.txt later)
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Create the data directory for the SQLite database
RUN mkdir -p /app/data

# Expose the common trap ports
EXPOSE 80 8080 8888 5555

# Run the master CLI daemon by default
CMD ["python", "cli.py", "--start", "--ports", "80", "8080", "8888"]
