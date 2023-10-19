# AGRIDASH

A dashboard which provides user with data to perform farming in an optimized way. This project allows farmers to access essential information and resources to improve their farming practices.


## Introduction

The Farming Dashboard is a web application built with Django Rest Framework that serves as a tool for farmers to optimize their farming practices. It provides access to crucial data and resources, including crop information, weather data, market price, and more, to enhance the efficiency of farming operations.

## Features

- **Crop Information**: Access detailed information about various crops, including planting schedules, growth stages, and recommended practices.
- **Weather Data**: Real-time weather data for better decision-making, including weather forecasts and historical data.
- **Crop Management**: Input data about crops, such as planting dates and care practices, and receive recommendations and reminders.
- **Market Data**: Real-time market data, including crop prices, to make informed selling decisions.
- **Farming Tips**: Educational content and tips to improve farming skills.

## Usage

Follow these steps to set up the Dashboard on your local environment:

1. Clone the repository:

   ```
   git clone https://github.com/Dhyuti/agridash.git
   cd agridash
   ```
2. Create a virtual environment and activate it:

   ```
   pipenv shell
   ```
3. Installing dependencies:

   ```
   pipenv install
   ```

 4. Migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

 5. To run dev server run this command

    ```
    python manage.py runserver
    ```
