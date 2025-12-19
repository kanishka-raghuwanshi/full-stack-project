Consultation, Development & Marketing – Landing Page & Admin Panel
This project is a full‑stack web application built with Streamlit, Python, and SQLite. It implements a marketing agency landing page and an admin panel as described in the Flipr full‑stack assignment.​

Features
Landing Page
Hero section with title, subtitle, CTA button, and banner image.

“Why Choose Us?” section with four feature cards (Expert Team, Quality Work, On‑Time Delivery, 24/7 Support).

“Our Projects” section showing project cards (image, name, description, Read More button).

“Happy Clients” section showing client testimonials (avatar image, description, name, designation).

Contact form (“Get a Free Consultation”) that saves:

Full Name

Email Address

Mobile Number

City

Newsletter subscription form in the top bar/footer that stores subscriber email addresses.​

Admin Panel
Protected by a simple login:

Username: admin

Password: admin123

Tabs inside the admin panel:

Projects

Add new projects (image upload, name, description).

View all stored projects.

Clients

Add new client testimonials (image upload, name, description, designation).

View all stored clients.

Contact Forms

View all contact form submissions stored in the database.

Subscriptions

View all newsletter subscriber emails.​

Database
Uses a single SQLite database file site.db.

Tables:

projects(id, name, description, image_path)

clients(id, name, description, designation, image_path)

contacts(id, full_name, email, mobile, city, created_at)

subscriptions(id, email, created_at)

Sample projects and clients are auto‑seeded into the database the first time the app runs so the landing page is not empty.

Tech Stack
Frontend & Backend: Streamlit (Python web framework)

Database: SQLite (sqlite3 standard Python library)

Other libraries:

Pillow (for image handling, if needed later)

Setup Instructions
1. Clone the repository
bash
git clone <your-repo-url>
cd <your-repo-folder>
2. Create and activate virtual environment
bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
3. Install dependencies
bash
pip install streamlit pillow
SQLite is included with Python, so no extra install is required.

4. Run the application
bash
streamlit run app.py
This will:

Create site.db and all tables (if not present).

Seed sample projects and clients if the tables are empty.

Open the URL shown in terminal (usually http://localhost:8501) in a browser.

Usage
Landing Page
Open the app; the default view is Landing Page.

Scroll to view hero, “Why Choose Us?”, projects, clients, contact form, and subscription form.

Submit the contact form; the data will appear in Admin Panel → Contact Forms.

Subscribe with an email; it will appear in Admin Panel → Subscriptions.​

Admin Panel
Use the sidebar dropdown Go to → Admin Panel.

Log in with admin / admin123.

Use the tabs:

Projects: Add project info and image; saved items will show both in the tab and on the landing page.

Clients: Add client testimonial with image and designation; they appear in the “Happy Clients” section.

Contact Forms: Review all consultation requests.

Subscriptions: Review all subscribed email addresses.

Project Structure
text
flipr_fullstack_task/
│
├── app.py        # Streamlit UI and app logic
├── db.py         # SQLite connection, table creation, and sample seeding
├── site.db       # Auto-generated SQLite database (ignored in VCS recommended)
├── venv/         # Virtual environment (ignored in VCS)
└── README.md

Future Improvements

Add edit/delete actions for projects and clients.

Implement stronger authentication (hashed passwords, multiple users).

Deploy app to a cloud platform (Streamlit Community Cloud, Render, etc.).