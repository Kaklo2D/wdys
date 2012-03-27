# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, Context, loader


from django.conf import settings

def main(request):
    t = loader.get_template('main.html')
    indexes = range(1,13)
    c = RequestContext(request, { 'indexes': indexes })
    return HttpResponse(t.render(c))

def make(request):
    t = loader.get_template('make.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
    
def comment(request):
    t = loader.get_template('comment.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))