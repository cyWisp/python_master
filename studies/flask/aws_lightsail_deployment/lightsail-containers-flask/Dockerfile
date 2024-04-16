# Set base image (host OS)
FROM python:3.12-alpine

# Python buffered environment
ENV PYTHONBUFFERED 1

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN python -m pip install --upgrade pip
RUN rm -rf ~/.cache/pip
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .

# Specify the command to run on container start
CMD [ "/usr/local/bin/python3.12", "/usr/src/app/app.py" ]