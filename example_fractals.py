
from netpbm import ImgColor
from random import randint


image = ImgColor(640, 480)


# Fractals
_sierpinski_triangle = [[1, 0], \
                        [1, 1]]

_sierpinski_square = [[1, 1, 1], \
                      [1, 0, 1], \
                      [1, 1, 1]]

_vicsek = [[1, 0, 1], \
           [0, 1, 0], \
           [1, 0, 1]]

_snowflake = [[1, 1, 0], \
              [1, 0, 1], \
              [0, 1, 1]]

_hexaflake = [[1, 1, 0], \
              [1, 1, 1], \
              [0, 1, 1]]

_spiral = [[0, 0, 1, 1, 0], \
           [1, 0, 1, 0, 0], \
           [1, 1, 1, 1, 1], \
           [0, 0, 1, 0, 1], \
           [0, 1, 1, 0, 0]]

bm = _sierpinski_square
nx = len(bm[0])
ny = len(bm)


def bmf(x0, y0, x1, y1):
    global image, bm, nx, ny
    xd = x1-x0
    yd = y1-y0
    if xd < 2 and yd < 2:
        image.set_pixel(int(x0), int(y0), (randint(0, 255), randint(0, 255), randint(0, 255)))
        return
    for i in range(ny):
        for k in range(nx):
            if bm[i][k] > 0:
                bmf(x0+xd*k/nx, y0+yd*i/ny, x0+xd*(k+1)/nx, y0+yd*(i+1)/ny)


bmf(0, 0, image.width - 1, image.height - 1)
# image.reverse()
image.to_file("fractal")
