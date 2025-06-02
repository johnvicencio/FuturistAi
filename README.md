# FuturistAi

FuturistAi is a modern web application built with Flask and front-end technologies, showcasing simple AI-driven functionality and clean design. It features a responsive navbar, routing, and can be deployed to services like Render.

## Features

- Python Flask backend
- Mobile-friendly layout using Bootstrap or MDB
- Clean and minimal navigation UI
- GitHub repo link button
- Easy deployment to Render

## Getting Started

### Prerequisites

- Python 3.x
- pip
- Git

### Installation

```bash
git clone https://github.com/johnvicencio/FuturistAi.git
cd FuturistAi
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # For Windows: venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application locally:

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

## Deployment to Render

1. Make sure you have a `requirements.txt` and `Procfile` in the root folder.

**requirements.txt**
```
Flask
gunicorn
```

**Procfile**
```
web: gunicorn app:app
```

2. Push your code to your GitHub repo (e.g. `https://github.com/johnvicencio/FuturistAi`).

3. Go to [https://render.com](https://render.com) and:

- Create a new Web Service
- Connect your GitHub account and select your FuturistAi repo
- Set the build command:

```bash
pip install -r requirements.txt
```

- Set the start command:

```bash
gunicorn app:app
```

- Choose Python environment and deploy

## Project Structure

```
FuturistAi/
├── static/
│   └── img/
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── Procfile
├── README.md
```

## License

MIT License

---

Developed by John Vicencio, [https://johnvicencio.com](https://johnvicencio.com)
