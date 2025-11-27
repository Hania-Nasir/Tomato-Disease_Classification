from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime
import tempfile

def generate_pdf(image,disease,confidence):

    temp_file = tempfile.NamedTemporaryFile(delete=False,suffix="pdf")
    c = canvas.Canvas(tempfile.name, pagesize=letter)

    c.setFont("Helvetica-bold",18)
    c.drawString(50,750,"Tomato Plant Disease Classification Report")

    img_reader = ImageReader(image)
    c.drawImage(img_reader,50,500,width=300,height=200)

    c.setFont("Helvetica", 12)
    c.drawString(50, 470, f"Disease: {disease}")
    c.drawString(50, 450, f"Confidence: {confidence}")
    c.drawString(50, 430, f"Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

    c.showPage()
    c.save

    return temp_file.name