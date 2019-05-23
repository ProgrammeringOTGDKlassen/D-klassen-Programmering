white_pixels = np.array(np.where(image == 255))
first_white_pixel = white_pixels[:,0]
last_white_pixel = white_pixels[:,-1]
first_white_pixel, last_white_pixel = np.array(np.where(image == 255))[:,[0,-1]].T