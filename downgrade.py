import subprocess
import os
import time

def run_adb_command(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode().strip()

def run_commands():
    # Prompt the user to enter the path to adb.exe
    adb_path = input("Enter the path to adb.exe - Nhập đường dẫn đến adb.exe: ")

    # Check if adb.exe exists at the specified path
    if not os.path.isfile(adb_path):
        print("adb.exe not found at the specified path - adb.exe không tồn tại ")
        return

    # Prompt the user to enter the package name
    package_name = input("Enter the package name - Nhập tên app: ")

    # Prompt the user to enter the APK name with version
    apk_name = input("Enter the downgrade APK name - Nhập tên file apk cần hạ cấp: ")

    # Prompt the user to enter the backup name
    backup_name = input("Enter the backup name - Nhập tên file backup: ")

    # Get the directory path of adb.exe
    adb_directory = os.path.dirname(adb_path)

    # Change directory to adb_directory
    os.chdir(adb_directory)

    # List connected devices
    cmd = "adb devices"
    output = run_adb_command(cmd)
    print("Connected devices - Kết nối thiết bị:")
    print(output)

    # Get the package path
    cmd = f"adb shell pm path {package_name}"
    package_path = run_adb_command(cmd)
    print("Package path - Tên path:")
    print(package_path)

    # Uninstall the package
    cmd = f"adb shell pm uninstall -k {package_name}"
    subprocess.call(cmd, shell=True)

    # Reboot the device
    cmd = "adb reboot"
    subprocess.call(cmd, shell=True)

    # Wait for 45 seconds
    time.sleep(45)

    # Check device connectivity again
    cmd = "adb devices"
    output = run_adb_command(cmd)
    print("Connected devices after reboot - Kiểm tra xem thiết bị kết nối chưa:")
    print(output)

    # Install the APK
    cmd = f"adb install {apk_name}"
    subprocess.call(cmd, shell=True)

    # Wait for another 45 seconds
    time.sleep(30)

    # Create a backup
    cmd = f"adb backup -f {backup_name}.ab {package_name}"
    subprocess.call(cmd, shell=True)

# Run the commands
run_commands()
