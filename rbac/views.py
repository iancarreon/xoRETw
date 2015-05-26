from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))

@login_required
def dashboard(request):
    user_id = request.user.id
    object_type = int(request.GET.get('object_type', 1))
    
    print 'user_id = request.user.id is ', user_id
    print 'object_type ', object_type
    
    
    #option = int(request.GET.get('object', 0))
    #return render_to_response('dashboard.html', {}, context_instance=RequestContext(request))
    return render_to_response('dashboard.html', {'object_type':object_type}, context_instance=RequestContext(request))


