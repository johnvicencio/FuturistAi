# FuturistAi

FuturistAi is a modern web application built with Flask and front-end technologies, showcasing simple AI-driven functionality and clean design. It features a responsive navbar, routing, and a GitHub repository link button.

## Features

- Python Flask backend  
- Mobile-friendly layout using Bootstrap or MDB  
- Clean and minimal navigation UI  
- GitHub repo link button  

## Demo
[View Demo](#demo)

![FuturistAi Demo](https://github.com/johnvicencio/FuturistAi/blob/main/static/img/futuristai-demo.gif?raw=true)

## Technologies Used

- Python 🐍
- Flask 🔥
- HTML 🧱
- CSS 🎨
- JavaScript ⚙️

FuturistAi is a lightweight Python-based Flask web application that allows users to input a prompt through a web interface and receive a response generated by OpenAI's GPT model. It integrates OpenAI's official Python SDK to interact with their API and uses modern web technologies for the frontend.

Additional details:

- **Templating Engine**: Jinja2  
- **OpenAI API**: Accessed using the official `openai` Python SDK  
- **Astrology Calculation**: `swisseph` (Swiss Ephemeris)  
- **Time & Location Handling**: `datetime`, `pytz`, `geopy`, `timezonefinder`  
- **Frontend Framework**: Bootstrap 5  
- **Environment Variables**: Managed using `python-dotenv` 

## Getting Started

### Prerequisites

Install the following:

#### On macOS (using Homebrew):

```bash
brew install python
brew install git
```

#### On Windows:

Download and install:

- Python from https://www.python.org/downloads/
- Git from https://git-scm.com/download/win

Ensure `python` and `git` are available in your terminal or command prompt.

### Clone the Repository

```bash
git clone https://github.com/johnvicencio/FuturistAi.git
cd FuturistAi
```

### Create and Activate a Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Setting Environment Variables with a .env File

Create a file named .env in the project root folder with your environment variables, for example:

```.env
OPENAI_API_KEY=your_openai_api_key_here
FLASK_ENV=development
```

### Running the App Locally

Make sure your `app.py` file has the following block at the end:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

Then run:

```bash
python app.py
```

Or, if you prefer using Flask CLI:

```bash
export FLASK_APP=app.py           # macOS/Linux
set FLASK_APP=app.py              # Windows (Command Prompt)
$env:FLASK_APP = "app.py"         # Windows (PowerShell)

flask run
```

### View the App

Open your browser and go to:

```
http://localhost:5000
```

## Project Structure

```
FuturistAi/
├── static/
│   ├── css/
│   ├── img/
│   └── js/
├── templates/
│   ├── about.html
│   ├── base.html
│   ├── contact.html
│   └── index.html
├── app.py
├── requirements.txt
├── README.md
```

## License

MIT License

---

Developed by John Vicencio  
https://johnvicencio.com