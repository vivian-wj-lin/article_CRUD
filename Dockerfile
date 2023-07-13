# Use an official Python runtime as a parent image
FROM python:3.7.17-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Run the command to start uWSGI
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "article_CRUD.wsgi:application"]
