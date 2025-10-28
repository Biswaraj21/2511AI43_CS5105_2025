# Use an official lightweight Python image
FROM python:3.10-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy dependency files first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Streamlit app code into the container
COPY . .

# Expose Streamlit’s default port
EXPOSE 8501

# Default command to run Streamlit
CMD ["streamlit", "run", "tut02.py", "--server.port=8501", "--server.address=0.0.0.0"]
