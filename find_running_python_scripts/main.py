from process_manager import PythonProcessManager

if __name__ == "__main__":
    manager = PythonProcessManager()
    
    running_scripts = manager.detect_running_python_scripts()
    print("Running Python Scripts:")
    for script in running_scripts:
        print(f"PID: {script['pid']}, Command Line: {script['cmdline']}")

    pid_to_kill = int(input("Enter PID to kill a process (0 to skip): "))
    if pid_to_kill != 0:
        manager.kill_process_by_pid(pid_to_kill)

    print("\nLogging Running Scripts:")
    manager.log_running_scripts()