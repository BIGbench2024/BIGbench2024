import benchmark

if __name__ == "__main__":
    model = "./data/workflow/lcm_sdxl.json" # can be changed
    iterations = 1 # can be changed
    data_path="./data/"
    ip = "http://127.0.0.1:8190/prompt"
    for i in range(iterations):
        benchmark.generate_image(model, ip, data_path)