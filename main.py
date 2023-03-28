from PIL import Image,ImageFilter
def prog1():
    pic="statham.jpg"
    with Image.open(pic) as pic:
        pic.load()

    pic.show()

    width, height= pic.size

    format=pic.format

    mode=pic.mode

    print("Ширина: ",width)
    print("Высота : ",height)
    print("формат : ",format)
    print("цветовая модель : ",mode)
def prog2():
    pic = "statham.jpg"
    with Image.open(pic) as pic:
        pic.load()

    new_pic = pic.resize((pic.width // 3, pic.height // 3))
    new_pic.save("statham2.jpg")

    zerv_pic=pic.transpose(Image.FLIP_TOP_BOTTOM)
    zerv_pic.save("zerv_statham.jpg")
    zerg_pic = pic.transpose(Image.FLIP_LEFT_RIGHT)
    zerg_pic.save("zerg_statham.jpg")
def prog3():
    pics=["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg"]

    for pic in pics:
        with Image.open(pic) as pic:
            pic.load()
            new_pic= pic.filter(ImageFilter.CONTOUR)
            new_pic.show()
            new_pic.save("new_" + pic)
def prog4():

    mark="watermark.png"
    with Image.open(mark) as pic1:
        pic1.load()

    mask_pic=Image.open('watermark.png').resize(pic1.size).convert('L')
    new_pic1=Image.open('watermark.png')
    new_pic1=pic1.resize((100,100))
    pic = "statham.jpg"
    with Image.open(pic) as pic:
        pic.load()

    pic.paste(new_pic1,(10,10),new_pic1)
    pic.save("marked_statham.jpg")
    pic.show()
    pic.close()
prog4()