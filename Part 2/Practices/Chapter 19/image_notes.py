from PIL import Image
from pathlib import Path

cwd = Path.cwd()


catIm = Image.open(cwd / 'Data' / 'absfiles' / 'zophie.png')

print(catIm.size)

new_image = Image.new('RGBA', (100,100), 'purple') #? if u don't pass the color it will set to be transparent image
new_image.save(cwd / 'Data' / 'purpleImageTest.png')


croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')

catCopyImg = catIm.copy() #? and paste do not have any relation to os clipboard

catCopyImg.paste(croppedIm, (0,0))
catCopyImg.paste(croppedIm, (400,500))

catCopyImg.save('hehecopy.png')

catTwo = catIm.copy()

catImgW, catImgH = catIm.size
faceImgW, faceImgH = croppedIm.size

for left in range(0, catImgW, faceImgW):
    for top in range(0, catImgH, faceImgH):
        catTwo.paste(croppedIm, (left, top))
        
catTwo.save('HEHEHECATHEHEE.png')


'''Resize

from PIL import Image
catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')
'''


'''Rotate

from PIL import Image
catIm = Image.open('zophie.png')
catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')
'''

'''mirro flip

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
'''

# from PIL import ImageDraw

# im = Image.new("RGBA", (100,100), 'white')

# draw = ImageDraw.Draw(im)

from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green') # cool - generative art :D

im.save('drawing.png')


''' U CAN ALSO DRAW TEXT - example:

from PIL import Image, ImageDraw, ImageFont
import os
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'FONT_FOLDER' # e.g. ‘/Library/Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('text.png')
'''