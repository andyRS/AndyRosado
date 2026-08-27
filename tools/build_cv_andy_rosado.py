from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "cv-andy-rosado.pdf"

PAGE_W, PAGE_H = A4
NAVY = HexColor("#07111f")
NAVY_2 = HexColor("#0d1b2c")
CYAN = HexColor("#18c7e8")
TEXT = HexColor("#182433")
MUTED = HexColor("#607083")
LIGHT = HexColor("#e7eef5")


def wrapped_lines(text, font, size, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        proposal = f"{current} {word}".strip()
        if stringWidth(proposal, font, size) <= max_width:
            current = proposal
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paragraph(c, text, x, y, width, size=9.2, leading=12.2, color=TEXT, font="Helvetica"):
    c.setFillColor(color)
    c.setFont(font, size)
    for line in wrapped_lines(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def section_title(c, title, x, y, width):
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x, y, title.upper())
    c.setStrokeColor(CYAN)
    c.setLineWidth(2)
    c.line(x, y - 5, x + width, y - 5)
    return y - 20


def role(c, title, meta, description, x, y, width):
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, title)
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawRightString(x + width, y, meta.upper())
    y -= 14
    y = paragraph(c, description, x, y, width, size=8.65, leading=11.2, color=MUTED)
    return y - 9


def side_heading(c, title, x, y):
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 9.4)
    c.drawString(x, y, title.upper())
    return y - 17


def side_text(c, text, x, y, width, size=8.2, leading=11.2, bold=False):
    font = "Helvetica-Bold" if bold else "Helvetica"
    c.setFillColor(white if bold else HexColor("#cbd8e6"))
    c.setFont(font, size)
    for line in wrapped_lines(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("CV profesional - Andy Rosado")
    c.setAuthor("Andy Rosado")
    c.setSubject("Ingeniería de Sistemas, desarrollo full-stack, SEO y automatización con IA")

    side_w = 174
    margin = 26
    main_x = side_w + 30
    main_w = PAGE_W - main_x - 30

    c.setFillColor(NAVY)
    c.rect(0, 0, side_w, PAGE_H, fill=1, stroke=0)
    c.setFillColor(NAVY_2)
    c.rect(0, PAGE_H - 172, side_w, 172, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.rect(side_w, 0, 5, PAGE_H, fill=1, stroke=0)

    # Monogram
    c.setFillColor(CYAN)
    c.circle(side_w / 2, PAGE_H - 74, 35, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(side_w / 2, PAGE_H - 82, "AR")

    y = PAGE_H - 135
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(side_w / 2, y, "ANDY ROSADO")
    y -= 20
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(side_w / 2, y, "INGENIERO DE SISTEMAS")

    x = margin
    side_text_w = side_w - 2 * margin
    y = PAGE_H - 205
    y = side_heading(c, "Perfil online", x, y)
    y = side_text(c, "andyrosado.com", x, y, side_text_w, bold=True)
    y -= 5
    y = side_text(c, "Portafolio, casos de estudio, servicios y formulario de contacto.", x, y, side_text_w)
    y -= 5
    y = side_text(c, "Santo Domingo, República Dominicana", x, y, side_text_w)

    y -= 21
    y = side_heading(c, "Especialidades", x, y)
    for item in [
        "Desarrollo full-stack y SaaS",
        "Automatización con n8n y agentes IA",
        "E-commerce e integraciones",
        "SEO técnico y analítica",
        "Meta Business Suite y Meta Ads",
    ]:
        c.setFillColor(CYAN)
        c.circle(x + 2, y + 3, 1.5, fill=1, stroke=0)
        y = side_text(c, item, x + 10, y, side_text_w - 10)
        y -= 4

    y -= 16
    y = side_heading(c, "Tecnologías", x, y)
    for group in [
        ("Frontend", "React, Next.js, TypeScript, HTML, CSS"),
        ("Backend", "Node.js, APIs, bases de datos"),
        ("Automatización", "n8n, agentes IA, WhatsApp Cloud API"),
        ("Marketing", "Search Console, GA4, Semrush, Google Ads, Meta Ads"),
    ]:
        y = side_text(c, group[0], x, y, side_text_w, bold=True)
        y = side_text(c, group[1], x, y, side_text_w)
        y -= 7

    # Main column
    y = PAGE_H - 54
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 25)
    c.drawString(main_x, y, "PRODUCTOS DIGITALES")
    y -= 28
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(main_x, y, "FULL-STACK - SEO - AUTOMATIZACIÓN CON IA")
    y -= 32

    y = section_title(c, "Perfil profesional", main_x, y, main_w)
    y = paragraph(
        c,
        "Ingeniero de Sistemas enfocado en convertir objetivos de negocio en productos digitales claros, medibles y escalables. Desarrollo plataformas SaaS, e-commerce y sistemas full-stack; complemento la implementación con SEO técnico, analítica, automatizaciones y configuración de infraestructura publicitaria.",
        main_x,
        y,
        main_w,
        size=9.1,
        leading=12.3,
    )
    y -= 18

    y = section_title(c, "Experiencia aplicada seleccionada", main_x, y, main_w)
    y = role(
        c,
        "Agentes de ventas por WhatsApp",
        "Producto propio - IA",
        "Sistema comercial con cuatro agentes especializados, memoria por cliente, atribución de campañas, supervisión y transferencia humana.",
        main_x,
        y,
        main_w,
    )
    y = role(
        c,
        "VitaGloss RD",
        "E-commerce - Meta",
        "E-commerce y gestión de ventas con activos de Meta conectados, cuenta publicitaria, píxel y catálogo de productos.",
        main_x,
        y,
        main_w,
    )
    y = role(
        c,
        "Kingdom Studio",
        "SaaS - Full-stack",
        "Plataforma de automatización editorial con inteligencia artificial, flujos operativos y generación de documentos.",
        main_x,
        y,
        main_w,
    )
    y = role(
        c,
        "La Agencia IA",
        "SEO - Meta Ads",
        "SEO técnico e infraestructura publicitaria: portafolio profesional en Meta, Instagram conectado, cuenta publicitaria y configuración de anuncios.",
        main_x,
        y,
        main_w,
    )

    y -= 5
    y = section_title(c, "Formacion y certificaciones", main_x, y, main_w)
    for title, detail in [
        ("Ingeniería de Sistemas", "Formación universitaria - UTESA"),
        ("AI-Powered Performance Ads", "Certificación oficial de Google Skillshop"),
        ("AI-Powered Shopping Ads", "Certificación oficial de Google Skillshop"),
        ("Machine Learning & AI Fundamentals", "AWS Skill Builder"),
    ]:
        c.setFillColor(TEXT)
        c.setFont("Helvetica-Bold", 8.8)
        c.drawString(main_x, y, title)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 8.2)
        c.drawRightString(main_x + main_w, y, detail)
        y -= 15

    c.setFillColor(LIGHT)
    c.rect(main_x, 28, main_w, 34, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(main_x + 12, 48, "PORTAFOLIO Y CASOS DE ESTUDIO")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.5)
    c.drawString(main_x + 12, 35, "andyrosado.com/portafolio/")
    c.linkURL("https://andyrosado.com/portafolio/", (main_x, 28, main_x + main_w, 62), relative=0)

    c.setFillColor(HexColor("#8090a0"))
    c.setFont("Helvetica", 6.8)
    c.drawRightString(PAGE_W - 30, 14, "Documento profesional - Andy Rosado")
    c.save()


if __name__ == "__main__":
    build()
    print(OUTPUT)
