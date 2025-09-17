# Django Resume - Pratham Saraf's Professional Portfolio

A Django-based web application to showcase Pratham Saraf's professional resume and portfolio. This project displays comprehensive career information including education, professional experience, projects, research, technical skills, and extracurricular activities in a clean, professional format.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd se_ind_assignment
```

### 2. Create and Activate a Virtual Environment (Recommended)
To prevent conflicts with system dependencies, create a virtual environment:

**Create virtual environment:**
```bash
python -m venv venv
```

**Activate the virtual environment:**

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
Install Django and other required dependencies:

```bash
pip install django
```

### 4. Apply Database Migrations
Run the following command to set up the database:

```bash
python manage.py migrate
```

### 5. Run the Development Server
Start the Django application:

```bash
python manage.py runserver
```

The application will be available at:
🌐 **http://127.0.0.1:8000/**

## Project Structure

```
django_resume/
├── django_resume/          # Main Django project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings configuration
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── resume/                 # Resume app directory
│   ├── templates/resume/   # HTML templates
│   │   └── resume.html     # Main resume template
│   ├── static/resume/      # Static files (CSS, JS, images)
│   │   └── css/
│   │       └── styles.css  # Resume styling
│   ├── __init__.py
│   ├── admin.py           # Django admin configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Data models (currently unused)
│   ├── tests.py           # Unit tests
│   ├── urls.py            # App URL routing
│   └── views.py           # View functions
├── manage.py              # Django management script
├── db.sqlite3            # SQLite database
└── README.md             # This file
```

## Features

### 📋 Professional Resume Display
- **Complete Professional Profile**: Displays comprehensive career information
- **Education**: NYU Masters in Computer Science, Manipal University B.Tech
- **Professional Experience**: Internships at HPE, ONGC, and OnFees
- **Projects**: GuardNet DNS Security Platform, WholeSight AI Nutrition Assistant
- **Research**: Facial Morphing Detection, Computational Neuroscience
- **Technical Skills**: Organized by categories (Languages, Databases, Frameworks, etc.)
- **Extracurricular Activities**: Leadership and mentoring experience

### 🎨 Design Features
- **Professional Styling**: Clean, business-appropriate design
- **Responsive Layout**: Works on desktop, tablet, and mobile devices
- **Print-Friendly**: Optimized for printing to PDF or paper
- **Modern Typography**: Easy-to-read fonts and proper spacing
- **Color Coding**: Strategic use of colors to highlight important information

### 🛠 Technical Features
- **Django Framework**: Built with Django 5.2.6
- **Static Files Management**: Proper separation of CSS and HTML
- **Template System**: Uses Django templates for maintainability
- **Responsive Design**: CSS Grid and Flexbox for layout
- **Cross-browser Compatibility**: Works across modern browsers

## Customization

### Updating Resume Content
To update the resume information:

1. Edit the content in `resume/templates/resume/resume.html`
2. Modify personal information, experience, projects, etc.
3. Save the file and refresh the browser

### Styling Changes
To modify the appearance:

1. Edit `resume/static/resume/css/styles.css`
2. Customize colors, fonts, spacing, or layout
3. Use browser developer tools to test changes

### Adding New Sections
To add new sections to the resume:

1. Add HTML structure in `resume/templates/resume/resume.html`
2. Add corresponding CSS styles in `styles.css`
3. Follow the existing pattern for consistency

## Development

### Running in Development Mode
The project is configured for development with:
- `DEBUG = True` in settings
- SQLite database for simplicity
- Django development server

### Production Deployment
For production deployment:
1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Set up proper database (PostgreSQL recommended)
4. Configure static files serving
5. Use a production WSGI server like Gunicorn

## Browser Support

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## License

This project is for educational and personal use.

## Contact Information

**Pratham Saraf**
- 📧 Email: prathamssaraf@gmail.com
- 📱 Phone: +1 347-793-7420
- 🌐 GitHub: github.com/prathamssaraf/
- 📍 Location: Brooklyn, New York, USA

## Screenshots

The resume displays the following sections:
- Professional header with contact information
- Education with GPAs and coursework details
- Professional experience with quantified achievements
- Technical projects with technology stacks
- Research work and publications
- Comprehensive technical skills grid
- Extracurricular activities and leadership

---

*Professional Django Resume • Modern Design • Responsive Layout*