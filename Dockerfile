# base image
FROM python:3.7

# working directory
WORKDIR /code 

# copy dependencies to working directory
COPY requirements.txt .

# install dependencies in working directory
RUN pip install -r requirements.txt

# copy files from src directory to working directory
COPY src/ .

# command to run on container start
CMD ["python", "./main.py"]