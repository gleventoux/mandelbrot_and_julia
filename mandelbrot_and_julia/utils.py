from PIL import Image
import numpy as np


def suite(z,c)-> complex:
    """Générateur des éléments de la suite $z_{n+1}=z_n^2+c$
    
    c.f. Chapitre 2"""
    while True:
        yield z
        z = z ** 2 + c

def suite_mandelbrot(c)-> bool:
    """Renvoie la suite de Mandelbrot"""
    return suite(0,c)

def suite_julia(z,c)-> bool:
    """Renvoie la suite de julia pour candidat et parametre"""

    return suite(z,c)

def is_in_mandelbrot(c,max_iter=50,threshold=1000):

    """
    Verify experimentally if the given complex candidate belongs to the Mandelbrot set.

    Parameters
    ----------
    c : complex
        The candidate
    max_iter : int, optional
        The number of terms of the Mandelbrot sequence to assume this one is bounded
    threshold : float, optional
        Radius of the disk within which computed terms must all be to consider the Mandelbrot sequence as bounded

    Returns
    -------
    bool
        True if candate is in the Mandelbrot set, False otherwise.
    """
    
    if abs(c) > 2:
        return False

    else:
        s = suite_mandelbrot(c)
        for _ in range(max_iter):
            if abs(next(s)) >= threshold:
                return False
        return True
    
def is_in_julia(z0,c,max_iter=50):
    
    """
    Verify experimentally if the complexe candidate z0 belongs to the Julia set for a given c .

    Parameters
    ----------
    z0 : complex
        Initial terme of the Julia sequence
    c : complex
        The given parameter for the Julia sequence
    max_iter : int, optional
        The number of terms of the Mandelbrot sequence to assume this one is bounded
    threshold : float, optional
        Radius of the disk within which computed terms must all be to consider the Mandelbrot sequence as bounded

    Returns
    -------
    bool
        True if candate is in the Julia set for the given c, False otherwise.
    """

    s = suite_julia(z0,c)
    for _ in range(max_iter):
        if abs(next(s)) >= 2:
            return False
    return True

def plot_mandelbrot(zmin=-2-1j, zmax=1+1j, pixel_size=1e-2, max_iter=20, figname="Mandelbrot.png"):
    
    """
    Plot and save the Mandelbrot set.

    Parameters
    ----------
    zmin : complex, optional
        Lower left corner of the plotting window
    zmax : complex, optional
        Upper right corner of the plotting window
    pixel_size : float, optional
        Size of the pixel
    max_iter : int, optional
        The number of terms of the Mandelbrot sequence to assume this one is bounded
    figname : string, optional
        Save file name with extension

    """

    width = zmax.real - zmin.real
    height = zmax.imag - zmin.imag
    if width <= 0 or height <= 0:
        print("Window empty !")
    else:
        nx = int(width/pixel_size)
        ny = int(height/pixel_size)
        a = np.full((ny,nx),True)
        z0 = complex(zmin.real,zmax.imag)
        dx = width/nx
        dy = height/ny
        for i in range(ny):
            for j in range(nx):
                c = z0 + complex((j+0.5)*dx,0) - complex(0,(i+0.5)*dy)
                if is_in_mandelbrot(c,max_iter=max_iter):
                    a[i][j] = False
        im = Image.fromarray(a)
        im.save('output/'+figname)

def plot_julia(c=0.8+0.156j, zmin=-1-1j, zmax=1+1j, pixel_size=1e-2, max_iter=20, figname="Julia.png"):
    
    """
    Plot and save the Julia set for a given c.

    Parameters
    ----------
    c : complex, optional
        Julia sequence parameter
    zmin : complex, optional
        Lower left corner of the plotting window
    zmax : complex, optional
        Upper right corner of the plotting window
    pixel_size : float, optional
        Size of the pixel
    max_iter : int, optional
        The number of terms of the Mandelbrot sequence to assume this one is bounded
    figname : string, optional
        Save file name with extension

    """

    width = zmax.real - zmin.real
    height = zmax.imag - zmin.imag
    if width <= 0 or height <= 0:
        print("Window empty !")
    else:
        nx = int(width/pixel_size)
        ny = int(height/pixel_size)
        a = np.full((ny,nx),True)
        z0 = complex(zmin.real,zmax.imag)
        dx = width/nx
        dy = height/ny
        for i in range(ny):
            for j in range(nx):
                z = z0 + complex((j+0.5)*dx,0) - complex(0,(i+0.5)*dy)
                if is_in_julia(z,c,max_iter=max_iter):
                    a[i][j] = False
        im = Image.fromarray(a)

        # set save file's path
        im.save('output/'+figname)
