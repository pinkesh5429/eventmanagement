from io import BytesIO
from operator import imod
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.conf import settings

def save_pdf(params:dict):
    template=get_template("user/paymentstatus.html")
    html= template.render(params)
    response=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')),response)
    file_name="pinkesh"

    try:
        with open(str(settings.BASE_DIR)+f"/public/static/{file_name}.pdf",'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')),output)

    except Exception as e:
        print(e)
