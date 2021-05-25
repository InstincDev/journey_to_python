"""
This program generates the Warhol effect based on the original image.
"""
import random
from simpleimage import SimpleImage

N_ROWS = 4
N_COLS = 4
PATCH_SIZE = 220
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE

PATCH_NAME = ['prof_mehran.jpg', 'chris_piech.jpg', 'julie_2.jpeg']

def main():
    play_level3()

def play_level3():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for x in range(N_COLS):
        for y in range(N_ROWS):
            patch = make_recolored_patch(random.random()*2.5,random.random()*1.5,random.random()*1.5)
            put_patches(final_image, x, y, patch)
    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    x = random.randint(0,len(PATCH_NAME)-1)
    patch = SimpleImage(PATCH_NAME[x])
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

def put_patches(final_image, x, y, patch):
    start_x = x * PATCH_SIZE
    start_y = y * PATCH_SIZE
    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            px = patch.get_pixel(x,y)
            final_image.set_pixel(x + start_x, y + start_y, px)
            



if __name__ == '__main__':
    main()