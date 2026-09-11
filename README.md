# Quick start
```bash```
```py -m venv venv```
```.\venv/bin/activate```
```pip install -r requirements.txt```
```cp .env.example .env```
```python manage.py migrate```
```python manage.py seed_diseases```
```python manage.py runserver```

# Endpoint	Method	Description
```/api/auth/register/	POST	Create account```
```/api/auth/login/	POST	Get JWT tokens```
```/api/diseases/	GET	List disease catalog```
```/api/detections/	POST	Upload photo, get diagnosis```
```/api/detections/?disease=	GET	Scan history, filterable```

# Tech stack
```Layer	Tech```
```Backend	Django, Django REST Framework```
```Auth	SimpleJWT```
```Database	PostgreSQL (SQLite for local dev)```
```ML	PyTorch / Hugging Face (in progress)```
```Frontend	React (separate repo)```

# Features
 ```JWT auth (register/login/refresh) with email-based login```
 ```Photo upload with validation, scored disease prediction```
 ```Full disease catalog — symptoms, treatment, and prevention per class```
 ```Scan history, filterable by disease```
 ```Swappable inference layer — ships with a mock ML engine so the API contract is stable while the real PyTorch model is trained in parallel```
