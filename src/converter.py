from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader


def converter(images):
    if not images:
        return

    root_path = Path(__file__).resolve().parent.parent

    pdf_path = str(root_path / "output.pdf")

    a4_width, a4_height = A4
    c = canvas.Canvas(pdf_path, pagesize=A4)

    for image_path in images:
        with Image.open(image_path) as image:
            image = image.convert("RGB")
            image.thumbnail((int(a4_width), int(a4_height)), Image.Resampling.LANCZOS)

            width, height = image.size
            x = (a4_width - width) / 2
            y = (a4_height - height) / 2

            c.drawImage(
                ImageReader(image),
                x,
                y,
                width=width,
                height=height
            )

        c.showPage()

    c.save()