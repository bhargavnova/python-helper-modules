import runtime_calculator
import time

@runtime_calculator.measure_runtime
def test():
    ...
    pass

@runtime_calculator.measure_runtime
def test2():
    time.sleep(3)

test()
test2()

@runtime_calculator.measure_runtime
def test3():
    time.sleep(2)

test3()

if __name__ == "__main__":
    runtime_calculator.measure_script_runtime()