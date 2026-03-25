# =============================================
# FILE: config.py
# PURPOSE: Database connection configuration
# =============================================

import mysql.connector
from mysql.connector import Error

# Database configuration
# IMPORTANT: Change these values to match your MySQL setup
DB_CONFIG = {
    'host': 'localhost',           # MySQL server address
    'user': 'root',                 # MySQL username
    'password': '',    # ⚠️ CHANGE THIS to your MySQL password
    'database': 'internship_management',
    'port': 3306,                    # MySQL default port
    'raise_on_warnings': True
}

def get_connection():
    """
    Create and return a database connection
    This is the main function that connects frontend to backend
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("✅ Database connected successfully")
            return connection
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None

def test_connection():
    """Test if database connection works"""
    conn = get_connection()
    if conn:
        print("✅ Connection test successful!")
        conn.close()
        return True
    else:
        print("❌ Connection test failed!")
        return False

# Test connection when this file is run directly
# =============================================
# FILE: config.py
# PURPOSE: Database connection configuration
# =============================================

import mysql.connector
from mysql.connector import Error

# Database configuration
# IMPORTANT: Change these values to match your MySQL setup
DB_CONFIG = {
    'host': 'localhost',           # MySQL server address
    'user': 'root',                 # MySQL username
    'password': '',    # ⚠️ CHANGE THIS to your MySQL password
    'database': 'internship_management',
    'port': 3306,                    # MySQL default port
    'raise_on_warnings': True
}

def get_connection():
    """
    Create and return a database connection
    This is the main function that connects frontend to backend
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("✅ Database connected successfully")
            return connection
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None

def test_connection():
    """Test if database connection works"""
    conn = get_connection()
    if conn:
        print("✅ Connection test successful!")
        conn.close()
        return True
    else:
        print("❌ Connection test failed!")
        return False

# Test connection when this file is run directly
if __name__ == "_main_":
    print("Testing database connection...")
    test_connection()
    