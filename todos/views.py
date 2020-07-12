from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from .models import Todo


def index(request):
    return HttpResponse("todos:index")


class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "todos"

    def get_queryset(self):
        return Todo.objects.all()


def create(request):
    todo = Todo(title=request.POST["title"])
    todo.save()
    return HttpResponseRedirect(reverse("todos:index"))


def update(request):
    process = []

    try:
        update_request = request.POST.getlist("todo")

        for todo in Todo.objects.all():
            todo.status = bool(str(todo.id) in update_request)

            process.append(todo)

    except (KeyError, Todo.DoesNotExist):
        return render(request, "index.html", {"error_message": "!!Error!!"})
    else:
        # 処理成功時に更新する
        for todo in process:
            todo.save()

        return HttpResponseRedirect(reverse("todos:index"))
