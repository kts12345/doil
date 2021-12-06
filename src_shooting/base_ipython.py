from PIL import Image
import IPython.display as ipd

def show(e):
    ipd.display(Image.fromarray(e))