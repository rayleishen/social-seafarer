import subprocess
import time


main_script_path = "socialseafarer.py"


while True:
    time.sleep(1)
    try:
        # Start the main script
        subprocess.run(["python", main_script_path])
        print("social seafarer started")
    except Exception as e:
        print(f"Main script crashed: {e}")
        print("Restarting in 5 seconds...")
        time.sleep(5)