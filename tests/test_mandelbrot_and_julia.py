from pickle import FALSE
from mandelbrot_and_julia import utils


def test_is_in_mandelbrot():

    # Points intérieurs loin de la frontière
    assert utils.is_in_mandelbrot(c=-0.25,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=-0.6,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=-0.3+0.3j,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=-0.11+0.8j,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=-0.23+0.24j,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=0.24-0.26j,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=-1-0.1j,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=-0.51-0.56j,max_iter=20) == True

    # Points extérieurs loin de la frontière
    assert utils.is_in_mandelbrot(c=0.42-0.05j,max_iter=100) == False
    assert utils.is_in_mandelbrot(c=0.51-0.38j,max_iter=100) == False
    assert utils.is_in_mandelbrot(c=0.20-0.73j,max_iter=100) == False
    assert utils.is_in_mandelbrot(c=-0.44-0.79j,max_iter=100) == False
    assert utils.is_in_mandelbrot(c=-0.80-0.30j,max_iter=100) == False
    assert utils.is_in_mandelbrot(c=-1.48+0.25j,max_iter=100) == False
    assert utils.is_in_mandelbrot(c=-0.83+0.54j,max_iter=100) == False

    # Points extérieurs proche de la frontière
    assert utils.is_in_mandelbrot(c=0.345861297-0.081431768j,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=0.345861297-0.081431768j,max_iter=50) == True
    assert utils.is_in_mandelbrot(c=0.345861297-0.081431768j,max_iter=100) == True
    assert utils.is_in_mandelbrot(c=0.345861297-0.081431768j,max_iter=200) == True
    assert utils.is_in_mandelbrot(c=0.345861297-0.081431768j,max_iter=400) == False

    assert utils.is_in_mandelbrot(c=0.368232662-0.302460851j,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=0.368232662-0.302460851j,max_iter=50) == True
    assert utils.is_in_mandelbrot(c=0.368232662-0.302460851j,max_iter=100) == True
    assert utils.is_in_mandelbrot(c=0.368232662-0.302460851j,max_iter=200) == True
    assert utils.is_in_mandelbrot(c=0.368232662-0.302460851j,max_iter=400) == False

    assert utils.is_in_mandelbrot(c=0.06935123-0.620134229j,max_iter=20) == True
    assert utils.is_in_mandelbrot(c=0.06935123-0.620134229j,max_iter=50) == True
    assert utils.is_in_mandelbrot(c=0.06935123-0.620134229j,max_iter=100) == True
    assert utils.is_in_mandelbrot(c=0.06935123-0.620134229j,max_iter=200) == False

def test_is_in_julia():

    # c = -0.8 + 0.156j

    # Points intérieurs loin de la frontière
    assert utils.is_in_julia(c=-0.8+0.156j,z0=-0.8390625+0.290624j,max_iter=20) == True
    assert utils.is_in_julia(c=-0.8+0.156j,z0=-0.1125+0.243749j,max_iter=20) == True
    assert utils.is_in_julia(c=-0.8+0.156j,z0=-0.871875-0.262499j,max_iter=20) == True

    # Points intérieurs loin de la frontière
    assert utils.is_in_julia(c=-0.8+0.156j,z0=-0.707812+0.098437j,max_iter=20) == False
    assert utils.is_in_julia(c=-0.8+0.156j,z0=-0.239062+0.074999j,max_iter=20) == False
    assert utils.is_in_julia(c=-0.8+0.156j,z0=0.459375+0.290624j,max_iter=20) == False
