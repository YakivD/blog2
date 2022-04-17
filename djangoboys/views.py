from django.shortcuts import render


def post_list(request):
    print(dir(request))
    return render(request, 'djangoboys/post_list.html', {})
