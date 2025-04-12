# ✈️ Pilot Logbook Management System 📝

A **web-based application** designed for pilots to log flights, manage certifications, track training records, and generate  log reports. This system prioritizes user-friendly design, modular development, and secure data handling.

---

## ✨ **Features**
- 🔒 **User Authentication**: Register and log in securely.
- 🛫 **Flight Logs**: Add, view, edit, and delete detailed flight logs.
- 🧾 **Pilot Certification**: Manage single pilot certification with editable details.
- 🎓 **Training Records**: Track and manage your training records.
- 📄 **Report Generation**: Generate and download flight log reports in PDF format, including summaries like total flights and souls on board.
- ❌ **Error Handling**: Friendly messages for invalid inputs and errors.

---

## 🛠️ **Technologies Used**
- **Backend**: Django Framework (4.2)
- **Frontend**: Bootstrap (4)
- **Database**: SQLite
- **Language**: Python (3.13)

---

## 🚀 **Getting Started**

### Clone the Repository
```bash
git clone  https://github.com/dcccalvin/logbook_project.git
```

### Navigate into the Project Directory
```bash
cd pilot_logbook
```

### Apply Migrations
```bash
python manage.py migrate
```

### Start the Server
```bash
python manage.py runserver
```

### Access the Application
Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the application.

---

## 📚 Usage

### Register/Login
Create an account or log in to access the dashboard.

### Flight Logs
Add, edit, or delete your flight records with ease.

### Pilot Certification
Update and manage your single certification.

### Training Records
Track and update your training history.

### Report Generation
Generate downloadable PDF reports for your flights. Reports include individual flight details as well as a summary section showing total flights logged and total souls carried.

---

## Database
### Database schema
This is the schema for the database
![Database schema](<corrected schema.png>)

---


## 🤝 **Contributing**
We welcome contributions from the community! Here’s how you can help:

- **Fork the Repository**: Create your own copy and experiment freely.
- **Submit Pull Requests**: Improve features, fix bugs, or enhance the documentation.
- **Report Issues**: Found a bug or have a feature request? Open an issue.
- **Enhance Documentation**: Help us keep the docs up to date.

Your contributions are greatly appreciated! 🚀
