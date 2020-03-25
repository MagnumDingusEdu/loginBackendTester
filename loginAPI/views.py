from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from loginAPI.models import UserModel
import secrets

@csrf_exempt
def defaultView(request):
    return JsonResponse({"error":"unauthorized"}, status=403)
@csrf_exempt
def loginView(request):
    if request.method == "POST":
        user = request.POST.get('user', False)
        passw = request.POST.get('pass', False)
        print(user, passw)
        if user and passw:
            user = UserModel.objects.filter(username=user, password=passw).first()
            if not user:
                return JsonResponse({"authorized":False}, status=403)
            else:
                user.access_token = secrets.token_hex(20)
                user.loggedin = True
                user.save()
                return JsonResponse({
                    "authorized":True,
                    "name":user.name,
                    "token":user.access_token,


                })
                print("Successfully logged in")
            pass
        else:
            return JsonResponse({"error":"Bad request"}, status=400)
    return JsonResponse({"error":"403 Bad Request"}, status=400)

@csrf_exempt
def logoutView(request):
    if request.method == 'POST':
        token = request.POST.get('token', False)

        if not token:
            return JsonResponse({"error":"Bad request"}, status=400)
        else:
            user = UserModel.objects.filter(access_token = token).first()

            if user:
                user.access_token = ""
                user.loggedin = False
                user.save()
                return JsonResponse({"authorized":True, "status":"logged out successfully"})
            else:
                return JsonResponse({"authorized":False}, status=403)
    else:
        return JsonResponse({"error":"bad request"}, status=400)


@csrf_exempt
def authView(request):
    if request.method == "POST":
        # username = request.POST.get('username', False)
        token = request.POST.get('token', False)
        print(token)
        if token:
            user = UserModel.objects.filter(access_token=token)

        if user:
            if len(user) == 1:
                user = user.first()
                return JsonResponse({"authorized":True})
        else:
            return JsonResponse({"authorized":False}, status=403)

@csrf_exempt
def registerView(request):
    if request.method == "POST":
        usern = request.POST.get('user', False)
        passw = request.POST.get('pass', False)
        name=request.POST.get('name',False)

        if (not usern ) or (not passw):
            return JsonResponse({"error":"Bad Request"}, status=400)
        UserModel.objects.create(
            name=name,
            username=usern,
            password=passw

        )
        return JsonResponse({"status":"created successfully"})

    else:
        return JsonResponse({"error":"bad request"}, status=400)