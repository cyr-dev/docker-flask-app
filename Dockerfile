# Base python docker image
FROM python:3.9.5-buster

# Import Code 
ADD . /Code

# Changing the directory
WORKDIR /Code

# Installating lib 
RUN pip install -r requirements.txt


# Exposing the port 
EXPOSE 5001

# Running python file
CMD python main.py