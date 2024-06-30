# Use an official Python runtime as a parent image
FROM python:3.7

COPY . /app

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install  -r requirements.txt

EXPOSE $PORT 

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app