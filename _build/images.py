"""Optimize source photos into responsive WebP + JPEG. Run: python3 images.py"""
import os, json
from PIL import Image, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src-images")
OUTD = os.path.join(os.path.dirname(HERE) if os.path.basename(HERE) == "_build" else os.path.join(HERE, "out"), "images")
os.makedirs(OUTD, exist_ok=True)
WIDTHS = [800, 1400]
def run():
    meta = {}
    for f in sorted(os.listdir(SRC)):
        name, ext = os.path.splitext(f)
        if ext.lower() not in (".jpg", ".jpeg", ".png", ".webp"): continue
        im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, f))).convert("RGB")
        w, h = im.size
        meta[name] = {"w": w, "h": h, "ratio": round(h / w, 4)}
        for tw in WIDTHS:
            tw2 = min(tw, w); th = round(h * tw2 / w)
            r = im.resize((tw2, th), Image.LANCZOS)
            r.save(os.path.join(OUTD, "%s-%d.webp" % (name, tw)), "WEBP", quality=78, method=6)
            r.save(os.path.join(OUTD, "%s-%d.jpg" % (name, tw)), "JPEG", quality=80, optimize=True, progressive=True)
    json.dump(meta, open(os.path.join(HERE, "images.json"), "w"), indent=1)
    return meta
if __name__ == "__main__":
    m = run(); print(m)
    for f in sorted(os.listdir(OUTD)): print(f, os.path.getsize(os.path.join(OUTD, f)) // 1024, "KB")
