# Django Resume Builder (Simple CRUD)

A Django web application that allows users to create, read, update, and delete resume entries using a single model. This project uses a manually built HTML form and simple styling for demonstration.

## ✅ Features

- Add new resumes
- View all resumes
- Edit resume entries
- Delete resume entries
- Upload profile pictures
- Manual HTML form (no Django Form class)

## 🛠 Technologies Used

- Python 3.x
- Django 4.x+
- SQLite (default)
- HTML5 & CSS3

## 🧾 ResumeModel Fields

FullName, ProfilePicture, Email, Phone, Address, Summary, Degree, InstituteName, YearOfGraduation, CompanyName, Position, YearsOfExperience, Skills (comma-separated), Hobbies (comma-separated), Achievements (comma-separated)

## 📁 Project Structure

resume_project/
├── resume_app/
│   ├── templates/resume_app/
│   │   ├── create.html
│   │   ├── list.html
│   │   └── edit.html
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── media/
├── db.sqlite3
├── manage.py
├── resume_project/
│   ├── settings.py
│   ├── urls.py
├── requirements.txt
└── README.md

## ⚙️ How to Run This Project

1. Clone the repository:
   git clone https://github.com/yourusername/django-resume-builder.git
   cd django-resume-builder

2. Create virtual environment:
   python -m venv env
   source env/bin/activate   # Windows: env\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt
   (or pip install django if requirements.txt is missing)

4. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Run development server:
   python manage.py runserver

Open your browser: http://127.0.0.1:8000/

## 🧑 CRUD URLs

- Create: /add/
- Read/List: /
- Update: /edit/<id>/
- Delete: /delete/<id>/

## 📤 Manual Resume Form Example (create.html)

<form method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  <input type="text" name="FullName" placeholder="Full Name" required><br>
  <input type="file" name="ProfilePicture"><br>
  <input type="email" name="Email" placeholder="Email" required><br>
  <input type="text" name="Phone" placeholder="Phone"><br>
  <input type="text" name="Address" placeholder="Address"><br>
  <textarea name="Summary" placeholder="Summary"></textarea><br>
  <input type="text" name="Degree" placeholder="Degree"><br>
  <input type="text" name="InstituteName" placeholder="Institute Name"><br>
  <input type="text" name="YearOfGraduation" placeholder="Year of Graduation"><br>
  <input type="text" name="CompanyName" placeholder="Company Name"><br>
  <input type="text" name="Position" placeholder="Position"><br>
  <input type="number" name="YearsOfExperience" placeholder="Years of Experience"><br>
  <input type="text" name="Skills" placeholder="Skills (comma-separated)"><br>
  <input type="text" name="Hobbies" placeholder="Hobbies (comma-separated)"><br>
  <input type="text" name="Achievements" placeholder="Achievements (comma-separated)"><br>
  <button type="submit">Save</button>
</form>

## 🎨 Styling (Optional)

Put CSS inside: static/resume_app/style.css  
And link in HTML:

<link rel="stylesheet" href="{% static 'resume_app/style.css' %}">

## ✍️ Future Features

- Export resume to PDF
- Add user authentication
- Bootstrap/Tailwind UI

## 👤 Author

Created by Your Name  
your.email@example.com

## 📜 License

This project is licensed under the MIT License
