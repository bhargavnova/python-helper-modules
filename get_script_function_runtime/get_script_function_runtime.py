import time

class runtime_calculator:
    def __init__(self):
        self.timer_start = None
        # This is used to measure the runtime of the script
        self.script_timer_start = time.time()

    def start(self):
        """Start measuring the runtime of a function."""
        self.timer_start = time.time()
        
    def stop(self):
        """Stop measuring the runtime of a function."""
        runtime = time.time() - self.timer_start
        return runtime
    
    def stop_script(self):
        """Stop measuring the runtime of the script."""
        script_runtime = time.time() - self.script_timer_start
        self.script_timer_start = None
        return script_runtime


calculator = runtime_calculator()

def measure_runtime(func):
    """A decorator function that measures the runtime of a given function"""
    def wrapper(*args, **kwargs):
        calculator.start()
        result = func(*args, **kwargs)
        runtime = calculator.stop()
        print(f"Function {func.__name__} took {runtime: .2f} seconds to run.")
        return result
    return wrapper

def measure_script_runtime():
    runtime = calculator.stop_script()
    print(f"Script took {runtime: .2f} seconds to run.")