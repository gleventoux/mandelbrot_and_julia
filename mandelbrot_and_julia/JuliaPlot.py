import argparse
from mandelbrot_and_julia.utils import plot_julia

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-c','--candidate',metavar='candidate',type=complex,default=0.8+0.156j)
    parser.add_argument('--zmin',metavar='zmin',type=complex,default=-1-1j)
    parser.add_argument('--zmax',metavar='zmax',type=complex,default=1+1j)
    parser.add_argument('--pixel_size',metavar='pixel_size',type=float,default=1e-2)
    parser.add_argument('--max_iter',metavar='max_iter',type=int,default=20)
    parser.add_argument('-o','--figname',metavar='figname',type=str,default="Julia.png")

    args = parser.parse_args()

    plot_julia(c=args.candidate, zmin=args.zmin, zmax=args.zmax, pixel_size=args.pixel_size, max_iter=args.max_iter, figname=args.figname)


if __name__ == '__main__':
    main()
