# @csrf_exempt
# def handle_upload(request):
#
#
#     if request.method == "POST":
#         type = request.POST.get('adType', None)
#
#         file = request.FILES.get("file", None)
#         if file:  # 处理附件上传到方法
#             try:
#                 handle_upload_file(file)
#
#             except Exception as e:
#                 pass
#                 data = str(e)
#                 res = 0
#                 result = {'res': res, 'data': data}
#                 content = json.dumps(result)
#                 return HttpResponse(content)
#
#
#     def handle_upload_file(filename):
#
#
#         """
#         handle_upload_file 上传文件
#         """
#         try:
#             path = os.path.dirname(os.path.dirname(__file__)) + '/static/ad/upload/'
#             print
#             path
#             if not os.path.exists(path):
#                 os.makedirs(path)
#             destination = open(path + filename.name, 'wb+')
#             for chunk in filename.chunks():
#                 destination.write(chunk)
#             destination.close()
#             res = 1
#         except Exception, e:
#             print e
#             res = 0
#             return res
