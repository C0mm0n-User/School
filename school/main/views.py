from django.shortcuts import render
import os


def index(request):
    return render(request, 'main/main.html')


def students(request):
    return render(request, 'main/students.html')


def parents(request):
    return render(request, 'main/parents.html')


def files(request):
    directory = 'main/static/main/download'
    arr = os.listdir(directory)
    var_list = {
        "files_to_download": [],
        "path_name": "http://127.0.0.1:8000/static/main/download/"
    }
    var_list["files_to_download"].extend(arr)

    return render(request, 'main/files.html', var_list)


def gallery(request):
    directory = 'main/static/main/img/gallery'
    arr = os.listdir(directory)
    var_list = {
        "images": [],
        "path_name": "http://127.0.0.1:8000/static/main/img/gallery/"
    }
    var_list["images"].extend(arr)

    return render(request, 'main/gallery.html', var_list)


def achievements(request):
    directory = 'main/static/main/img/achievements'
    arr = os.listdir(directory)
    var_list = {
        "images": [],
        "path_name": "http://127.0.0.1:8000/static/main/img/achievements/"
    }
    var_list["images"].extend(arr)

    return render(request, 'main/achievements.html', var_list)


if __name__ == '__main__':

    directory_ = "static/main/download"
    arr_ = os.listdir(directory_)

    print(arr_)
