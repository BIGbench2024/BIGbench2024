from benchmark.generate import dir_build
import os

if __name__ == "__main__":
    model = "lcm" # the model name
    source_path = "your/T2I_model/output/path" # the result of generation
    target_path = f"./arranged/{model}" # the place to store
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    dir_build(source_path, target_path)