"""App opcional: exportación de reportes (ENABLE_REPORTS)."""
import csv
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from core.decorators import feature_required
from core.models import Categoria, Libro


def _libros(request):
    q = request.GET.get('q', '').strip()
    qs = Libro.objects.select_related('categoria')
    if q:
        qs = qs.filter(Q(titulo__icontains=q) | Q(autor__icontains=q))
    return qs


@login_required
@feature_required('ENABLE_REPORTS')
def panel(request):
    resumen = Categoria.objects.annotate(titulos=Count('libros'), ejemplares=Sum('libros__disponibles'))
    return render(request, 'reportes/panel.html', {'resumen': resumen})


@login_required
@feature_required('ENABLE_REPORTS')
def exportar_csv(request):
    resp = HttpResponse(content_type='text/csv; charset=utf-8')
    resp['Content-Disposition'] = 'attachment; filename="catalogo.csv"'
    resp.write('\ufeff')
    w = csv.writer(resp)
    w.writerow(['Título', 'Autor', 'Categoría', 'Año', 'ISBN', 'Disponibles'])
    for l in _libros(request):
        w.writerow([l.titulo, l.autor, l.categoria.nombre, l.anio, l.isbn, l.disponibles])
    return resp


@login_required
@feature_required('ENABLE_REPORTS')
def exportar_pdf(request):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=landscape(A4), title='Reporte de catálogo')
    st = getSampleStyleSheet()
    data = [['Título', 'Autor', 'Categoría', 'Año', 'Disp.']]
    data += [[Paragraph(l.titulo, st['BodyText']), l.autor, l.categoria.nombre, l.anio, l.disponibles]
             for l in _libros(request)]
    t = Table(data, colWidths=[300, 200, 150, 50, 50], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1b3247')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), .4, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    doc.build([Paragraph('BiblioSPL - Reporte del catálogo', st['Title']),
               Paragraph(f'Generado: {timezone.localtime():%d/%m/%Y %H:%M} por {request.user.username}', st['Normal']),
               Spacer(1, 12), t])
    resp = HttpResponse(buf.getvalue(), content_type='application/pdf')
    resp['Content-Disposition'] = 'inline; filename="catalogo.pdf"'
    return resp
