# Use an official Python runtime as the base image
FROM python:3.10.2

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Copy the Python script
COPY run.py .

# Copy the unit test
COPY test.py .

# copy the CSV file
COPY sample_delivery_logs.csv .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Run the script
CMD ["python", "run.py", "sample_delivery_logs.csv"]
