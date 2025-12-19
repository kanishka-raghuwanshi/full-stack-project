import streamlit as st
from PIL import Image

from db import init_db, get_connection, seed_sample_data


# ---------- INITIAL SETUP ----------
init_db()
seed_sample_data()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.set_page_config(page_title="Consultation, Development & Marketing", layout="wide")

# ---------- GLOBAL CSS ----------
page_bg_img = """
<style>
/* App background: simple light gray */
[data-testid="stAppViewContainer"] {
    background: #f5f6fa;
}

/* Main content card */
[data-testid="stMainBlockContainer"] {
    background: #ffffff;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}

/* Sidebar background and text */
section[data-testid="stSidebar"] {
    background-color: #0f4c81 !important;
}
section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* Selectbox styling in sidebar */
section[data-testid="stSidebar"] .stSelectbox label {
    color: #ffffff !important;
}
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
    background-color: #0f4c81 !important;
    color: #ffffff !important;
    border-radius: 6px !important;
    border: 1px solid #ffffff55 !important;
}
section[data-testid="stSidebar"] .stSelectbox div[role="listbox"] {
    background-color: #0f4c81 !important;
    color: #ffffff !important;
}

/* Hide default top header background */
header[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0) !important;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)




button_css = """
<style>
div.stButton > button {
    background-color: #ff7a30;
    color: white;
    border-radius: 6px;
    padding: 0.5rem 1.5rem;
    border: none;
    font-weight: 600;
}
div.stButton > button:hover {
    background-color: #ff944f;
}

button[kind="formSubmit"] {
    background-color: #ff7a30 !important;
    color: white !important;
    border-radius: 6px !important;
    border: none !important;
    font-weight: 600 !important;
}

h1, h2, h3 {
    color: #12355b;
    font-family: 'Segoe UI', sans-serif;
}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)

# ---------- SIDEBAR NAV ----------
page = st.sidebar.selectbox(
    "Go to",
    ["Landing Page", "Admin Panel"]
)

# ---------- HELPER FUNCTIONS ----------
def save_resized_image(uploaded_file, prefix, size=(450, 350)):
    """Resize/crop uploaded image and save to disk. Returns saved path."""
    image = Image.open(uploaded_file).convert("RGB")
    image = image.resize(size, Image.Resampling.LANCZOS)

    filename = f"{prefix}_{uploaded_file.name}"
    image.save(filename, format="JPEG", quality=90)
    return filename

def fetch_projects():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_clients():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_contact(full_name, email, mobile, city):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (full_name, email, mobile, city) VALUES (?,?,?,?)",
        (full_name, email, mobile, city),
    )
    conn.commit()
    conn.close()

def insert_subscription(email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO subscriptions (email) VALUES (?)",
        (email,),
    )
    conn.commit()
    conn.close()

def admin_login():
    st.subheader("Admin Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Logged in successfully.")
        else:
            st.error("Invalid username or password.")

def insert_project(name, description, image_path):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO projects (name, description, image_path) VALUES (?,?,?)",
        (name, description, image_path),
    )
    conn.commit()
    conn.close()

def insert_client(name, description, designation, image_path):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO clients (name, description, designation, image_path) VALUES (?,?,?,?)",
        (name, description, designation, image_path),
    )
    conn.commit()
    conn.close()

def fetch_contacts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_subscriptions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM subscriptions ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

# ---------- PAGES ----------

# Landing Page
if page == "Landing Page":
    # HERO SECTION
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(
            "<h1 style='font-size:48px;'>Consultation, Development & Marketing</h1>",
            unsafe_allow_html=True,
        )
        st.write(
            "We help businesses grow with our expert consultation, innovative development solutions, and strategic marketing services."
        )
        st.button("Get Started")
    with col2:
        st.image("https://images.pexels.com/photos/1181376/pexels-photo-1181376.jpeg",
                 caption="Team at work")

    st.markdown("---")

    # WHY CHOOSE US
    st.subheader("Why Choose Us?")
    wcols = st.columns(4)
    features = [
        ("Expert Team", "Skilled professionals with years of experience."),
        ("Quality Work", "High-quality deliverables that exceed expectations."),
        ("On-Time Delivery", "We respect deadlines and deliver on time."),
        ("24/7 Support", "Responsive support whenever you need it."),
    ]
    for col, (title, desc) in zip(wcols, features):
        with col:
            st.markdown("✅")
            st.markdown(f"**{title}**")
            st.write(desc)

    st.markdown("---")

    # OUR PROJECTS
    st.subheader("Our Projects")
    projects = fetch_projects()
    if projects:
        pcols = st.columns(3)
        for i, proj in enumerate(projects):
            with pcols[i % 3]:
                if proj["image_path"]:
                    st.image(proj["image_path"], use_column_width=True)
                st.markdown(f"**{proj['name']}**")
                st.write(proj["description"])
                st.button("Read More", key=f"read_{proj['id']}")
    else:
        st.info("No projects added yet.")

    st.markdown("---")

    # HAPPY CLIENTS
    st.subheader("Happy Clients")
    clients = fetch_clients()
    if clients:
        ccols = st.columns(3)
        for i, client in enumerate(clients):
            with ccols[i % 3]:
                if client["image_path"]:
                    st.image(client["image_path"], width=80)
                st.write(client["description"])
                st.markdown(f"**{client['name']}**")
                st.caption(client["designation"])
    else:
        st.info("No clients added yet.")

    st.markdown("---")

    # CONTACT FORM
    st.subheader("Get a Free Consultation")
    with st.container():
        with st.form("contact_form"):
            full_name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            mobile = st.text_input("Mobile Number")
            city = st.text_input("Area, City")
            submitted = st.form_submit_button("Get Quick Quote")
            if submitted:
                if full_name and email and mobile and city:
                    insert_contact(full_name, email, mobile, city)
                    st.success("Thank you! We will contact you soon.")
                else:
                    st.error("Please fill all fields.")

    st.markdown("---")

    # NEWSLETTER
    st.subheader("Subscribe Us")
    with st.container():
        with st.form("newsletter_form"):
            sub_email = st.text_input("Enter Email Address")
            sub_btn = st.form_submit_button("Subscribe")
            if sub_btn:
                if sub_email:
                    insert_subscription(sub_email)
                    st.success("Subscribed successfully!")
                else:
                    st.error("Please enter your email.")

# Admin Panel
elif page == "Admin Panel":
    if not st.session_state.logged_in:
        admin_login()
    else:
        st.title("Admin Panel")

        tabs = st.tabs(["Projects", "Clients", "Contact Forms", "Subscriptions"])

        # ---------- Projects tab ----------
        with tabs[0]:
            st.subheader("Add New Project")
            with st.form("add_project_form"):
                p_image = st.file_uploader("Project Image", type=["png", "jpg", "jpeg"])
                p_name = st.text_input("Project Name")
                p_desc = st.text_area("Project Description")
                p_submit = st.form_submit_button("Add Project")

            if p_submit:
                img_path = None
                if p_image is not None:
                 img_path = save_resized_image(p_image, "proj", size=(450, 350))

                if p_name and p_desc:
                    insert_project(p_name, p_desc, img_path)
                    st.success("Project added.")
                else:
                    st.error("Please fill project name and description.")

            st.markdown("### All Projects")
            for proj in fetch_projects():
                st.write(f"**{proj['name']}** - {proj['description']}")

        # ---------- Clients tab ----------
        with tabs[1]:
            st.subheader("Add New Client")
            with st.form("add_client_form"):
                c_image = st.file_uploader("Client Image", type=["png", "jpg", "jpeg"])
                c_name = st.text_input("Client Name")
                c_desc = st.text_area("Client Testimonial / Description")
                c_desig = st.text_input("Client Designation (e.g., CEO, Designer)")
                c_submit = st.form_submit_button("Add Client")

            if c_submit:
               img_path = None
               if c_image is not None:
                 img_path = save_resized_image(c_image, "client", size=(150, 150))

                 if c_name and c_desc and c_desig:
                    insert_client(c_name, c_desc, c_desig, img_path)
                    st.success("Client added.")
                 else:
                    st.error("Please fill all client fields.")

            st.markdown("### All Clients")
            for client in fetch_clients():
                st.write(f"**{client['name']}** - {client['designation']}")

        # ---------- Contact Forms tab ----------
        with tabs[2]:
            st.subheader("Contact Form Submissions")
            contacts = fetch_contacts()
            if contacts:
                st.table(contacts)
            else:
                st.info("No contact form submissions yet.")

        # ---------- Subscriptions tab ----------
        with tabs[3]:
            st.subheader("Email Subscriptions")
            subs = fetch_subscriptions()
            if subs:
                st.table(subs)
            else:
                st.info("No email subscriptions yet.")
