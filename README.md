# Table of Contents
* [General info](#General-info)
* [Additional info](#Additional-info)
* [Installation](#Installation)
* [Usage](#Usage)

## General Info
This is a rectruitment task as web application that allows user to search for example: the different rates or maximum differnce between bid and ask prices

## Aditional Info
From the start i wanted to write that task with OOP, but it seems more efficient with def only, so i stayed with the second version

## Installation
1. Clone the repository 
```
git clone https://github.com/Wykoo/rectask.git
```

2. Change your directory to the project directory
```
cd rectask
```

3. Install the required 
```
pip install -r requirements.txt
```

4. Run the Flask app (standard port=5000)
```
flask run
```

## Usage
### Endpoints

1. '/avg' - 
Retrieves the average exchange rate for a specific argument

Example
```
GET /avg?table=A&code=USA&date=2022-04-21
```

Response
```
"0": 3.7191
```

2. '/max-min-rate' - 
Retrieves maximum difference between ask and bid prices for a specific argument

Example
```
GET /max-min-rate?table=A&code=USA&topCount=10
```

Response
```
Max: 3.7288, Min: 3.6948
```

3.'buy-ask' - 
Retrieves maximum difference between highest and lowest prices for a specific argument

Example
```
GET /buy-ask?table=A&code=USA&topCount=10
```

Response
```
Max: 3.7288, Min: 3.6948
```



