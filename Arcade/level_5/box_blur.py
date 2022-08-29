'''Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! 
You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. 
The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value
of the pixel values from the 3 x 3 square that has its center at x, including x itself. 

All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.'''

image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]

image_2 = [[7, 4, 0, 1],
           [5, 6, 2, 2],
           [6, 10, 7, 8],
           [1, 4, 2, 0]]

image_3 = [[36, 0, 18, 9],
           [27, 54, 9, 0],
           [81, 63, 72, 45]]


def solution(image):

    image_width = len(image[0])
    image_height = len(image)
    window_size = 3

    blurred_image = [x[:image_width - window_size + 1]
                     for x in image[:image_height - window_size + 1]]

    for row in range(image_width - window_size + 1):
        for col in range(image_height - window_size + 1):
            blurred_pixel = blur_pixel(image, row, col, window_size)
            blurred_image[col][row] = blurred_pixel

    return blurred_image


def blur_pixel(image, row, col, window_size):
    # left top pixel is used as reference
    blur_window = [x[row: row + window_size]
                   for x in image[col: col + window_size]]
    blur_window_flat = [t for s in blur_window for t in s]
    blurred_pixel = int(sum(blur_window_flat) / len(blur_window_flat))

    return blurred_pixel


print(solution(image_3))
