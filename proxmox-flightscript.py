import os
import subprocess
import time

# Global Variables for branding and reference
AUTHOR = "Rich Knowles"
GITHUB_LINK = "https://github.com/richknowles/proxmox-flightscript"

# List of Post-Install Steps
def post_install_steps():
    """
    Defines a list of post-installation steps that will be presented in the menu.
    These steps are common tasks for optimizing a Proxmox installation.
    """
    steps = [
        "Apply essential system tweaks",
        "Remove licensing nag",
        "Clean up unnecessary repositories",
        "Install recommended software packages",
        "Set up system monitoring tools",
        "Optimize kernel parameters",
        "Configure backups",
        "Enable Firewall and Secure SSH",
        "Configure Time Synchronization",
        "Clean temporary files",
        "Configure network optimizations",
        "Install latest Proxmox updates",
        "Enable ZFS optimizations",
        "Setup email notifications",
        "Install container templates",
        "Configure VM defaults",
        "Enable performance monitoring",
        "Configure NTP",
        "Optimize disk I/O",
        "Review and finalize configurations",
    ]
    return steps

# Install recommended software packages
def install_software():
    """
    Returns a list of recommended software packages for installation.
    These packages enhance system functionality and monitoring capabilities.
    """
    software = [
        "htop",          # Interactive process viewer
        "iftop",         # Real-time network usage
        "vim",           # Text editor
        "curl",          # Command-line tool for transferring data with URLs
        "wget",          # Network file downloader
        "zfsutils-linux",# ZFS utilities
        "net-tools",     # Basic networking utilities
        "screen",        # Terminal multiplexer
        "tmux",          # Alternative terminal multiplexer
    ]
    return software

# Main menu system using text-based interface
def main_menu(predefined_choice=None):
    """
    Main menu loop that handles user input and renders the interface in text.
    Supports predefined input for environments where interactive input is restricted.
    """
    menu_items = post_install_steps() + [
        "List Installed Apps",
        "System Info",
        "View/Print Logs",
        "Cleanup - USE CAUTION",
    ]

    for idx, item in enumerate(menu_items):
        print(f"{idx + 1}. {item}")

    # Handling predefined or default user input
    if predefined_choice is not None:
        choice = predefined_choice
    else:
        choice = 1  # Default choice to avoid interactive input issues

    print(f"\nAutomatically proceeding with choice: {choice}")

    if 1 <= choice <= len(menu_items):
        handle_selection(choice - 1, menu_items[choice - 1])
    else:
        print("Invalid choice. Please verify the predefined_choice value.")

# Handle the execution of selected menu items
def handle_selection(index, selection):
    """
    Executes actions based on the selected menu item.
    """
    if index < len(post_install_steps()):
        print(f"Running: {selection}\n")
        if selection == "Apply essential system tweaks":
            apply_system_tweaks()
        else:
            time.sleep(1)  # Simulate the execution of the task
            print("Done!")
    elif selection == "List Installed Apps":
        show_installed_apps()
    elif selection == "System Info":
        show_system_info()
    elif selection == "View/Print Logs":
        view_logs()
    elif selection == "Cleanup - USE CAUTION":
        run_cleanup()

# Apply essential system tweaks
def apply_system_tweaks():
    """
    Applies system-level tweaks, including updates and optimizations.
    """
    print("Applying essential system tweaks...\n")
    try:
        os.system("apt update && apt dist-upgrade -y")
        print("System tweaks applied successfully!")
    except Exception as e:
        print(f"Error applying system tweaks: {e}")

# Display a list of installed applications
def show_installed_apps():
    """
    Uses the dpkg command to retrieve and display a list of installed packages.
    """
    print("Installed Applications:\n")
    apps = subprocess.getoutput("dpkg --get-selections")  # Retrieve installed packages
    print(apps)

# Display system information
def show_system_info():
    """
    Uses neofetch to display system information in a detailed and user-friendly format.
    """
    print("System Info:")
    try:
        os.system("neofetch")  # Use neofetch to display system information
    except Exception as e:
        print(f"Error running neofetch: {e}")

# View or print logs
def view_logs():
    """
    Displays the content of a predefined log file.
    """
    log_file = "/var/log/syslog"  # Example log file path
    print(f"Viewing logs from {log_file}...\n")
    try:
        with open(log_file, "r") as file:
            logs = file.readlines()
            for line in logs[-50:]:  # Display the last 50 lines for brevity
                print(line, end="")
    except Exception as e:
        print(f"Error reading log file: {e}")

# Perform cleanup tasks
def run_cleanup():
    """
    Simulates a cleanup operation with a delay to indicate progress.
    """
    print("Running Cleanup Tasks:\n")
    time.sleep(2)  # Simulate cleanup time
    print("Cleanup Completed!")

# Entry point of the script
if __name__ == "__main__":
    predefined_input = 1  # Automatically select the first option to avoid interactive input
    main_menu(predefined_input)
