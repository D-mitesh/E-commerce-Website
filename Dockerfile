# Use the official Python image from the Docker Hub
FROM python:3.12.0

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /buycom

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /buycom/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /buycom/

# Run Django commands to collect static files, apply migrations, and start the server
#RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Expose the port that the Django app runs on
EXPOSE 8000

# Start the Django application
CMD ["gunicorn", "buycom.wsgi:application", "--bind", "0.0.0.0:8000"]
