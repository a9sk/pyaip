import subprocess
import sys
import os

def install_packages():
    # ensure requirements.txt exists
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if not os.path.isfile(requirements_path):
        print(f"Error: {requirements_path} not found.")
        return
    
    # install the packages
    try:
        print("Installing packages from requirements.txt...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])
        print("All packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")

if __name__ == "__main__":
    install_packages()
