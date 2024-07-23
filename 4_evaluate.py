from benchmark.evaluate import eta
from benchmark.evaluate import explicit
from benchmark.evaluate import implicit
import os
# Compare this snippet from BIGbench/benchmark/evaluate/eta.py:

if __name__ == "__main__":
    model = "lcm" # can be changed
    align_path = f"./aligned/{model}"
    eta(align_path, model)
    print("eta finished")
    explicit(align_path, model)
    print("explicit finished")
    implicit(align_path, model)
    print("implicit finished")
