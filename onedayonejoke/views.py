from onedayonejoke.models import Joke, Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile

@csrf_exempt
def jokes(request):
    if request.method == 'POST':
        # CREATE A JOKE MODLE
        req = json.loads(request.raw_post_data)
        title = req['title']
        content = req['content']
        weight = req['weight']
        joke = Joke(title=title, content = content, weight = weight)
        joke.save()
        # save the tags for a joke
        tags = req['tags']
        print 'tags ', tags
        joke.add_tags(tags)
        # save the image for a joke.
        image_id = req['imageId']
        photo = Photo.objects.get(id = image_id)
        joke.image = photo
        joke.save()

        return HttpResponse(json.dumps({"status": "1", "joke":joke.to_json(), "msg": "success"}), content_type= 'Application/json')
    elif request.method == 'GET':
        # GET LIST OBJECT
        type = request.GET.get('type', 'new')
        if type == 'new':
            page = request.GET.get('page', 1)
            count = request.GET.get('count', 5)
            return list_page(type, page, count)
        elif type == 'hot':
            page = request.GET.get('page', 1)
            count = request.GET.get('count',5)
            return list_page(type, page, count)

    return HttpResponse(json.dumps({"status": "0", "msg": "fail"}), content_type= 'Application/json')

def handle_uploaded_file(filename, f):
    destination = open('some/file/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        photo = Photo()
        photo.image = request.FILES.get('image')
        try:
            photo.save()
        except:
            return HttpResponse(json.dumps({"status": "0", "msg": "Upload image failed"}), content_type= 'Application/json')
        return HttpResponse(json.dumps({"status": "1", "image": photo.to_json(), "msg": "Upload image success"}), content_type= 'Application/json')
    return HttpResponse("HelloWorld")

@csrf_exempt
def joke(request, joke_id):
    if request.method == 'GET':
        # get a joke object by id
        joke = Joke.objects.get(id=joke_id)
        return HttpResponse(json.dumps({"joke": joke.to_json(), "status": "1", "msg": "success"}), content_type= 'Application/json')
    elif request.method == 'DELETE':
        # delete a joke by id
        print 'request delete id %s ' % joke_id
        Joke.objects.filter(id=joke_id).delete()
        return HttpResponse(json.dumps({"status": "1", "msg": "success"}), content_type= 'Application/json')
    elif request.method == 'PUT':
        # update a joke by id
        req = json.loads(request.raw_post_data)
        title = req['title']
        content = req['content']
        weight = req['weight']
        Joke.objects.filter(id = joke_id).update(title=title, content = content, weight = weight)
        return HttpResponse(json.dumps({"status": "1", "msg": "success"}), content_type= 'Application/json')

    return HttpResponse(json.dumps({"status": "0", "msg": "fail"}), content_type= 'Application/json')

def list_page(type, page, count):
    if type == "new":
        objects = Joke.objects.order_by('-create_time')
    elif type == "hot":
        objects = Joke.objects.order_by('-weight')
    paginator = Paginator(objects, count) # Show count size object per page

    try:
        jokes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jokes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jokes = paginator.page(paginator.num_pages)

    data = []
    for joke in jokes:
        data.append(joke.to_json())
    return HttpResponse(json.dumps({"status":1, "msg":"success", "list": data, "page_size": paginator.num_pages, "page_index": page}), content_type='Application/json')

@csrf_exempt
def joke_weight(request):
    if request.method == 'POST':
        req = json.loads(request.raw_post_data)
        joke_id = req['id']
        count = req['count']
        joke = Joke.objects.get(id=joke_id)
        joke.weight = joke.weight+count
        joke.save()
        return HttpResponse(json.dumps({"status": "1", "msg": "success"}), content_type= 'Application/json')
    return HttpResponse(json.dumps({"status": "0", "msg": "fail"}), content_type= 'Application/json')
