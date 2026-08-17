#!/usr/bin/env python3
"""Kameraoriginal -> webbfil i samma format som resten av assets/images/.

    mkweb.py IMG_2638.HEIC assets/images/lakes/img_2638.jpg

Längsta sidan 1600 px, roteringen inbakad, JPEG kvalitet 82, progressiv.

Varför inte `sips -Z 1600` rakt av: sips skalar den råa pixelbufferten och
lämnar kvar EXIF-orientationen. Ett stående telefonfoto blir då en liggande fil
med en flagga som säger "rotera mig" – webbläsare lyder flaggan, men sajtens
övriga filer är fysiskt roterade (1200x1600 för stående), och en fil som avviker
visas fel så fort något led tappar EXIF. ImageOps.exif_transpose bakar in den.

Pillow läser inte HEIC utan pillow-heif, så sips får göra HEIC->JPEG först.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

MAX_SIDE = 1600
QUALITY = 82


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)

    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    if not src.exists():
        sys.exit("hittar inte %s" % src)
    dst.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp:
        subprocess.run(
            ["sips", "-s", "format", "jpeg", "-s", "formatOptions", "best",
             str(src), "--out", tmp.name],
            check=True, capture_output=True,
        )
        im = Image.open(tmp.name)
        im = ImageOps.exif_transpose(im)
        im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        # save() utan exif-argument skriver ingen orienteringstagg.
        im.convert("RGB").save(dst, "JPEG", quality=QUALITY, optimize=True,
                               progressive=True)

    print("%s  %dx%d  %d kB" % (dst, im.width, im.height,
                                dst.stat().st_size // 1024))


if __name__ == "__main__":
    main()
