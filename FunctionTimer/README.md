## runtime_calculator
A Python module that can be used to find the runtime of a function or script.

### Import the module

```python
import runtime_calculator
```

### Find the runtime of a function

```python
@runtime_calculator.measure_runtime
def test():
    ...
    pass
```

### Find the runtime of a script

```python
runtime_calculator.measure_script_runtime()
```
> Should typically be used at the end of a script for accurate results.

### Example file and output
```python
# main.py
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
```

```plaintext
Function test took  1.01 seconds to run.
Function test2 took  3.01 seconds to run.
Function test3 took  2.01 seconds to run.
Script took  6.04 seconds to run.
```
