# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

# Use an ENTRYPOINT instead of CMD and then you can use command line options 
ENTRYPOINT ["python3", "RF_deploy.py"]
