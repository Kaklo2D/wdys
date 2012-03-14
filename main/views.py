# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

def main(request):
    t = loader.get_template('test.html')
    c = Context({ 'string': "blah" })
    
    return HttpResponse(t.render(c))