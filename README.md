📚 Library Management System (Django)

A full-stack web-based Library Management System built using Django that allows users to manage books, track borrowers, and handle book lending operations efficiently.

🚀 Features
🔐 Authentication System
User Registration & Login
Secure authentication using Django’s built-in system
Logout functionality
📖 Book Management
Add new books with:
Title
Author
Publication Date
Book Image
PDF Upload
View all books
Search books by title or author
👨‍🎓 Borrower Management
Borrow books with:
Borrower Name
Department
Borrow Date
Track borrowed books
Return book functionality
💰 Fine Calculation System
Automatic fine calculation:
First 5 days → No fine
After 5 days → ₹5/day
Fine reset on book return
📂 File Handling
Upload and store:
Book images
PDF files
View PDF directly in browser
🛠️ Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite (default)
Authentication: Django Auth System
Media Handling: Django File & Image Fields
📁 Project Structure
library-management-system/
│── app/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│
│── media/
│   ├── images/
│   ├── pdf/
│
│── db.sqlite3
│── manage.py
│── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
2️⃣ Create Virtual Environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver
🌐 Usage
Open browser: http://127.0.0.1:8000/
Register a new account
Login and manage books
Borrow and return books
View PDFs directly
📊 Database Models Overview
📘 Book Model
User (ForeignKey)
Image
PDF Upload
Title
Author
Publication Date
👤 Borrower Model
Book (ForeignKey)
Name
Department
Borrow Date
Fine
Returned Status (Yes/No)
🔍 Key Functionalities Explained
🔎 Search Feature
Users can search books by:
Title
Author
📄 PDF Viewer
Books uploaded as PDF can be viewed directly using Django FileResponse
💵 Fine Logic
if days_difference > 5:
    fine = 5 * (days_difference - 5)
else:
    fine = 0
    
📸 Screenshots (Optional)
<img width="523" height="401" alt="Screenshot 2026-01-03 082355" src="https://github.com/user-attachments/assets/eb3a6889-9781-4dc2-b802-bcc7ed4b8b5d" />
<img width="565" height="513" alt="Screenshot 2026-01-03 082552" src="https://github.com/user-attachments/assets/5f636ed4-04ea-4768-8284-0b2bfc3e05ba" />
<img width="1362" height="602" alt="image" src="https://github.com/user-attachments/assets/085fd3e2-c04e-43c5-93b0-75e929e885c2" />
<img width="728" height="599" alt="image" src="https://github.com/user-attachments/assets/a2110468-3954-4413-aa1b-adc6608949dd" />
<img width="1349" height="599" alt="image" src="https://github.com/user-attachments/assets/e4b39c31-38af-4028-ab88-75628b5ecd41" />


🧑‍💻 Author
Kaushal kumar
