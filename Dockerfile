FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04

# Install Python and other necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

    
# Set the working directory
WORKDIR /app
    
# Copy the current directory contents into the container at /app
COPY . /app

# Install pip requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port that the FastAPI server will run on
EXPOSE 8000

# Command to run the FastAPI server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
