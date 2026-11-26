from .mandol_number import calculate_mandolbrot_number

def calculate_mandolbrot_set(x, y, scale, max_iter):
    x_start, y_start = calc_zero_zero(x, y, scale)
    x_list = [x_start + (i * scale) for i in range(0, 501)]
    y_list = [y_start - (i * scale) for i in range(0, 501)]

    return_list = []
    
    for i in y_list:
        internal_list = []
        for j in x_list:
            internal_number = calculate_mandolbrot_number(j, i, max_iter)
            internal_list.append(internal_number)
        return_list.append(internal_list)
    return return_list
     
def calc_zero_zero(x, y, scale):
    x_zero = x - (250 * scale) 
    y_zero = y + (250 * scale) 
    return x_zero, y_zero
