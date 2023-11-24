Backend Developer with AI-Focus Assignment @strativ
======================
The weather in Dhaka is too hot to handle. Let's travel somewhere to cool off. We have the latitude and longitude of all the districts of Bangladesh here: https://raw.githubusercontent.com/strativ-dev/technical-screening-test/main/bd-districts.json, Using the API from open-meteo.com, we can get the temperature forecasts of each district for up to 7 days: https://open-meteo.com/en/docs. *Note:* The weather forecasts are updated periodically, according to the documentation.

* **Task 1:** Let's make an API for the coolest 10 districts based on the average temperature at 2pm for the next 7 days. *Constraint:* No API responses for a user of the system should exceed 500 ms.
* **Task 2:** Train a *simple model* that forecasts the weather conditions in a given *future date*. To simplify things, restrict predictions to the Dhaka district. After training the model, the model should be query-able via a simple API. For example, your API should be able to predict the temperature at any future date (beyond the 7 days provided by OpenMeteo). *Note:* If you feel that you do not have enough time and want to simplify further, provide a written solution plan for this section instead of a coded solution.

Deployment Instructions
-----------------------
* Clone this repositories in your machine
* Create a virtual environment with PIP, activate that and install all packages
`$ python3 -m venv ~/venvs/strativ`
`$ source ~/venvs/strativ/bin/activate`
`$ pip install --upgrade pip setuptools wheel black --no-cache-dir`
`$ pip install -r requirements.txt --no-cache-dir`

* **For Task 1:** Run the below commands. *Note:* It will take around 2 minutes, because it has to fetch weather data from the OpenMeteo API for all the 64 districts and do some computations to create a *Hashmap*, so that we can lookup the 10 coolest districts in *O(1)* constant time.
`$ python3 task_1/app.py`
After that, using Postman or any other similar software, make a GET request with the below endpoint -
`http://127.0.0.1:5000/coolest_10`

* **For Task 2:** Run the below commands -
`$ jupyter notebook`
Then open the *analysis.ipynb* in the browser and run all the cells in order to generate the *forcast.csv*, which is the future weather prediction dataset from January 2023 to April 2050. Implemented NeuralProphet deep learning package for the time-series dataset named *dhaka_2020-2022.csv*, which includes historical temperature data from the year 2020 to 2022 for Dhaka district. After that, run the below python script  in order to create an API endpoint.
`$ python3 task_2/app.py `
After that, using Postman or any other similar software, make a GET request with the below endpoint -
`http://127.0.0.1:5000/get_temperature?date=2024-11-30`
Note: Above endpoint return the model predicted temperature on *2024-11-30*. You just need to put the desired date in YYYY-MM-DD format between January 2023 to April 2050.

Version
-------
* **v1.0** on **November 24, 2023**

Contributor
------------
* [**Kaiser Hamid Rabbi**](mailto:kaiser.hamid.rabbi@gmail.com) 
* [![Linkedin](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/kaiserhamidrabbi/)
