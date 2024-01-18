import subprocess
import datetime

def check_ntpd_status():
    try:
        # Check if the ntpd service is active
        subprocess.check_call(['systemctl', 'is-active', '--quiet', 'ntpd'])
        return True  # Service is running
    except subprocess.CalledProcessError:
        return False  # Service is not running

def restart_ntpd():
    try:
        # Restart the ntpd service
        subprocess.check_call(['systemctl', 'restart', 'ntpd'])
        return True  # Restart successful
    except subprocess.CalledProcessError as e:
        print("Failed to restart ntpd: {}".format(e))
        return False  # Restart failed

def main():
    if not check_ntpd_status():
        # Log the current time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("/srv/ntpd-check/ntpd_restart.log", "a") as log_file:
            log_file.write("ntpd service is down at {}\n".format(current_time))

        # Restart the ntpd service
        if restart_ntpd():
            print("ntpd service restarted successfully.")
        else:
            print("Failed to restart ntpd service.")

if __name__ == "__main__":
    main()
