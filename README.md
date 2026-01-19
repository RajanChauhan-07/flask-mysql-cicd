# Flask MySQL CI/CD Project

[![Build Status](http://44.203.78.191:8080/buildStatus/icon?job=flask-mysql-pipeline)](http://44.203.78.191:8080/job/flask-mysql-pipeline/)

## Description

A two-tier Flask web application with MySQL database, automated deployment using Docker and Jenkins CI/CD pipeline.

## Tech Stack

- **Frontend/Backend:** Flask (Python)
- **Database:** MySQL 8.0
- **Containerization:** Docker & Docker Compose
- **CI/CD:** Jenkins
- **Version Control:** GitHub
- **Infrastructure:** AWS EC2

## Features

- ✅ Automated deployment pipeline
- ✅ Docker containerization
- ✅ Database integration with MySQL
- ✅ Health check endpoints
- ✅ Integration tests
- ✅ Beautiful UI with form validation

## Architecture

```
Developer → GitHub → Jenkins → Docker → Flask + MySQL Containers
```

## How It Works

1. Developer pushes code to GitHub
2. GitHub webhook triggers Jenkins
3. Jenkins clones repository
4. Jenkins builds Docker images
5. Jenkins runs docker-compose
6. Integration tests verify connectivity
7. Application deployed successfully!

## Access the Application

Visit: http://44.203.78.191:5000

## Project Structure

```
flask-mysql-app/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Flask container definition
├── docker-compose.yml    # Multi-container orchestration
├── Jenkinsfile           # CI/CD pipeline definition
├── init.sql              # Database initialization
└── templates/
    └── index.html        # Frontend UI
```

## Future Enhancements

- [ ] Add unit tests
- [ ] Implement user authentication
- [ ] Add data visualization
- [ ] Set up production environment with SSL
- [ ] Implement database backups
- [ ] Add monitoring and logging

## Author

Rajan Chauhan

## License

MIT
