import PIL.Image as Image

def transparent_back(img):
    img=img.convert("RGBA")
    L,H = img.size
    color_0 = img.getpixel((0,0))
    print(color_0)
    for h in range(H):
        for l in range(L):
            dot = (l,h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1]+(0,)
                img.putpixel(dot,color_1)
    return img
if __name__ == "__main__":
    img = Image.open(r"C:\Users\Administrator\Desktop\234.png")
    img = transparent_back(img)
    img.save(r"C:\Users\Administrator\Desktop\che11.png")
