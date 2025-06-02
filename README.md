# FuturistAi

FuturistAi is a modern web application built with Flask and front-end technologies, showcasing simple AI-driven functionality and clean design. It features a responsive navbar, routing, and a GitHub repository link button.

## Features

- Python Flask backend  
- Mobile-friendly layout using Bootstrap or MDB  
- Clean and minimal navigation UI  
- GitHub repo link button  

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