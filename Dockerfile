# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /movies

# Copy the project requirements.txt file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files to the container
COPY . .

# Expose the port that the application will run on
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
