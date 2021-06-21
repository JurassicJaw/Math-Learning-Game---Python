from PIL import Image



TitleImage = Image.open("G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\png\Title.png")
TitleRGBA = TitleImage.convert("RGBA")
TitleData = TitleRGBA.getdata()

NewTitleData = []
for item in TitleData:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
        # storing a transparent value when we find a black colour
        NewTitleData.append((255, 255, 255, 0))
    else:
        NewTitleData.append(item)  # other colours remain unchanged

TitleRGBA.putdata(NewTitleData)
TitleRGBA.save("transparent_image.png", "PNG")

