#!/usr/bin/env python3

import fitz
from PIL import Image


def __annonate(filename):
    img = Image.open(filename)
    w = min(img.size)
    h = max(img.size)
    rotated = (w != img.size[0])

    newimg = Image.new(img.mode, (w,h), "white")

    if rotated:
        img = img.rotate(90)

    resize_factor = 0.90
    resized_w, resized_h = int(w * resize_factor), int(h * resize_factor)
    resize_img = img.resize((resized_w, resized_h))

    print(w, h, resized_w, resized_h)

    newimg.paste(resize_img, (int((w-resized_w)/2), int((h-resized_h)/2)))

    newimg.show()

    return img



def annonate_pdf(srcfilename, outfilename, annonation):
    pdf = fitz.open(srcfilename)
    page_count = pdf.page_count
    print(page_count)
    print(pdf.metadata)

    for page in pdf:
        pix = page.get_pixmap(dpi=300)
        pix.save("tempfile.png")

        print("#1")
        img = __annonate("tempfile.png")


if __name__ == "__main__":
    import sys
    annonate_pdf(sys.argv[1], sys.argv[2], sys.argv[3])
