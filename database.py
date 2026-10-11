import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "object_detection_db"))

def init_db():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS detection_events (
            id INT AUTO_INCREMENT PRIMARY KEY,
            image_name VARCHAR(255) NOT NULL,
            object_name VARCHAR(100) NOT NULL,
            confidence DECIMAL(6,5) NOT NULL,
            detected_at DATETIME NOT NULL)""")
        conn.commit()
        cur.close()
    finally:
        conn.close()

def log_detection(image_name, object_name, confidence, detected_at):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO detection_events (image_name, object_name, confidence, detected_at) VALUES (%s,%s,%s,%s)",
                    (image_name, object_name, confidence, detected_at.strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        cur.close()
    finally:
        conn.close()
