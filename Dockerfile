# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages (none needed for your script, but this is how to add them)
RUN pip install flask

# Command to run the application
CMD ["python", "json_load.py"]
