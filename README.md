```markdown
# Dipanchal Innovation Lab (DiL) - Web Portal

Welcome to the official web portal repository for the **Dipanchal Innovation Lab (DiL)**. This project is a dynamic, scalable, and fully responsive Django-based web application designed to showcase the lab's research, publications, ongoing projects, and team members.

## 🌟 Key Features

### 1. Dynamic Content Management
* **Projects Portfolio:** Manage and display ongoing and completed research projects.
* **Progress Statistics:** Dynamically update the lab's core metrics (e.g., Active Researchers, Publications) directly from the admin dashboard.
* **Team Directory:** Categorized team roster (Advisors, Investigators, Mentors, RAs, URAs) with fallback avatars and social links.

### 2. Advanced Publications Archive
* **Search & Filtering:** Users can search publications by title or author, and filter by publication type (Conference, Journal, etc.) and year.
* **Interactive UI:** Seamless "Show/Hide Abstract" functionality and direct links to full papers.
* **Featured Spotlight:** Pin specific high-impact papers to the top of the publications page.

### 3. Integrated Contact & Admin Notification System
* **Dynamic Lab Info:** Update the lab's physical address, email, phone, and office hours globally via the admin panel.
* **Automated Alerts:** Contact form submissions automatically trigger an email alert to the lab admin.
* **Direct Admin Reply:** Administrators can reply to user inquiries directly from the Django Admin panel, which automatically sends a formatted email back to the user.

### 4. Cloud Asset Management
* **Cloudinary Integration:** All media uploads (project thumbnails, team avatars, publication covers) are securely handled and optimized via Cloudinary.

---

## 🚀 How to Run the Project Locally (VS Code)

Because this project uses environment variables to protect sensitive data (like database credentials, email passwords, and Cloudinary keys), the `.env` file is intentionally omitted from the repository. 

Follow these steps to set up the project on your local machine:

### Step 1: Clone the Repository
Open your terminal in VS Code and run:
```bash
git clone <your-repository-url>
cd dipanchallab

```

### Step 2: Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt

```

### Step 4: Configure Environment Variables

In the root directory of the project (where `manage.py` is located), create a new file named `.env`.

Copy the following template into your new `.env` file and replace the placeholder values with your actual credentials:

```ini
# --- .env ---

# Django Settings
SECRET_KEY=your_django_secret_key_here
DEBUG=True

# Cloudinary Settings (Get these from your Cloudinary Dashboard)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Email Settings (For Contact Form & Admin Replies)
# Note: If using Gmail, you must generate an "App Password" 
EMAIL_HOST_USER=your_lab_email@gmail.com
EMAIL_HOST_PASSWORD=your_16_digit_app_password

```

### Step 5: Apply Database Migrations

Set up your local SQLite database with the required schema:

```bash
python manage.py makemigrations
python manage.py migrate

```

### Step 6: Create a Superuser (Admin Access)

To access the backend and manage the lab's content, create an admin account:

```bash
python manage.py createsuperuser
# Follow the prompts to set your username, email, and password

```

### Step 7: Run the Development Server

```bash
python manage.py runserver

```

Open your browser and navigate to `http://127.0.0.1:8000/` to view the site, and `http://127.0.0.1:8000/admin/` to log into the dashboard.

---

## 🛠️ Usage Guide (Admin Panel)

Once logged into the Django Admin panel, you must perform a few initial setup steps:

1. **Lab Information:** Navigate to `Lab Information` and create exactly **one** record. This populates the contact page and footer.
2. **Progress Stats:** Add your 4 core statistics (e.g., Researchers, Projects, Publications, Partners) to populate the homepage grid.
3. **Replying to Messages:** When a user submits a contact form, go to `Contact Messages`, click on the message, type your response in the `Admin Reply` box, and click **Save**. The email will be dispatched automatically.

## 💻 Tech Stack

* **Backend:** Django, Python, SQLite (Dev)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Third-Party:** Cloudinary, FontAwesome

---

*Developed for Dipanchal Innovation Lab.*