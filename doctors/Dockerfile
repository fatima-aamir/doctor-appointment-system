# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . .

# Expose the port that the application will run on
EXPOSE 9090

# Command to run the application
CMD ["python", "app.py"]
