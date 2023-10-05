import psutil

class PythonProcessManager:
    def __init__(self):
        pass

    def detect_running_python_scripts(self):
        python_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if 'python' in proc.info['name'].lower() or 'python3' in proc.info['name'].lower():
                    python_processes.append({'pid': proc.info['pid'], 'cmdline': ' '.join(proc.info['cmdline'])})
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return python_processes

    def kill_process_by_pid(self, pid):
        try:
            process = psutil.Process(pid)
            process.terminate()
        except psutil.NoSuchProcess:
            print(f"Process with PID {pid} not found.")
        except psutil.AccessDenied:
            print(f"Permission denied to terminate process with PID {pid}.")

    def log_running_scripts(self):
        running_scripts = self.detect_running_python_scripts()
        for script_info in running_scripts:
            print(f"PID: {script_info['pid']}, Command Line: {script_info['cmdline']}")


