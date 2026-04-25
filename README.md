# Reminder to Look at You 👁️

> [!IMPORTANT]
> **BETA VERSION**: This project is currently in a beta state. Features are being active developed and may change.

## Overview
A screen time tracker and reminder tool for Linux, designed to help you stay productive and healthy by monitoring your usage and providing timely nudges.

### Goals
- [x] **Track Daily Screen Time**: Monitor active usage throughout the day.
- [x] **API Support**: Access your data via a local REST API.
- [ ] **Reminder Notifications**: (In Progress) System nudges for water/breaks.
- [ ] **Todos**: (Planned) Simple task management.
- [ ] **Eye Blink Reminder**: (Future) Prevent eye strain.

## Tech Stack
- **Languages**: Python
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **Environment Management**: Nix Flakes + [uv](https://github.com/astral-sh/uv)

---

## Getting Started

### 1. Prerequisites
- **Nix** (with Flakes enabled)
- **Linux** (Primary OS supported)

### 2. Enter the Development Environment
Run the following command to enter the pre-configured shell:
```bash
nix develop
```
*This will automatically set up the virtual environment and install dependencies.*

### 3. Running the Project
Once inside the environment, start all components (API, Database, and Tracker) with a single command:
```bash
python src/backend/main.py
```

- **API Access**: [http://localhost:8000](http://localhost:8000)
- **Tracking**: Logs will appear in the terminal as you use your system.


