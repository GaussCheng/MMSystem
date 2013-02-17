from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _
import xlwt
import re
from django.http import HttpResponse
from django.utils.http import urlquote
from django.utils.encoding import smart_str

def print_to_html(request, queryset):
    maintain_logs = queryset
    return render_to_response('maintain_log/print_to_html.html',
                              {'maintain_logs': maintain_logs})

def export_to_excel(request, queryset):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('MaintainLog')
#    style = xlwt.easyxf('font: bold on,colour_index green,height 360;'
#                          'align: wrap on;'
#                          'borders:left 1,right 1,top 1,bottom 1;'
#                          'pattern: pattern alt_bars, fore_colour gray25, back_colour gray25')
    
#    fnt =xlwt.Font()
#    fnt.name = 'Arial'
#    fnt.colour_index = 4
#    fnt.bold = True

#    pattern=xlwt.Pattern()
#    pattern.pattern = xlwt.Pattern.SOLID_PATTERN  
#    pattern.pattern_back_colour=0x3A
#    pattern.pattern_fore_colour=0x3A
#
#    borders = xlwt.Borders()
#    borders.left = 1
#    borders.right = 1
#    borders.top = 1
#    borders.bottom = 1
#    borders.bottom_colour=0x3A    
#
    style = xlwt.XFStyle()
#    style.font = fnt
#    style.borders = borders    
#    style.pattern = pattern
    excel_date_fmt = 'MM/DD/YYYY'
    style.num_format_str = excel_date_fmt
    
    row = 0
    
    ws.write(row, 0, _('Customer'), style)
    ws.write(row, 1, _('Product'), style)
    ws.write(row, 2, _('Code'), style)
    ws.write(row, 3, _('Manufacture Date'), style)
    ws.write(row, 4, _('Carry Date'), style)
    ws.write(row, 5, _('Bug Found By Customer'), style)
    ws.write(row, 6, _('Bug Found By Tester'), style)
    ws.write(row, 7, _('Maintain Date'), style)
    ws.write(row, 8, _('Receive Express Number'), style)
    ws.write(row, 9, _('Invoice Number'), style)
    ws.write(row, 10, _('Express Delivery'), style)
    
#    style.borders = None
#    style.pattern = None
#    fnt.bold = False
#    style.font = fnt
    row += 1
    
    for log in queryset:
        print log
        ws.write(row, 0, unicode(log.customer))
        ws.write(row, 1, unicode(log.product))
        ws.write(row, 2, log.code)
        ws.write(row, 3, log.manufacture_date, style)
        ws.write(row, 4, log.carry_date, style)
        ws.write(row, 5, log.bug_find_by_customer)
        ws.write(row, 6, log.result)
        ws.write(row, 7, log.maintain_date, style)
        ws.write(row, 8, log.receive_express_number)
        ws.write(row, 9, log.invoice_number)
        ws.write(row, 10, unicode(log.express))
        row += 1
    fname = 'maintain_logs.xls'
    agent=request.META.get('HTTP_USER_AGENT') 
    if agent and re.search('MSIE',agent):
        response = HttpResponse(mimetype="application/vnd.ms-excel")
        response['Content-Disposition'] ='attachment; filename=%s' % urlquote(fname)
    else:
        response = HttpResponse(mimetype="application/ms-excel")
        response['Content-Disposition'] ='attachment; filename=%s' % smart_str(fname)
    wb.save(response)
    return response