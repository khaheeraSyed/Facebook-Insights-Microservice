# Facebook-Insights-Microservice
facebook-insights-microservice/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── scraper.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── pages.py
│   └── services/
│       ├── __init__.py
│       └── facebook_service.py
│
├── frontend/
│   ├── index.html
│   └── script.js    
│    └── styles.css
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── requirements.txt
└── README.md
## Overview

This microservice allows users to fetch insights from Facebook Pages using their usernames.

## Technology Stack

- FastAPI for building APIs.
- MongoDB for data storage.
- Beautiful Soup for web scraping.

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies from `requirements.txt`.
4. Start MongoDB.
5. Run the application with:
   uvicorn app.main:app --reload 

6. Access API documentation at `http://127.0.0.1:8000/docs`.
7. Open web browser and search for http://127.0.0.1:8000/frontend/index.html

## API Endpoints

- **Get Page Details**: `/api/pages/{username}`
- **Get Recent Posts**: `/api/pages/{username}/posts`
- **Get Followers**: `/api/pages/{username}/followers`

## Running Tests

Run tests using:
pytest tests/
