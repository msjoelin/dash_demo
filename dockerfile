# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the app
EXPOSE 8000

# Run the Dash app using Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:server"]