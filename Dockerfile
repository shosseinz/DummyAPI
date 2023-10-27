# Use an official Python runtime as a parent image
FROM python:3.9-slim as base


# Setup env
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of your test suite directory into the container
COPY . /app

# Install Robot Framework and any additional dependencies
RUN pip install robotframework

# Run your Robot Framework test suite using the robot command
CMD ["robot", "your_test_suite.robot"]