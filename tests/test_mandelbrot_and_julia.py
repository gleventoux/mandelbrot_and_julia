from pickle import FALSE
from mandelbrot_and_julia import utils


def test_is_in_mandelbrot():

    # c = 1+1j
    assert utils.is_in_mandelbrot(c=1+1j,max_iter=20) == False

    # c = 0.251
    assert utils.is_in_mandelbrot(c=0.251,max_iter=100) == True
    assert utils.is_in_mandelbrot(c=0.251,max_iter=200) == False