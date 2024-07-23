from benchmark.generate import dir_build
from benchmark.internViT_pkg import process_all_subdirs_multi
import os
import torchvision
import transformers

def align(model_path, output_path):
    process_all_subdirs_multi(model_path, output_path,1)

if __name__ == "__main__":
    model = "lcm" # the model name
    image_path = f"./arranged/{model}"
    output_path = f"./aligned/{model}" # the alignment output path
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    process_all_subdirs_multi(image_path, output_path, model)
    print("finished")