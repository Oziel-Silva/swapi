### How to run!!!
This code is a Flask web application that utilizes the requests library to make a GET request to the Star Wars API to retrieve information about starships. The MGLT parameter can be passed in as a query parameter to the endpoint and defaults to 1,000,000 if not provided. The json library is used to parse the response from the API.

The script then performs some calculations on the retrieved data to determine the number of stops each starship would need to make based on its MGLT and consumables values. The results are stored in a dictionary final_results with the key being the name of the starship and the value being the number of stops.

The script then constructs a string containing the results in a more user-friendly format and returns this string to the user when they visit the endpoint.

Finally, the script uses the waitress library to run the application on the host IP 0.0.0.0 and port 8080.

In order to exec this app, follow the steps bellow:

First we need create a virtual environment and install dependencies:
use:
```
$ python3 -m venv env && source env/bin/activate
```
if you are using windows follow the step on this doc: <link>
to create a virtual-env

to install dependencies, use:
```
(env)$ pip3 install -r requirement.txt
````

Now, let's run using:
```
(env)$ python hello.py
```

On the web browser let's put on the url:
```
http://127.0.0.1:8080
```
In order to alter the MGLT value we need parse it on the url, for exemple:
```
http://127.0.0.1:8080?MGLT=500000
````
If this value not was putted, the default value is 1000000.
