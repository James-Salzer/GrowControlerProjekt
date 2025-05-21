import sqlite3

DATABASE_NAME = "app_database.db"

def initialize_database():
    """
    Initializes the SQLite database and creates necessary tables.
    If the database or tables already exist, it will not recreate them.
    """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create SensorReadings table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS SensorReadings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temperature REAL,
            humidity REAL,
            sensor_name TEXT
        )
        """)

        # Create RelayStates table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS RelayStates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            relay_name TEXT,
            state TEXT CHECK(state IN ('ON', 'OFF'))
        )
        """)

        conn.commit()
        print(f"Database '{DATABASE_NAME}' initialized successfully.")
        print("Tables created: SensorReadings, RelayStates (if they didn't exist).")

    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    initialize_database()
