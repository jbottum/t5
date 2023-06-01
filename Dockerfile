# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the code file into the container
RUN pip install torch torchvision
COPY t5.py .

# Install the required dependencies
RUN pip install transformers

# Set the command to run when the container starts
CMD ["python", "t5.py"]

