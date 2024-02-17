
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color

import os, csv
import cgitb; cgitb.enable()

rakshins = []
file = open("assets/rakshins.csv", "r", encoding = 'utf-8')
data = csv.reader(file)
for rakshin in data:
    rakshins.append(rakshin)

for i in rakshins:
        rname = i[0]
        college,location = i[1], i[2]
        if not os.path.exists(rname+".pdf"):
            pdfname = (rname+".pdf")
            c = canvas.Canvas(pdfname, pagesize = (862.5, 484.88))
            c.setTitle(rname+"'s Certificate One")
            c.drawImage("assets/cert-3.png", 0, 0, width = 862.5, height = 484.88)
            pdfmetrics.registerFont(TTFont('Allura', 'assets/allura.ttf'))
            pdfmetrics.registerFont(TTFont('Mont', 'assets/mont.ttf'))
            
            c.setFillColor("#003399")
            c.scale(1, 1)
            c.setFont("Mont", 20)
            c.drawCentredString(170.25, 250, rname)  
            c.setFont("Mont", 13)
            c.drawCentredString(170.25, 230, college+","+location)
            c.setFont("Allura", 20)  
            c.setFillColor(Color(0, 0, 0, alpha = 1))    
            c.drawCentredString(610.25, 250, rname)
            c.showPage()
            c.save()

            print(rname + " certificate generated.")
        else:   
            print(rname + " certificate already exists.")
            
            
            


