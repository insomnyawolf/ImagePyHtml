from PIL import Image
import glob, os, os.path, sys

size = 256, 256
args = []
args = (sys.argv[1:])

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

for arg in args:
    im = Image.open(arg)
    im.thumbnail(size)
    width, height = im.size
    x = 0
    y = 0
    html = "<html><body><table border=\"0\" cellpadding=\"1\" cellspacing=\"0\"><tr>"
    while(y < height and x < width):
        r, g, b = im.getpixel((x, y))
        color = str(r) + "," + str(g) + "," + str(b)
        html += "<td bgcolor=\"" + rgb2hex(r, g, b) + "\"></td>"
        x += 1
        if(x == width):
            y+=1
            x=0
            html += "</tr><tr>"

    html+="</tr></table></body></html>"
    f = open(os.path.splitext(arg)[0] + ".html", 'w')
    f.write(html)