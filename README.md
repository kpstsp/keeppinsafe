# keeppinsafe

# Backup Monitor

## Overview

**Backup Monitor** is a Django-based web application designed to help administrators monitor backup files for databases and website content. The application scans specified directories for backup files and displays their presence on a calendar view. Authorized users can log in to view the calendar, which updates every 5 minutes to reflect the latest backup status.

---

## Table of Contents

- [Goals](#goals)
- [Features](#features)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Goals

The primary goals of the Backup Monitor project are:

- **Automate Backup Monitoring**: Provide a visual representation of backup files' presence for databases and website content.
- **User Authentication**: Ensure that only authorized users can access the backup status.
- **Real-Time Updates**: Automatically update the backup status every 5 minutes to reflect any changes.
- **Ease of Use**: Offer a straightforward interface for users to quickly assess backup completeness.
- **Extensibility**: Design the application to be easily extendable for future enhancements.

---

## Features

- **Calendar View**: Displays a monthly calendar highlighting days with available backups.
  - **Database Backups**: Indicated by a blue 'd' on the date cell.
  - **Website Backups**: Indicated by a green 'w' on the date cell.
- **Automatic Refresh**: The calendar view refreshes every 5 minutes to show the latest backup status.
- **User Authentication**: Only authorized users can log in and view the backup calendar.
- **Responsive Design**: The interface adjusts to different screen sizes for better usability.
- **Navigation**: Users can navigate between months to view past and upcoming backup statuses.

---

## Requirements

- **Python**: 3.6 or higher
- **Django**: 3.2 or higher
- **Operating System**: Cross-platform (Tested on Unix/Linux and Windows)
- **Dependencies**:
  - `pathlib` (Standard in Python 3.4+)
  - Other dependencies as listed in `requirements.txt`

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/backup-monitor.git
cd backup-monitor
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Project

#### a. Set Up `settings.py`

- **Database Configuration**: By default, the project uses SQLite. Adjust `DATABASES` in `backup_monitor/settings.py` if necessary.

- **Backup Directories**:

  In `backup_monitor/settings.py`, set the paths to your backup directories:

  ```python
  from pathlib import Path

  BASE_DIR = Path(__file__).resolve().parent.parent

  # Define backup directories
  DB_BACKUP_DIR = Path('/absolute/path/to/db_backups')    # Replace with your actual path
  WWW_BACKUP_DIR = Path('/absolute/path/to/www_backups')  # Replace with your actual path
  ```

#### b. Set Up Authentication URLs

Ensure that the authentication URLs are included in `backup_monitor/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from monitor import views as monitor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
    path('', monitor_views.calendar_view, name='calendar'),
    path('<int:year>/<int:month>/', monitor_views.calendar_view, name='calendar'),
]
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

### 7. Run the Development Server

```bash
python manage.py runserver
```

---

## Usage

### Accessing the Application

- Open your web browser and navigate to `http://localhost:8000/`.
- Log in using the superuser credentials you created.

### Viewing the Calendar

- Upon logging in, you'll be presented with a calendar view of the current month.
- Dates with backups are marked:
  - **'d'**: Database backup available (colored blue).
  - **'w'**: Website files backup available (colored green).
- Dates from previous or next months are displayed in a lighter color.
- The current date is highlighted.

### Navigating Between Months

- Use the **Prev** and **Next** links at the top of the calendar to navigate between months.

### Automatic Refresh

- The calendar automatically refreshes every 5 minutes to display the latest backup status.

---

## Roadmap

Planned features and enhancements for future releases include:

### Short-Term Goals

- **Email Notifications**: Send alerts to administrators if backups are missing for a certain period.
- **Backup Integrity Check**: Verify the integrity of backup files and display warnings for corrupted files.
- **Multiple Site Support**: Extend the application to monitor backups for multiple websites and databases.

### Medium-Term Goals

- **Role-Based Access Control**: Implement different user roles (e.g., admin, viewer) with varying permissions.
- **Enhanced UI/UX**: Improve the visual design and user experience of the calendar view.
- **Customizable Backup Patterns**: Allow configuration of backup filename patterns to accommodate different naming conventions.

### Long-Term Goals

- **Dashboard View**: Provide a summary dashboard with statistics and trends on backup statuses.
- **API Integration**: Offer RESTful APIs for integrating with other systems or automation tools.
- **Dockerization**: Provide a Docker image for easy deployment.

---

## Contributing

Contributions are welcome! To contribute to Backup Monitor, please follow these steps:

1. **Fork the Repository**: Click the 'Fork' button at the top right of the repository page.

2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/yourusername/backup-monitor.git
   ```

3. **Create a Feature Branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**: Implement your feature or bug fix.

5. **Commit Your Changes**:

   ```bash
   git commit -am 'Add new feature'
   ```

6. **Push to Your Fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**: Open a pull request to the main repository's `develop` branch.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software in accordance with the terms of the license.

---

## Contact

For questions or support, please open an issue on the repository or contact the maintainer (check my GitHub or Linkedin: https://www.linkedin.com/in/konstantin-parashchevin/).

---

**Note**: Replace placeholders like `yourusername`, `/absolute/path/to/db_backups`, and `your.email@example.com` with your actual information.

---