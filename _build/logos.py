"""Make integration logos transparent, trim, and compress. Run: python3 logos.py"""
import os
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src-logos")
OUTD = os.path.join(os.path.dirname(HERE) if os.path.basename(HERE) == "_build" else os.path.join(HERE, "out"), "logos")
os.makedirs(OUTD, exist_ok=True)
H = 96  # output height in px (displayed at ~40-48px, sharp on retina)

def process(path):
    im = Image.open(path)
    if im.mode == "RGBA" and im.getpixel((0, 0))[3] == 0:
        arr = np.array(im).astype(np.float32)
    else:
        rgb = np.array(im.convert("RGB")).astype(np.float32)
        mx, mn = rgb.max(axis=2), rgb.min(axis=2)
        # fake checkerboard / off-white backgrounds -> pure white
        bgmask = (mn > 200) & ((mx - mn) < 26)
        rgb[bgmask] = 255
        a = (255 - rgb).max(axis=2) / 255.0
        out = np.zeros(rgb.shape[:2] + (4,), np.float32)
        safe = np.where(a > 0, a, 1)[..., None]
        out[..., :3] = np.clip((rgb - 255 * (1 - a[..., None])) / safe, 0, 255)
        out[..., 3] = a * 255
        arr = out
    img = Image.fromarray(arr.astype(np.uint8), "RGBA")
    alpha = img.split()[3].point(lambda v: 255 if v > 12 else 0)
    img = img.crop(alpha.getbbox())
    w, h = img.size
    img = img.resize((max(1, round(w * H / h)), H), Image.LANCZOS)
    return img

if __name__ == "__main__":
    for f in sorted(os.listdir(SRC)):
        name = os.path.splitext(f)[0]
        img = process(os.path.join(SRC, f))
        img.save(os.path.join(OUTD, name + ".png"), optimize=True)
        img.save(os.path.join(OUTD, name + ".webp"), "WEBP", quality=90, method=6)
        print(name, img.size, os.path.getsize(os.path.join(OUTD, name + ".webp")) // 1024, "KB webp",
              os.path.getsize(os.path.join(OUTD, name + ".png")) // 1024, "KB png")
