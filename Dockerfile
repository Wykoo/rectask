#Starting with a Python 3.8 base
From python:3.8-slim-buster

#Setting up working directory
WORKDIR /app

#Copies requirements.txt file and installs Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copies enitre directory to the container
COPY . . 

#Exposes port 500 fot Flask app to run the program
EXPOSE 5000

#Setting up default command to run app.py file
CMD ["python", "app.py"]