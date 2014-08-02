from django.shortcuts import render_to_response
from django.template import RequestContext
from antmap.models import Ant, Species

def ant_list(request):
	
	context = RequestContext(request)
	ant_list = Ant.objects.order_by('specimen_ID')
	context_dict = {'ant_list': ant_list}
	return render_to_response('antmap/antlist.html', context_dict, context)
	
