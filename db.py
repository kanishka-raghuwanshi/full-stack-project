import sqlite3
from pathlib import Path

DB_PATH = Path("site.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Projects table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            image_path TEXT
        )
        """
    )

    # Clients table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            designation TEXT NOT NULL,
            image_path TEXT
        )
        """
    )

    # Contacts (contact form submissions)
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            mobile TEXT NOT NULL,
            city TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # Newsletter subscriptions
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()


def seed_sample_data():
    """Insert sample projects and clients only if tables are empty."""
    conn = get_connection()
    cur = conn.cursor()

    # Seed projects if none
    cur.execute("SELECT COUNT(*) FROM projects")
    if cur.fetchone()[0] == 0:
        sample_projects = [
            (
                "Consultation",
                "Project Name, Location",
                "https://images.pexels.com/photos/885350/pexels-photo-885350.jpeg",
            ),
            (
                "Design",
                "Project Name, Location",
                "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg",
            ),
            (
                "Marketing & Design",
                "Project Name, Location",
                "https://images.pexels.com/photos/186077/pexels-photo-186077.jpeg",
            ),
            (
                "Consultation & Marketing",
                "Project Name, Location",
                "https://images.pexels.com/photos/1571463/pexels-photo-1571463.jpeg",
            ),
            (
                "Consultation",
                "Project Name, Location",
                "https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg",
            ),
        ]
        cur.executemany(
            "INSERT INTO projects (name, description, image_path) VALUES (?,?,?)",
            sample_projects,
        )

    # Seed clients if none
    cur.execute("SELECT COUNT(*) FROM clients")
    if cur.fetchone()[0] == 0:
        sample_clients = [
            (
                "Rowhan Smith",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "CEO, Foreclosure",
                "https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg",
            ),
            (
                "Shipra Kayak",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "Brand Designer",
                "https://images.pexels.com/photos/1181686/pexels-photo-1181686.jpeg",
            ),
            (
                "John Lepore",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "CEO, Foreclosure",
                "https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg",
            ),
            (
                "Marry Freeman",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "Marketing Manager at Mixit",
                "https://images.pexels.com/photos/1181519/pexels-photo-1181519.jpeg",
            ),
            (
                "Lucy",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "Sales Rep at Alibaba",
                "https://images.pexels.com/photos/1181579/pexels-photo-1181579.jpeg",
            ),
        ]
        cur.executemany(
            "INSERT INTO clients (name, description, designation, image_path) VALUES (?,?,?,?)",
            sample_clients,
        )

    conn.commit()
    conn.close()

