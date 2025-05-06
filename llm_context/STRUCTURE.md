# Project Structure Overview

This document provides a clear outline of the file and folder organization for the AI-powered Web App, including backend, frontend, and IDE-integrated LLM contexts.

## Folder summary:

- `backend/`: FastAPI (Python) backend implementation.
- `frontend/`: React/Vite/Tailwind frontend code.
- `llm_context/`: Contains context & instructions for IDE-integrated LLM assistant:
  - `STRUCTURE.md`: This document, outlining the entire folder structure.
  - `PROJECT.md`: Detailed project overview and goals.
  - `tech_stack.json`: Detailed tech stack used.
  - `llm_instructions.txt`: LLM prompt and behavioral guidelines.

---

## Detailed Structure:
```markdown
AI-powered-Web-App/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   └── users.py
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── Dockerfile
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
│
├── llm_context/                 # LLM-specific contextual info (🔥 newly updated!)
│   ├── STRUCTURE.md             # Detailed folder and file structure description
│   ├── PROJECT.md               # Clearly defines project goals and objectives
│   ├── tech_stack.json          # Tech stack clearly defined with versions
│   └── llm_instructions.txt     # Prompt and instructions for your LLM
│
├── .vscode/
├── .env
├── .gitignore
├── README.md
└── docker-compose.yml
```
---
