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
