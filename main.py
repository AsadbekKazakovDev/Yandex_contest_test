import random

for i in range(1, 51):
    in_file = f"{i:02d}"
    out_file = f"{i:02d}.a"
    
    with open(in_file, "w") as input_file, open(out_file, "w") as output_file:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        input_file.write(f"{a} {b}\n")
        output_file.write(str(a + b))
