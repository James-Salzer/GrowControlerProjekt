import os
import subprocess

def main():
    print("Starting GrowController...")

    # Apply migrations
    print("Applying migrations...")
    try:
        subprocess.check_call(['python', 'manage.py', 'migrate'])
        print("Migrations applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error applying migrations: {e}")
        return

    # Start the development server
    print("Starting development server...")
    try:
        subprocess.check_call(['python', 'manage.py', 'runserver', '0.0.0.0:8000'])
    except subprocess.CalledProcessError as e:
        print(f"Error starting development server: {e}")
        return

if __name__ == "__main__":
    main()
