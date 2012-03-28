# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Tag, CommonImage
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

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
    try:
        tag = Tag.objects.all()
        print(tag)
    except ObjectDoesNotExist:
        print "Either the entry or blog doesn't exist."
    t = loader.get_template('comment.html')
#   c = RequestContext(request, {"tag":tag})
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def upload(request):
    t = loader.get_template("upload.html")
    c = RequestContext(request)
    return HttpResponse(t.render(c))

@csrf_exempt
def uploadImages(request):
    if request.method == "POST":
        image = CommonImage()
        image.img.save(
            "patata.jpg",
            request.FILES['Filedata'],
            save=True
        )
    
    print("shit2\n")
    
    t = loader.get_template("upload.html")
    c = RequestContext(request)
    return HttpResponse(t.render(c))
    
def step2(request):
    t = loader.get_template('step2.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
    
def step3(request):
    t = loader.get_template('step3.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
    
def publish(request):
    t = loader.get_template('publish.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))