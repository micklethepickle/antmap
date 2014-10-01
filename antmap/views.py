# encoding=utf8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from antmap.models import Ant, Species, Document
from antmap.forms import DocumentForm
from antmap.gps_converter import to_decimal


def ant_list(request):
	
	context = RequestContext(request)

	ant_list = Ant.objects.order_by('landmark')

	for ant in ant_list:
		
		if ant.GPS_lat:
			print ant.GPS_lat.encode('UTF-8')
			ant.GPS_lat = to_decimal(ant.GPS_lat.encode('UTF-8'))
			ant.GPS_long = to_decimal(ant.GPS_long.encode('UTF-8'))



	try:
		ant_list_min = list(ant_list)
		for index, ant in enumerate(ant_list_min):
			if index != 0 or index != (len(ant_list_min)-1):
				if ant.landmark:
					if ant.landmark == ant_list_min[index-1].landmark :
						ant_list_min.remove(ant_list_min[index-1])
					if (ant.GPS_lat == ant_list_min[index-1].GPS_lat) and (ant.GPS_long == ant_list_min[index-1].GPS_long):
						ant_list_min.remove(ant_list_min[index-1])
	except:
		ant_list_min = ant_list


	context_dict = {'ant_list': ant_list, 'ant_list_min': ant_list_min}
	return render_to_response('antmap/antlist.html', context_dict, context)


if __name__ == "__main__":
	ant_list = Ant.objects.order_by('landmark')
	for ant in ant_list:
                if ant.GPS_lat:
			print ant.GPS_lat

def upload_doc(request):
	print "HEEEEEEEEEEEEEEEEEEEEEEEEEEYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
	context = RequestContext(request)
	if request.method == 'POST':
		print"QWWWWQERQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ"
		form = DocumentForm(request.POST, request.FILES)
		print form
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			print "HEEEYY JUDE DONT BE AFFFFRRRAaaaaaaaaaaaaAAAAAAAAAAIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDD"
			print request.FILES['docfile']
			newdoc.save()
			return HttpResponseRedirect('/antmap/antlist/')
	else:
		form = DocumentForm()

	return render_to_response('antmap/upload.html',{'form':form},context)

