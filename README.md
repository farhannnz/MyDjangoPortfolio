# My Portfolio Website

This is my personal portfolio website built with Django. The website features a techy feel, colorful theme, animations, transitions, and background images to create an extraordinary and visually appealing design.

## Features

- **Home Page**: An introduction with a catchy hero section, background images, and animations.
- **About Me**: A section detailing my background, skills, and experiences.
- **Projects**: A showcase of my projects with descriptions and links to their repositories or live demos.
- **Contact**: A contact form for visitors to get in touch with me.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: SQLite (for development), PostgreSQL (for production)
- **Styling**: Bootstrap, custom CSS
- **Animations and Transitions**: CSS animations, JavaScript libraries (like AOS)

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/portfolio-website.git
    cd portfolio-website
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Open your browser and visit**:
    ```
    http://127.0.0.1:8000/
    ```

## Deployment

For deploying the website to a production server, follow these steps:

1. **Set up your production environment** (e.g., using DigitalOcean, Heroku, etc.).
2. **Configure your production settings** in `settings.py`.
3. **Set up a production database** (e.g., PostgreSQL).
4. **Collect static files**:
    ```bash
    python manage.py collectstatic
    ```
5. **Apply migrations and create a superuser** if not done already:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

## Contact

Feel free to reach out if you have any questions or suggestions!

- **Email**: krahit57@gmail.com


---

Thank you for checking out my portfolio website!
