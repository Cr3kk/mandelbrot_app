import numpy as np


# the code at the bottom was my first attempt at making the code, but because of inefficient memory usage with how i define the lists, 
# and because it relied on 2 different loops of both O(n^2), at longer iterations and smaller scales, it took painfully long for it to render the image,
# like up to 2 minutes for more detailed zoomed in images. 
# this was unacceptable if we wanted a smooth running app, especially because at the time of me writing this we still need to implement the click to zoom. 
# So i decided to go back and try to use numpy, which i heard from people was a faster and better way to implement most math in python. 
# So with a lot of braindead staring at documentation, pretending i understand it, and just a little bit of begging claude to explain the bugs, 
# here is a hopefully better mandelbrot implementation

# the current implementation is to rather than run the function for every element in the grid individally before moving to the next one, running 250.000 times,
# i create the whole grid and run the function over the whole

# code after refactor
def calculate_mandolbrot_set(x, y, scale, max_iter):
    value_range = np.arange(500) # creates a list for each pixel in the canvas size, which is hardcoded here, im too lazy to fix a variable to it
    zerod_range = (value_range - 250) * scale # puts the start in the top left point, does what def calc_zero_zero() used to do
    
    # creates two lists filled with 500 by 500 values equal to 1, as the starting grid
    x_list, y_list = np.meshgrid(x + zerod_range, y - zerod_range)
    # see the obsolete calculate_mandolbrot_number function, this is what replaces the original a and b definition as the real and imaginairy parts of the set 
    # man fuck imaginariy functions, i had to watch a 30 minute video just to know wtf is going on, luckily 3blue1brown has a good video on this
    a = np.zeros_like(x_list) # real part
    b = np.zeros_like(y_list) # imaginairy part
    
    output_array = np.zeros(x_list.shape) # what will eventually be given as a return, replaces the counter in the bottom function of the old code
    oob_tracker = np.ones(x_list.shape, dtype=bool) # tracks whether or not each pixel is within the distance < 2 requirement of the original function and exercise (oob = Out Of Bounds)

    for i in range(max_iter):
        # applies the function over a whole part, a being real and b being imaginairy, which i learned is possible today, gets rid of one for loop
        f_a = (a*a - b*b + x_list)
        f_b = (2*a*b + y_list)
        
        a = np.where(oob_tracker, f_a, a) # sets a to f_a, so with the funciton applied, unless the pixel is already out of bounds, then it just stays at a
        b = np.where(oob_tracker, f_b, b)
        
        # TODO maybe replace the wierd inversion with a ! and not function and false rather than true
        oob = oob_tracker & (a*a + b*b > 4) # does the same as the d (distance), but rather than preventing a new loop from forming, it just puts the oob_tracker to TODO:True for that pixel, which comes back in the two lines above this one, to prevent it from being updated
        output_array[oob] = i # this is the magic of the mandolbrot number. It gets the current iteration we are on (here i, from the for loop, replaces the counter in the old function), and stores it in the output array when the number goes oob there
        oob_tracker &= ~oob 
        
        if not oob_tracker.any(): # forces out of the loop if all elements in the current array went out of bounds
            break
        
    output_array[oob_tracker] = max_iter # some elements (most) might remain TODO:True at the end here, so we give it the max iterations value
    return output_array
        
        


# code before refactor
#def calculate_mandolbrot_set(x, y, scale, max_iter):
#    x_start, y_start = calc_zero_zero(x, y, scale)
#    x_list = [x_start + (i * scale) for i in range(0, 500)]
#    y_list = [y_start - (i * scale) for i in range(0, 500)]
#
#    return_list = []
#    
#    for i in y_list:
#        internal_list = []
#        for j in x_list:
#            internal_number = calculate_mandolbrot_number(j, i, max_iter)
#            internal_list.append(internal_number)
#        return_list.append(internal_list)
#    return return_list
#     
#def calc_zero_zero(x, y, scale):
#    x_zero = x - (250 * scale) 
#    y_zero = y + (250 * scale) 
#    return x_zero, y_zero


# this is from a different file that i used to use for it, kinda pointless with hindsight, but it used to look clean and makes for easy comparison to the new code
# from math import sqrt

#def calculate_mandolbrot_number(x, y, max_iter):
#    distance = 0
#    counter = 0
#    a = 0
#    b = 0
#    while distance < 2:
#        f_a = (a*a - b*b + x)
#        f_b = (2 * a * b + y)
#        counter += 1
#    
#        a = f_a
#        b = f_b
#        
#        distance = sqrt(a**2 + b**2)
#        if counter == max_iter:
#            break
#   if counter % 2 == 0:
#        return "black"
#    elif counter % 2 == 1:
#        return "white"
    

    