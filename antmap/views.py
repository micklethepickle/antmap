# encoding=utf8

from django.shortcuts import render_to_response
from django.template import RequestContext
from antmap.models import Ant, Species
from antmap.gps_converter import to_decimal

def ant_list(request):
	
	context = RequestContext(request)

	ant_list = Ant.objects.order_by('specimen_ID')
	
	for ant in ant_list:
		
		if ant.GPS_lat:
			print ant.GPS_lat.encode('UTF-8')
			ant.GPS_lat = to_decimal(ant.GPS_lat.encode('UTF-8'))
			ant.GPS_long = to_decimal(ant.GPS_long.encode('UTF-8'))

		
	context_dict = {'ant_list': ant_list}
	return render_to_response('antmap/antlist.html', context_dict, context)


if __name__ == "__main__":
	ant_list = Ant.objects.order_by('specimen_ID')
	for ant in ant_list:
                if ant.GPS_lat:
			print ant.GPS_lat
