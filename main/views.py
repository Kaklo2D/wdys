# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Tag
from django.core.exceptions import ObjectDoesNotExist

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
#    try:
#        tag = Tag.objects.get(pk=1)
#        print(tag)
#    except ObjectDoesNotExist:
#        print "Either the entry or blog doesn't exist."
    t = loader.get_template('comment.html')
#   c = RequestContext(request, {"tag":tag})
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def upload(request):
    t = loader.get_template("upload.html")
    c = RequestContext(request)
    return HttpResponse(t.render(c))