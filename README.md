# Restaurant Search Application

This is a Django-based web application that allows users to search for restaurants based on the dishes they offer. It utilizes a SQLite database to store restaurant information and provides a responsive interface for searching and displaying results.

## Features

-   **Search Functionality:** Users can search for restaurants based on the dishes they offer.
-   **Detailed Restaurant Information:** Each restaurant listing includes details such as name, location, and price of dishes.

## Requirements

-   Python 3.x
-   Django 4.x
-   SQLite (included with Python by default)

## Installation

### Clone the Repository:

```bash
git clone https://github.com/your_username/restaurant-search.git
cd restaurant-search
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

```

## Usage

1. **Access the Application:**

    - Open a web browser and navigate to `http://127.0.0.1:8000/`.

2. **Search for Restaurants:**

    - Enter a dish name (e.g., "samosa") in the search box.
    - Click on the "Search" button to view restaurants offering that dish.
    - Example: http://127.0.0.1:8000/search?query=samosa

3. **View Search Results:**
    - Restaurants matching the search query will display their names, locations, and dish prices.
    - Click on individual restaurant listings to view more details.
    - Navigate through different pages if multiple results are found.

## Screenshots

Explore screenshots of the application in the `screenshots/` folder within the project directory.
