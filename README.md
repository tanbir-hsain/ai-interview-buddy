# AI Interview Buddy

## Project Description

AI Interview Buddy is a full-stack web application that helps users prepare for technical interviews by asking AI-powered interview questions.

Users can enter interview-related questions through a simple web interface. The React frontend sends the question to the FastAPI backend through REST APIs. The backend communicates with the Google Gemini API to generate interview-focused responses and stores the conversation in MongoDB.

This project demonstrates Frontend Development, Backend Development, REST API Integration, AI API Integration, Database Integration, Docker, and GitHub Actions (CI).

---

## Tech Stack

- React
- JavaScript
- CSS
- FastAPI
- Python
- MongoDB
- Google Gemini API
- Docker
- Docker Compose
- Git
- GitHub
- GitHub Actions (CI)

---

## System Architecture

```text
User
   ↓
React Frontend
   ↓
REST API
   ↓
FastAPI Backend
   ↓
Google Gemini API
   ↓
AI Response
   ↓
MongoDB
   ↓
Response displayed to User
```

---

## Features

- AI-powered interview question answering
- React frontend
- FastAPI backend
- Google Gemini API integration
- MongoDB chat history storage
- REST API communication
- Dockerized application
- GitHub Actions CI workflow

---

## Project Workflow

1. User enters an interview question.
2. React sends the question to the FastAPI backend.
3. FastAPI receives the request.
4. FastAPI sends the question to the Google Gemini API.
5. Gemini generates the answer.
6. FastAPI stores the question and answer in MongoDB.
7. FastAPI returns the response.
8. React displays the answer.

---

## AI Model

### Provider

- Google Gemini API

### Purpose

- Interview question answering

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/tanbir-hsain/ai-interview-buddy.git
```

```bash
cd ai-interview-buddy
```

---

### Environment Variables

Create a `.env` file inside the backend folder and add:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

### Run with Docker

```bash
docker compose up --build
```

Open:

```
http://localhost:5173
```

---

## API Endpoint

### Request

```http
POST /api/chat
```

Example Request

```json
{
  "question": "Explain HTML block-level elements."
}
```

Example Response

```json
{
  "answer": "Block-level elements always start on a new line and take up the full available width."
}
```

---

## Skills Demonstrated

- React
- FastAPI
- REST API Development
- MongoDB
- Google Gemini API Integration
- Docker
- Docker Compose
- Git & GitHub
- GitHub Actions (CI)
- Full Stack Development

---

## Future Improvements

- User authentication
- Chat history management
- Markdown rendering improvements
- Deploy using Docker on AWS EC2
- Add unit and integration tests
- Continuous Deployment (CD)

---

## Author

**Tanbir Hussain**

GitHub  
https://github.com/tanbir-hsain

LinkedIn  
https://www.linkedin.com/in/tanbir-hussain-76320b414