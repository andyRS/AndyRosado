from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "manual-propuestas-meta-business-suite-andy-rosado.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

BG = colors.HexColor("#0B0F14")
SURFACE = colors.HexColor("#121923")
SURFACE_2 = colors.HexColor("#18212C")
CYAN = colors.HexColor("#22D3EE")
TEXT = colors.HexColor("#F4F7FA")
MUTED = colors.HexColor("#A7B3C4")
BORDER = colors.HexColor("#2B3A49")
WHITE = colors.white

FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
font_regular_path = Path("C:/Windows/Fonts/arial.ttf")
font_bold_path = Path("C:/Windows/Fonts/arialbd.ttf")
if font_regular_path.exists() and font_bold_path.exists():
    pdfmetrics.registerFont(TTFont("AndySans", str(font_regular_path)))
    pdfmetrics.registerFont(TTFont("AndySans-Bold", str(font_bold_path)))
    FONT_REGULAR = "AndySans"
    FONT_BOLD = "AndySans-Bold"


class BrandedDocTemplate(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=A4,
            rightMargin=18 * mm,
            leftMargin=18 * mm,
            topMargin=22 * mm,
            bottomMargin=18 * mm,
            title="Manual de propuestas para configuración de Meta Business Suite",
            author="Andy Rosado",
            subject="Guía comercial y operativa para propuestas de Meta Business Suite",
        )
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="content")
        self.addPageTemplates(PageTemplate(id="main", frames=[frame], onPage=self.draw_page))

    def draw_page(self, canvas, doc):
        page = canvas.getPageNumber()
        canvas.saveState()
        canvas.setFillColor(BG if page == 1 else colors.white)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        if page > 1:
            canvas.setFillColor(BG)
            canvas.rect(0, A4[1] - 12 * mm, A4[0], 12 * mm, fill=1, stroke=0)
            canvas.setFillColor(CYAN)
            canvas.setFont(FONT_BOLD, 9)
            canvas.drawString(18 * mm, A4[1] - 8 * mm, "AndyDev")
            canvas.setFillColor(colors.HexColor("#425466"))
            canvas.rect(18 * mm, 12 * mm, A4[0] - 36 * mm, 0.35 * mm, fill=1, stroke=0)
            canvas.setFillColor(colors.HexColor("#596579"))
            canvas.setFont(FONT_REGULAR, 8)
            canvas.drawString(18 * mm, 7.5 * mm, "Manual de propuestas - Meta Business Suite")
            canvas.drawRightString(A4[0] - 18 * mm, 7.5 * mm, str(page))
        canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverBrand", fontName=FONT_BOLD, fontSize=18, leading=22, textColor=CYAN,
    alignment=TA_LEFT, spaceAfter=40,
))
styles.add(ParagraphStyle(
    name="CoverTitle", fontName=FONT_BOLD, fontSize=31, leading=35, textColor=TEXT,
    alignment=TA_LEFT, spaceAfter=18,
))
styles.add(ParagraphStyle(
    name="CoverSub", fontName=FONT_REGULAR, fontSize=13, leading=20, textColor=MUTED,
    alignment=TA_LEFT, spaceAfter=20,
))
styles.add(ParagraphStyle(
    name="CoverMeta", fontName=FONT_REGULAR, fontSize=9.5, leading=14, textColor=MUTED,
    alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name="H1Andy", fontName=FONT_BOLD, fontSize=22, leading=27, textColor=BG,
    spaceBefore=4, spaceAfter=12,
))
styles.add(ParagraphStyle(
    name="H2Andy", fontName=FONT_BOLD, fontSize=14, leading=18, textColor=colors.HexColor("#087B8C"),
    spaceBefore=12, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="BodyAndy", fontName=FONT_REGULAR, fontSize=9.8, leading=14.5, textColor=colors.HexColor("#253241"),
    spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="SmallAndy", fontName=FONT_REGULAR, fontSize=8.2, leading=11.5, textColor=colors.HexColor("#536274"),
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="BulletAndy", fontName=FONT_REGULAR, fontSize=9.5, leading=14, textColor=colors.HexColor("#253241"),
    leftIndent=12, firstLineIndent=-8, bulletIndent=2, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="CalloutTitle", fontName=FONT_BOLD, fontSize=11, leading=14, textColor=CYAN, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="CalloutBody", fontName=FONT_REGULAR, fontSize=9.2, leading=13.5, textColor=TEXT,
))
styles.add(ParagraphStyle(
    name="TableHead", fontName=FONT_BOLD, fontSize=8.5, leading=11, textColor=TEXT,
))
styles.add(ParagraphStyle(
    name="TableBody", fontName=FONT_REGULAR, fontSize=8.2, leading=11.5, textColor=colors.HexColor("#253241"),
))
styles.add(ParagraphStyle(
    name="Template", fontName=FONT_REGULAR, fontSize=9, leading=13.5, textColor=colors.HexColor("#1F2A37"),
))


def bullet(text):
    return Paragraph(f"• {text}", styles["BulletAndy"])


def check(text):
    return Paragraph(f"□ {text}", styles["BulletAndy"])


def callout(title, body):
    table = Table([
        [Paragraph(title, styles["CalloutTitle"])],
        [Paragraph(body, styles["CalloutBody"])],
    ], colWidths=[174 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SURFACE),
        ("BOX", (0, 0), (-1, -1), 0.8, CYAN),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, 0), 9),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
    ]))
    return table


def section_title(number, title):
    return KeepTogether([
        Paragraph(f"{number} / {title}", styles["H1Andy"]),
        Table([[""]], colWidths=[28 * mm], rowHeights=[1.2 * mm], style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), CYAN),
        ])),
        Spacer(1, 6 * mm),
    ])


def scope_table():
    data = [
        [Paragraph("Módulo", styles["TableHead"]), Paragraph("Qué se configura", styles["TableHead"]), Paragraph("Evidencia de entrega", styles["TableHead"])],
        [Paragraph("Negocio y seguridad", styles["TableBody"]), Paragraph("Business Portfolio/Manager, datos del negocio, personas, socios, roles y 2FA.", styles["TableBody"]), Paragraph("Mapa de activos y accesos validados.", styles["TableBody"])],
        [Paragraph("Canales", styles["TableBody"]), Paragraph("Página de Facebook y cuenta profesional de Instagram conectadas.", styles["TableBody"]), Paragraph("Ambos activos visibles y asignados.", styles["TableBody"])],
        [Paragraph("Publicidad", styles["TableBody"]), Paragraph("Cuenta publicitaria, zona horaria, moneda, método de pago y permisos.", styles["TableBody"]), Paragraph("Cuenta operativa; pago validado por el cliente.", styles["TableBody"])],
        [Paragraph("Medición", styles["TableBody"]), Paragraph("Dataset/Meta Pixel, instalación, eventos acordados, dominio y pruebas.", styles["TableBody"]), Paragraph("Eventos recibidos en Events Manager.", styles["TableBody"])],
        [Paragraph("Comercio", styles["TableBody"]), Paragraph("Commerce Manager, catálogo, fuente de datos y diagnóstico de artículos.", styles["TableBody"]), Paragraph("Catálogo cargado y errores documentados.", styles["TableBody"])],
        [Paragraph("Cierre", styles["TableBody"]), Paragraph("QA, documentación, transferencia y recomendaciones.", styles["TableBody"]), Paragraph("Checklist firmado o aprobación escrita.", styles["TableBody"])],
    ]
    table = Table(data, colWidths=[34 * mm, 88 * mm, 52 * mm], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F7FA")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return table


story = []

# Cover
story += [
    Spacer(1, 20 * mm),
    Paragraph("Andy<span color='#F4F7FA'>Dev</span>", styles["CoverBrand"]),
    Paragraph("Manual de propuestas para configuración de Meta Business Suite", styles["CoverTitle"]),
    Paragraph("Guía comercial y operativa para preparar propuestas claras, proteger el alcance y entregar una infraestructura lista para publicidad en Facebook e Instagram.", styles["CoverSub"]),
    Spacer(1, 20 * mm),
    callout("OBJETIVO", "Usar este manual como checklist interno al responder oportunidades en Workana o clientes directos. No sustituye la documentación oficial ni garantiza aprobaciones de Meta."),
    Spacer(1, 22 * mm),
    Paragraph("Versión 1.0  |  Agosto 2026<br/>Andy Rosado Web  |  andyrosado.com", styles["CoverMeta"]),
    PageBreak(),
]

# 1
story += [
    section_title("01", "Antes de cotizar: diagnóstico obligatorio"),
    Paragraph("Una buena propuesta empieza delimitando el estado real de los activos. No prometas una configuración completa hasta confirmar qué existe, quién es propietario y qué accesos están disponibles.", styles["BodyAndy"]),
    Paragraph("Preguntas que debes hacer", styles["H2Andy"]),
    bullet("¿La empresa ya tiene un Business Portfolio/Business Manager? ¿Quién es el administrador principal?"),
    bullet("¿Existen la página de Facebook y la cuenta profesional de Instagram? ¿Están conectadas entre sí?"),
    bullet("¿Ya existe una cuenta publicitaria? Indicar moneda, zona horaria y si ha tenido restricciones."),
    bullet("¿El cliente tiene dominio propio y acceso al DNS, CMS, tienda o desarrollador del sitio?"),
    bullet("¿Existe un píxel/dataset? ¿Qué eventos necesitan medirse: visita, lead, carrito, compra u otros?"),
    bullet("¿Cuántos productos tiene el catálogo y de dónde salen los datos: carga manual, feed, Shopify, WooCommerce u otra plataforma?"),
    bullet("¿El proyecto incluye solo infraestructura o también creación/gestión de campañas?"),
    bullet("¿Hay fecha de lanzamiento, país de facturación y personas que recibirán acceso?"),
    Spacer(1, 4 * mm),
    callout("REGLA DE SEGURIDAD", "Nunca solicites contraseñas por chat. Pide que el cliente te agregue como persona o socio con el acceso mínimo necesario. Recomienda autenticación de dos factores para administradores."),
    PageBreak(),
]

# 2
story += [
    section_title("02", "Alcance técnico que puedes ofrecer"),
    Paragraph("Selecciona únicamente los módulos que correspondan al diagnóstico. La propuesta debe relacionar cada tarea con una evidencia verificable de entrega.", styles["BodyAndy"]),
    scope_table(),
    Spacer(1, 6 * mm),
    Paragraph("Opcionales que deben cotizarse por separado", styles["H2Andy"]),
    bullet("Conversions API, server-side tracking o integraciones personalizadas."),
    bullet("Corrección masiva de feeds, variantes, imágenes, precios o inventario."),
    bullet("Migración o recuperación de activos y soporte ante cuentas restringidas."),
    bullet("Configuración de WhatsApp Business, CRM o automatizaciones posteriores."),
    bullet("Creación de campañas, anuncios, copies, creatividades y optimización mensual."),
    PageBreak(),
]

# 3
story += [
    section_title("03", "Estructura de una propuesta profesional"),
    Paragraph("Tu propuesta debe permitir que el cliente entienda en menos de dos minutos qué resolverás, qué necesitas y cómo sabrá que terminaste.", styles["BodyAndy"]),
    Paragraph("1. Apertura contextual", styles["H2Andy"]),
    Paragraph("Menciona el objetivo específico del cliente y evita frases genéricas. Ejemplo: centralizar los activos de la marca y dejar preparada la medición para futuras campañas.", styles["BodyAndy"]),
    Paragraph("2. Diagnóstico o supuesto de partida", styles["H2Andy"]),
    Paragraph("Resume lo conocido y marca lo que debe confirmarse. Si el anuncio no da suficiente información, indica que el precio final depende de revisar activos, restricciones e integraciones.", styles["BodyAndy"]),
    Paragraph("3. Alcance por entregables", styles["H2Andy"]),
    Paragraph("Usa tareas concretas: configurar, conectar, validar, documentar. Evita términos ambiguos como 'dejar todo listo' sin explicar qué significa.", styles["BodyAndy"]),
    Paragraph("4. Requisitos y responsabilidades", styles["H2Andy"]),
    Paragraph("Aclara accesos, información legal, método de pago, catálogo y disponibilidad del cliente para verificaciones. El cliente conserva la propiedad de todos los activos.", styles["BodyAndy"]),
    Paragraph("5. Plazo, hitos y revisiones", styles["H2Andy"]),
    Paragraph("Cuenta el plazo desde la recepción de todos los accesos. Separa configuración, validación y cierre; indica cuántas rondas de ajustes incluye.", styles["BodyAndy"]),
    Paragraph("6. Exclusiones, inversión y aceptación", styles["H2Andy"]),
    Paragraph("Distingue la configuración técnica de la gestión de anuncios. Define forma de pago, vigencia de la propuesta y criterio de aceptación.", styles["BodyAndy"]),
    PageBreak(),
]

# 4
story += [
    section_title("04", "Paquetes de alcance recomendados"),
    Paragraph("Los paquetes ayudan a comparar opciones sin convertir cada oportunidad en una lista distinta. Ajusta el precio después del diagnóstico.", styles["BodyAndy"]),
]
packages = [
    [Paragraph("BASE", styles["TableHead"]), Paragraph("MEDICIÓN", styles["TableHead"]), Paragraph("COMERCIO", styles["TableHead"])],
    [Paragraph("Para marcas que necesitan ordenar su presencia y activos.", styles["TableBody"]), Paragraph("Para negocios con sitio web que captan leads o ventas.", styles["TableBody"]), Paragraph("Para e-commerce que necesita catálogo y medición.", styles["TableBody"])],
    [Paragraph("• Business Portfolio/Manager<br/>• Facebook + Instagram<br/>• Roles y seguridad<br/>• Cuenta publicitaria<br/>• QA y entrega", styles["TableBody"]), Paragraph("• Todo Base<br/>• Dominio<br/>• Meta Pixel/dataset<br/>• Eventos acordados<br/>• Pruebas en Events Manager", styles["TableBody"]), Paragraph("• Todo Medición<br/>• Commerce Manager<br/>• Catálogo y fuente de datos<br/>• Diagnóstico de artículos<br/>• Recomendaciones de mantenimiento", styles["TableBody"])],
]
pt = Table(packages, colWidths=[58 * mm] * 3)
pt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), BG),
    ("GRID", (0, 0), (-1, -1), 0.6, BORDER),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))
story += [pt, Spacer(1, 8 * mm), callout("NO PUBLICAR UN PRECIO A CIEGAS", "La complejidad cambia según activos existentes, restricciones, plataforma web, volumen del catálogo y necesidad de integraciones. Usa un precio base y añade complejidad solo después de revisar el caso."), PageBreak()]

# 5
story += [
    section_title("05", "Accesos y materiales que debe aportar el cliente"),
    check("Razón social, dirección, teléfono, sitio web y datos fiscales/comerciales correctos."),
    check("Administrador disponible para aceptar invitaciones, verificaciones y términos."),
    check("Página de Facebook y cuenta de Instagram profesional con propiedad clara."),
    check("Acceso al dominio/DNS y al CMS, tienda o desarrollador responsable."),
    check("Método de pago agregado directamente por el cliente a la cuenta publicitaria."),
    check("Archivo o fuente de productos con título, descripción, precio, disponibilidad, enlace e imagen."),
    check("Política de privacidad y consentimiento de cookies cuando aplique."),
    check("Definición de eventos y acciones relevantes para el negocio."),
    check("Correo corporativo de las personas que recibirán permisos."),
    Spacer(1, 6 * mm),
    callout("RESPONSABILIDAD DEL CLIENTE", "Las demoras causadas por accesos incompletos, verificaciones pendientes, pagos rechazados o revisiones de Meta deben pausar el cronograma. Escríbelo en la propuesta."),
    PageBreak(),
]

# 6
story += [
    section_title("06", "Exclusiones y límites que deben quedar escritos"),
    bullet("La aprobación de cuentas, comercios, productos o anuncios depende de Meta y no puede garantizarse."),
    bullet("El presupuesto publicitario y los cargos de Meta no forman parte de tus honorarios."),
    bullet("No se incluyen campañas, segmentación, copies, creatividades ni optimización continua salvo que se coticen."),
    bullet("No se garantiza un número de ventas, leads, ROAS ni resultados comerciales por una configuración técnica."),
    bullet("La recuperación de cuentas bloqueadas o activos cuya propiedad está disputada requiere un alcance nuevo."),
    bullet("Cambios de moneda o zona horaria pueden exigir crear otra cuenta publicitaria; se confirma en diagnóstico."),
    bullet("La asesoría legal sobre privacidad, cookies, términos o políticas de comercio corresponde al cliente."),
    bullet("Integraciones avanzadas, Conversions API, desarrollo web o corrección de feeds se presupuestan aparte."),
    Spacer(1, 6 * mm),
    Paragraph("Cláusula sugerida", styles["H2Andy"]),
    callout("ALCANCE Y TERCEROS", "La entrega cubre la configuración y validación técnica descrita. Los procesos de revisión, aprobación, restricción o disponibilidad de funciones administrados por Meta son externos al profesional y pueden modificar el plazo sin constituir incumplimiento."),
    PageBreak(),
]

# 7
story += [
    section_title("07", "Fases, plazos y criterios de aceptación"),
    Paragraph("Usa hitos breves y verificables. El ejemplo siguiente se adapta al tamaño del proyecto.", styles["BodyAndy"]),
]
timeline = [
    [Paragraph("Fase", styles["TableHead"]), Paragraph("Actividad", styles["TableHead"]), Paragraph("Criterio de salida", styles["TableHead"])],
    [Paragraph("1. Diagnóstico", styles["TableBody"]), Paragraph("Inventario de activos, propiedad, restricciones, accesos y alcance.", styles["TableBody"]), Paragraph("Mapa aprobado por el cliente.", styles["TableBody"])],
    [Paragraph("2. Configuración", styles["TableBody"]), Paragraph("Business Suite, canales, roles y cuenta publicitaria.", styles["TableBody"]), Paragraph("Activos conectados y permisos probados.", styles["TableBody"])],
    [Paragraph("3. Medición", styles["TableBody"]), Paragraph("Dominio, píxel/dataset, eventos e integración web.", styles["TableBody"]), Paragraph("Eventos recibidos y documentados.", styles["TableBody"])],
    [Paragraph("4. Comercio", styles["TableBody"]), Paragraph("Catálogo, fuente de datos y revisión de errores.", styles["TableBody"]), Paragraph("Productos cargados o incidencias informadas.", styles["TableBody"])],
    [Paragraph("5. Entrega", styles["TableBody"]), Paragraph("QA, capturas, accesos, manual breve y recomendaciones.", styles["TableBody"]), Paragraph("Aprobación escrita o cierre del período de revisión.", styles["TableBody"])],
]
tt = Table(timeline, colWidths=[35 * mm, 87 * mm, 52 * mm], repeatRows=1)
tt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), BG),
    ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F7FA")]),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
]))
story += [tt, Spacer(1, 7 * mm), Paragraph("Incluye un período de revisión definido -por ejemplo, 3 días hábiles- y una ronda de ajustes sobre el alcance contratado. Los cambios nuevos se cotizan como ampliación.", styles["BodyAndy"]), PageBreak()]

# 8
story += [
    section_title("08", "Cómo calcular y presentar la inversión"),
    Paragraph("No calcules solo por horas. El precio debe reflejar el riesgo, la cantidad de activos y la responsabilidad técnica.", styles["BodyAndy"]),
    Paragraph("Fórmula práctica", styles["H2Andy"]),
    callout("INVERSIÓN", "Base de configuración + activos adicionales + integración web + complejidad del catálogo + recuperación/restricciones + urgencia + soporte posterior."),
    Spacer(1, 6 * mm),
    Paragraph("Recomendaciones comerciales", styles["H2Andy"]),
    bullet("Usa hitos: diagnóstico/inicio, configuración y entrega."),
    bullet("En proyectos directos, solicita anticipo antes de tocar activos; en Workana usa depósito en garantía."),
    bullet("Indica si impuestos, comisiones de plataforma y herramientas de terceros están incluidos o no."),
    bullet("Define una vigencia para la propuesta y una tarifa o nueva cotización para ampliaciones."),
    bullet("Ofrece soporte posterior como bloque separado: correcciones de configuración, no gestión de campañas."),
    bullet("No reduzcas el precio eliminando QA, seguridad o documentación; reduce módulos del alcance."),
    PageBreak(),
]

# 9 template
story += [
    section_title("09", "Plantilla lista para adaptar en Workana"),
]
template_text = """
<b>Hola [Nombre del cliente],</b><br/><br/>
Puedo ayudarte a organizar y configurar la infraestructura de Meta de [marca] para que sus activos de Facebook e Instagram queden centralizados, con permisos correctos y preparados para publicidad y medición.<br/><br/>
<b>Alcance propuesto</b><br/>
• Revisión del estado actual y propiedad de los activos.<br/>
• Configuración de Meta Business Suite/Business Portfolio.<br/>
• Conexión de la página de Facebook y la cuenta profesional de Instagram.<br/>
• Creación o configuración de la cuenta publicitaria, roles y seguridad.<br/>
• [Verificación del dominio e implementación de Meta Pixel/eventos].<br/>
• [Configuración del catálogo y su fuente de productos].<br/>
• Pruebas, documentación y transferencia final.<br/><br/>
<b>Para iniciar necesito</b><br/>
Acceso mediante invitación, disponibilidad del administrador, datos comerciales, acceso al sitio/dominio y la fuente de productos cuando aplique. No necesito que compartas contraseñas.<br/><br/>
<b>Entrega y plazo</b><br/>
[X] días hábiles desde la recepción de todos los accesos, divididos en [hitos]. Incluye [número] ronda de ajustes sobre el alcance acordado.<br/><br/>
<b>No incluido</b><br/>
Presupuesto publicitario, creación o gestión de campañas, creatividades y garantías de aprobación o resultados, salvo que se indiquen como adicionales.<br/><br/>
Antes de confirmar, necesito saber: [preguntas pendientes]. Con esas respuestas puedo validar el alcance y cerrar la inversión exacta.<br/><br/>
<b>Andy Rosado</b><br/>Ingeniero de Sistemas | Desarrollo web, medición y automatización
"""
template_table = Table([[Paragraph(template_text, styles["Template"])]], colWidths=[174 * mm])
template_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F7FA")),
    ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
    ("LEFTPADDING", (0, 0), (-1, -1), 12),
    ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ("TOPPADDING", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
]))
story += [template_table, PageBreak()]

# 10 final checklist
story += [
    section_title("10", "Checklist final antes de enviar"),
    Paragraph("Claridad comercial", styles["H2Andy"]),
    check("La apertura menciona el problema y objetivo real del cliente."),
    check("El alcance usa tareas y entregables concretos."),
    check("Los opcionales están separados del alcance principal."),
    check("El precio, hitos, plazo y vigencia están claros."),
    Paragraph("Protección del proyecto", styles["H2Andy"]),
    check("Se indica que el plazo inicia al recibir todos los accesos."),
    check("No se solicitan contraseñas; se usa invitación o acceso de socio."),
    check("Se aclaran aprobaciones externas, restricciones y responsabilidades del cliente."),
    check("Campañas, inversión publicitaria y resultados quedan fuera si no se contrataron."),
    Paragraph("Calidad de la entrega", styles["H2Andy"]),
    check("Cada módulo tiene una prueba o evidencia de aceptación."),
    check("Se contempla QA, documentación y transferencia de accesos."),
    check("Se define el período de revisión y qué cuenta como cambio adicional."),
    check("El cliente conserva la propiedad y administración de sus activos."),
    Spacer(1, 8 * mm),
    callout("PRINCIPIO FINAL", "Una propuesta sólida no promete que Meta aprobará todo ni que las campañas venderán. Promete un proceso profesional, una configuración verificable y una entrega documentada."),
    Spacer(1, 12 * mm),
    Paragraph("andyrosado.com  |  soporte@andyrosado.com  |  Santo Domingo, República Dominicana", styles["SmallAndy"]),
]


doc = BrandedDocTemplate(str(OUTPUT))
doc.build(story)
print(OUTPUT)
