# ajax call 
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def iniFileUpload(request):
    if 'type' in request.GET:
        for key, val in request.GET.items():
            print('ke : ', key, "--- val :", val)
    else:
        print('this is main request')
    uploaded_files = request.FILES.get('myfile')
    error_message = 0
    error_message += validation.fileExtension(request, str(uploaded_files),str(inspect.stack()[0][3]))
    if error_message != 0:
        resp = {'error_message': error_message}
        return HttpResponse(json.dumps(resp), content_type='application/json')
    returnId = 767
    print(uploaded_files,)
    lib.handle_uploaded_file(uploaded_files, str(returnId))
    resp = {'success': True, "response": returnId, "name": str(uploaded_files)}
    return HttpResponse(json.dumps(resp), content_type='application/json')

#validation

def fileExtension(request,fileName,function):
    if function == 'iniFileUpload':
        extensions = ('.zip')
        if fileName and fileName.endswith(extensions):
            return 0
        else:
            messages.error(request, str(fileName) + " : is not " + extensions + " file.")
            return 1
	return 1

#handle uploaded file
def handle_uploaded_file(file,title):
    from apex import settings
    if file:
        destination = open(settings.UPLOAD_FILE_PATH+'/'+title+'.zip', 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return 0
    else:
        return 1
