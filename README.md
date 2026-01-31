# 🏢 XYZ Company Project Management System

A Python-based CLI application designed to help **XYZ Company** manage project lifecycles and allocate workforce resources efficiently. This tool provides a simple text-based interface to track ongoing projects, manage worker availability, and archive completed tasks.

## 🚀 Features

* **Project Initialization:** Add new projects with details such as Project Code, Client Name, Start/End Dates, and required workforce.
* **Resource Management:** Automatically checks if enough workers are available before starting a new project.
* **Project Archiving:** Move projects from "Ongoing" to "Completed" status and release assigned workers back to the available pool.
* **Dynamic Updates:** Edit details of ongoing projects, including status and worker requirements.
* **Workforce Expansion:** Add new workers to the company pool dynamically.
* **Statistical Overview:** View a summary of ongoing projects, completed projects, and currently available workers.

## 🛠️ Usage

1.  **Start the Application:**
    Run the script using Python.
    ```bash
    python DOC333 Python Codes-rimaz.20231917.py
    ```

2.  **Initial Setup:**
    Upon launching, you will be prompted to enter the total number of workers currently in the company:
    `No of Workers: 10`

3.  **Main Menu Options:**
    * **1. Add a new project:** Input project details. The system will validate if you have enough workers.
    * **2. Remove a completed project:** Frees up workers and moves the project to the completed list.
    * **3. Add new workers:** Increases the total pool of available employees.
    * **4. Update details:** Modify specific details of an active project.
    * **5. Project Statistics:** View counts of projects and available resources.
    * **6. Exit:** Closes the application.

## 📋 Data Structure
The application uses in-memory lists to track session data:
* `ongoing_projects`: Stores active project dictionaries.
* `completed_projects`: Stores archived project dictionaries.
* `available_workers`: Tracks workforce availability.

## 📝 Requirements
* Python 3.x

---
*Developed for XYZ Company*
