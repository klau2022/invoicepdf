#!/usr/bin/env python
# -*- coding: utf-8 -*-

$ pip install borb 
from borb.pdf.document import Document
from borb.pdf.page.page import Page

# Create document
pdf = Document()

# Add page
page = Page()
pdf.append_page(page)

# New imports
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from decimal import Decimal

page_layout = SingleColumnLayout(page)
page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)

# New import
from borb.pdf.canvas.layout.image.image import Image


page_layout.add(    
        Image(        
        "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/mmdbuwtygmnv2dooj6th",        
        width=Decimal(128),        
        height=Decimal(128),    
        ))
# New imports
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from datetime import datetime
import random

def _build_invoice_information():    
    table_001 = Table(number_of_rows=3, number_of_columns=3)
	
    table_001.add(Paragraph("[Unit 2 Coolham Road West Grinstead]"))    
    table_001.add(Paragraph("Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))    
    now = datetime.now()    
    table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year)))
	
    table_001.add(Paragraph("[Horsham RH13 8LN London]"))    
    table_001.add(Paragraph("Invoice #", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
    table_001.add(Paragraph("%d" % random.randint(1000, 10000)))   
	
    table_001.add(Paragraph("[accounts@versadex.xyz]"))    
    table_001.add(Paragraph("Due Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
    table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year))) 

page_layout = SingleColumnLayout(page)
page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)
page_layout.add(    
    Image(        
        "https://s3.stackabuse.com/media/articles/creating-an-invoice-in-python-with-ptext-1.png",        
        width=Decimal(128),        
        height=Decimal(128),    
        ))

# Invoice information table  
page_layout.add(_build_invoice_information())  
  
# Empty paragraph for spacing  
page_layout.add(Paragraph(" "))

# New import
from borb.pdf.pdf import PDF

with open("output.pdf", "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, pdf)

# New imports
from borb.pdf.canvas.color.color import HexColor, X11Color

def _build_billing_and_shipping_information():  
    table_001 = Table(number_of_rows=2, number_of_columns=1)  
    table_001.add(  
        Paragraph(  
            "Recipient",  
            background_color=HexColor("263238"),  
            font_color=X11Color("White"),  
        )  
    )  
   
    table_001.add(Paragraph("[Creator handle]"))          
    table_001.add(Paragraph("[Wallet address]"))        
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))  
    table_001.no_borders()  
    return table_001

# Invoice information table
page_layout.add(_build_invoice_information())

# Empty paragraph for spacing
page_layout.add(Paragraph(" "))

# Billing and shipping information table
page_layout.add(_build_billing_and_shipping_information())

# New import
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.table.table import TableCell


def _build_itemized_description_table(self):  
    table_001 = Table(number_of_rows=5, number_of_columns=4)  
    for h in ["CREATOR", "MONTH", "PRICE", "IMPRESSIONS"]:  
        table_001.add(  
            TableCell(  
                Paragraph(h, font_color=X11Color("White")),  
                background_color=HexColor("016934"),  
            )  
        )  
  
    odd_color = HexColor("BBBBBB")  
    even_color = HexColor("FFFFFF")  
    for row_number, item in enumerate([("The Rocking Uniquehorns", "July 2022", "5 CPM", 1241)]):  
        c = even_color if row_number % 2 == 0 else odd_color  
        table_001.add(TableCell(Paragraph(item[0]), background_color=c))  
        table_001.add(TableCell(Paragraph(str(item[1])), background_color=c))  
        table_001.add(TableCell(Paragraph("$ " + str(item[2])), background_color=c))  
        table_001.add(TableCell(Paragraph("$ " + str(item[1] * item[2])), background_color=c))  
	  
	# Optionally add some empty rows to have a fixed number of rows for styling purposes
    for row_number in range(3, 10):  
        c = even_color if row_number % 2 == 0 else odd_color  
        for _ in range(0, 4):  
            table_001.add(TableCell(Paragraph(" "), background_color=c))  
  
    table_001.add(TableCell(Paragraph("Subtotal", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT,), col_span=3,))  
    table_001.add(TableCell(Paragraph("$ 1,180.00", horizontal_alignment=Alignment.RIGHT)))  
    table_001.add(TableCell(Paragraph("Discounts", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT,),col_span=3,))  
    table_001.add(TableCell(Paragraph("$ 177.00", horizontal_alignment=Alignment.RIGHT)))  
    table_001.add(TableCell(Paragraph("Taxes", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT), col_span=3,))  
    table_001.add(TableCell(Paragraph("$ 100.30", horizontal_alignment=Alignment.RIGHT)))  
    table_001.add(TableCell(Paragraph("Total", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT  ), col_span=3,))  
    table_001.add(TableCell(Paragraph("$ 1163.30", horizontal_alignment=Alignment.RIGHT)))  
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))  
    table_001.no_borders()  
    return table_001
