import os
import subprocess

def main():
    print("Starting GrowController with PHP...")

    # Find the path to the php executable
    php_executable = os.path.join(os.getcwd(), "php", "php.exe")
    if not os.path.exists(php_executable):
        print("Error: php executable not found. Please ensure the php folder is in the project root.")
        return

    # Set the Laravel public directory as the root
    public_dir = os.path.join(os.getcwd(), "growcontrol", "public")
    if not os.path.exists(public_dir):
        print("Error: Laravel public directory not found. Please ensure Laravel is installed correctly.")
        return

    # Start the PHP web server
    print("Starting PHP web server...")
    try:
        subprocess.check_call([php_executable, '-S', '0.0.0.0:8000', '-t', public_dir])
    except subprocess.CalledProcessError as e:
        print(f"Error starting PHP web server: {e}")
        return

if __name__ == "__main__":
    main()
