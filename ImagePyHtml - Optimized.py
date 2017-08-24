from PIL import Image
import glob, os, os.path, sys

size = 256, 256
args = []
args = (sys.argv[1:])

rgbcol = ()

def rgb2hex(rgbcol):
    return '#{:02x}{:02x}{:02x}'.format(rgbcol[0], rgbcol[1], rgbcol[2])

for arg in args:
    im = Image.open(arg)
    im.thumbnail(size)
    img = im.convert("RGBA")
    width, height = img.size
    end = width-1
    x = 0
    y = 0
    html = "<html><body><table border=\"0\" cellpadding=\"1\" cellspacing=\"0\"><tr>"    
    while(y < height):
        col = 1
        last=""
        color=""
        while(x < width):
            #print(x,y)
            rgbcol = img.getpixel((x, y))
            color = rgb2hex(rgbcol)
            x+=1
            if(x == end):
                print(x,y)
            if (color != last or x == end ):
                if(col > 1):
                    html += "<td colspan=\"" + str(col) + "\" bgcolor=\"" + last + "\"></td>"
                else:
                    html += "<td bgcolor=\"" + last + "\"></td>"
                col = 1
            else:
                col+=1
            last = color
        y+=1
        x=0
        html += "</tr><tr>"
    html+="</tr></table></body></html>"
    f = open(os.path.splitext(arg)[0] + "o.html", 'w')
    f.write(html)