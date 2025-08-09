# VueJS Blog Project

A modern blog platform built with Flask and Vue.js, featuring Redis caching, Celery task queue, and comprehensive authentication.

## 🚀 Tech Stack

### Backend
- Python (98.3%)
- Flask Framework with extensions
- Redis Cache
- Celery for task processing
- SQL Database with SQLAlchemy
- MailHog for email testing

### Frontend
- Vue.js
- HTML/JavaScript
- RESTful API integration

## ✨ Features

### Core Features
- User Authentication with Flask-Security-Too
- RESTful API with Flask-RESTful
- Redis Caching System
- Background Task Processing with Celery
- Excel File Support with Flask-Excel
- Database Management with SQLAlchemy

### Advanced Features
- Role-based Access Control
- Email Verification System
- Background Task Queue
- Real-time Data Processing
- Secure Session Management
- Blueprint Architecture

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/iamabhaydawar/VueJS_BlogProject.git
cd VueJS_BlogProject
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up Redis
```bash
# Install Redis server according to your OS
# Start Redis server
redis-server
```

5. Set up Celery
```bash
# Start Celery worker
celery -A app.celery_app worker --loglevel=info

# Start Celery beat for scheduled tasks
celery -A app.celery_app beat --loglevel=info
```

6. Install and Set up MailHog

For Linux systems, follow these detailed installation steps:

```bash
# Install Golang package
sudo apt-get -y install golang-go

# Remove existing Go installation and install latest version
sudo rm -rf /usr/local/go && wget https://go.dev/dl/go1.23.0.linux-amd64.tar.gz && sudo tar -C /usr/local -xzf go1.23.0.linux-amd64.tar.gz && rm go1.23.0.linux-amd64.tar.gz
# This command removes old Go installation, downloads new version, extracts it, and cleans up

# Add Go to PATH in .bashrc and reload
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc && source ~/.bashrc && go version
# This adds Go to your PATH permanently and verifies the installation

# Set Go binary path
export PATH=/usr/local/go/bin:$PATH
# This sets Go binary path for current session

# Reload bash configuration
source ~/.bashrc

# Verify Go installation
go version

# Add Go path to bashrc and verify again
echo 'export PATH=/usr/local/go/bin:$PATH' >> ~/.bashrc && source ~/.bashrc && go version

# Install MailHog using Go
go install github.com/mailhog/MailHog@latest

# Verify MailHog installation
~/go/bin/MailHog --version

# Start MailHog in background
~/go/bin/MailHog > /dev/null 2>&1 &
# This runs MailHog in the background, suppressing all output
```

For other operating systems:

```bash
# On macOS:
brew install mailhog

# On Windows:
# Download the binary from https://github.com/mailhog/MailHog/releases
```

7. Run the application
```bash
python app.py
```

## 🔧 Configuration

### Redis Configuration
```python
# Configure Redis cache settings
cache = Cache(app)
```

### Celery Configuration
```python
# Configure Celery
celery_app = celery_init_app(app)
```

### Flask Application Setup
```python
app = Flask(__name__, template_folder='frontend', static_folder='frontend', static_url_path='/static')
```

### MailHog Configuration
```python
# In your Flask config
MAIL_SERVER = 'localhost'
MAIL_PORT = 1025  # Default MailHog SMTP port
MAIL_USE_TLS = False
MAIL_USE_SSL = False

# To use in your application
from flask_mail import Mail, Message

mail = Mail(app)

def send_email(subject, recipient, body):
    msg = Message(subject,
                 sender='your-app@example.com',
                 recipients=[recipient])
    msg.body = body
    mail.send(msg)
```

Access MailHog Web Interface:
- URL: http://localhost:8025
- SMTP Port: 1025
- Features:
  - Email testing and debugging
  - Web interface for email inspection
  - Email body and header analysis
  - Real-time email capture
