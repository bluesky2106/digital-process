import numpy as np 

# Modified convolution routine for signal processing
# [y,ny] = conv_m(x,nx,h,nh)
# [y,ny] = convolution result
# [x,nx] = first signal / excitation signal
# [h,nh] = second signal / impulse response

def conv_m(x,nx,h,nh):
    nyb = nx[0] + nh[0]
    nye = nx[len(x)-1] + nh[len(h)-1]
    ny = np.arange(nyb, nye + 1)
    y = np.convolve(x, h)

    return y, ny