def handle_uploaded_file(f,ruta):  
    with open(ruta+f.name,'wb+') as destination:  
    	for chunk in f.chunks():
    		destination.write(chunk) 