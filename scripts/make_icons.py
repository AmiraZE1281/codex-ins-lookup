"""Generate home-screen icons (original design: cocoa tile, cream 'INS', caramel rule)."""
from PIL import Image, ImageDraw, ImageFont
import pathlib
out = pathlib.Path(__file__).resolve().parent.parent/'docs'
COCOA=(74,44,23); CARAMEL=(181,121,58); CREAM=(250,243,231)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
def make(size, name):
    S=size*4
    im=Image.new('RGB',(S,S),COCOA); d=ImageDraw.Draw(im)
    f=ImageFont.truetype(FONT,int(S*0.34))
    w=d.textlength('INS',font=f); 
    d.text(((S-w)/2,S*0.27),'INS',font=f,fill=CREAM)
    d.rectangle([S*0.22,S*0.66,S*0.78,S*0.70],fill=CARAMEL)
    f2=ImageFont.truetype(FONT,int(S*0.09)); t='CODEX'
    w2=d.textlength(t,font=f2); d.text(((S-w2)/2,S*0.74),t,font=f2,fill=CARAMEL)
    im.resize((size,size),Image.LANCZOS).save(out/name)
make(180,'apple-touch-icon.png'); make(192,'icon-192.png'); make(512,'icon-512.png'); make(32,'favicon.png')
