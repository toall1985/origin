def clean_name(name):
	name = name.replace('&amp;','&').replace('amp;','').replace('#039;','\'').replace('&acute;','\'').replace('&\'','\'').replace('&quot;','"').replace('</div>','')
	name = name.replace('\n','').replace('<i class="icon_hd"></i>','')
	return name