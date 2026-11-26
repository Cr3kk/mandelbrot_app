import numpy as np

# i once again stole most of this code from a guy on the internet and then applied it to what i have, so idrk what this does

def count_to_image(input_array, max_iter):
    height, width = input_array.shape
    
    is_odd = (input_array % 2) == 1
    
    color = np.zeros((height, width, 3), dtype=np.uint8) # starts all pixels at value 0 (black i guess)
    color[is_odd] = 255 # odd numbers get 255 (white)
    
    header = f"P6\n{width} {height}\n255\n".encode()
    return header + color.tobytes()