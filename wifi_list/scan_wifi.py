import subprocess
import datetime
import os

def main():
    
    # Automatically determine current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(f"Current date: {current_date} {current_time}")

    # Prompt user for location name
    location_name = input("Enter location name (e.g. Ueno_Starbucks): ")

    # Make name variable for file name
    filename = f"{location_name}_{current_date}_{current_time}.txt"

    # Run linux command and save output to file
    command = "nmcli dev wifi list"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Save file in same folder as script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    with open(file_path, 'w') as file:
        file.write(result.stdout)

    print(f"Current Wi-Fi networks list saved to {file_path}")

if __name__ == "__main__":
    main()
