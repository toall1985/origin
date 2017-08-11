def clean_name(name):
	name = name.replace('&amp;','&').replace('amp;','').replace('#039;','\'').replace('&acute;','\'').replace('&\'','\'').replace('&quot;','"').replace('</div>','')
	name = name.replace('\n','').replace('<i class="icon_hd"></i>','')
	return name
	
def clean_number(name):
	name = name.lower().replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6')
	name = name.lower().replace('seven','7').replace('eight','8').replace('nine','9').replace('ten','10').replace('eleven','11').replace('twelve','12')
	name = name.lower().replace('thirteen','13').replace('fourteen','14').replace('fifteen','15').replace('sixteen','16').replace('seventeen','17').replace('eighteen','18')
	return name
	