from PIL import Image

my_image = Image.open("shocked_pikachu.jpg")
image_pixels = my_image.load()
width, height  = my_image.size
for i in range(0, width):
    for m in range(0, height):
        current_pixel = image_pixels[i,m]
        if current_pixel[0] >= 170:
            image_pixels[i,m] = (0, 0, 255, 255)
        if current_pixel[2] == 33 and current_pixel[1] == 85:
            image_pixels[i,m] = (0, 255, 0, 255)
        if current_pixel[0] == 236 and current_pixel[1] == 188:
            image_pixels[i,m] = (0, 255, 0, 255)
        # if (current_pixel[0] >= 170 or current_pixel[0] <= 180) and (current_pixel[2] < 10):
        #     image_pixels[i,m] = (0, 0, 255, 255)
        # if current_pixel[0] >= 170:
        #     image_pixels[i,m] = (0, 0, 255, 255)
my_image.show()
