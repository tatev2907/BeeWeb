from django.shortcuts import render
from django.shortcuts import redirect
from .models import URLs
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from shortening.settings import SHORT_URL_LENGTH_BOUNDS
import random
import hashlib


def home(request):
    return render(request, 'main/index.html')


def shortener(request):
    url = request.GET["url"]
    print(url)
    try:
        check = URLs.objects.get(targetURL=url)
        shortURL = getattr(check, 'shortURL')
    except URLs.DoesNotExist:
        hashObject = hashlib.md5(url.encode('utf-8'))
        min = SHORT_URL_LENGTH_BOUNDS[0]
        max = SHORT_URL_LENGTH_BOUNDS[1]
        a = random.randrange(min, max)
        shortURL = hashObject.hexdigest()[:a]
        random_user = User.objects.order_by('?')[0]
        entry = URLs(shortURL=shortURL, targetURL=url, SubUser=random_user)
        entry.save()
    return render(request, 'main/index.html', {'shortURL': shortURL})


def goto(request, inputURL):
    if inputURL[:1] == '!':
        inputURL = inputURL[1:]
        tobject = get_object_or_404(URLs, shortURL=inputURL)
        uid = tobject.SubUser.pk
        user = User.objects.get(id=uid)
        return render(request, 'main/description.html', {'object': tobject, 'user': user})
    else:
        target = get_object_or_404(URLs, shortURL=inputURL)
        targetURL = target.targetURL
        target.countV = target.countV + 1
        target.save()
    return redirect(targetURL)
