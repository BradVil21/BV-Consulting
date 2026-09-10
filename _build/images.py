"""Compress photos in src-images/ into small responsive AVIF + WebP + JPEG files.
Run: python3 images.py   (needs: pip3 install pillow)
Output: /images/<name>-480|800|1200.(avif|webp|jpg)
"""
import os, json, glob
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src-images")
OUTD = os.path.join(os.path.dirname(HERE) if os.path.basename(HERE) == "_build" else os.path.join(HERE, "out"), "images")
os.makedirs(OUTD, exist_ok=True)
WIDTHS = [480, 800, 1200]


def run():
    meta = {}
    for old in glob.glob(os.path.join(OUTD, "*")):
        os.remove(old)
    for f in sorted(os.listdir(SRC)):
        name, ext = os.path.splitext(f)
        if ext.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
            continue
        im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, f))).convert("RGB")
        w, h = im.size
        meta[name] = {"w": w, "h": h, "ratio": round(h / w, 4)}
        for tw in WIDTHS:
            tw2 = min(tw, w)
            r = im.resize((tw2, round(h * tw2 / w)), Image.LANCZOS)
            base = os.path.join(OUTD, "%s-%d" % (name, tw))
            r.save(base + ".avif", "AVIF", quality=55, speed=4)
            r.save(base + ".webp", "WEBP", quality=72, method=6)
            r.save(base + ".jpg", "JPEG", quality=74, optimize=True, progressive=True, subsampling=2)
    json.dump(meta, open(os.path.join(HERE, "images.json"), "w"), indent=1)
    return meta


if __name__ == "__main__":
    run()
    total = 0
    for f in sorted(os.listdir(OUTD)):
        s = os.path.getsize(os.path.join(OUTD, f)); total += s
        print("%-48s %5d KB" % (f, s // 1024))
    print("total", total // 1024, "KB")
