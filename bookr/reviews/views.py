from django.shortcuts import render


def index(request):
    name = "Brandon"
    return render(request, "base.html", {"name": name})


def book_search(request):
    # below we make a request using method GET, so we can look at the URL when
    # we then use lil get, to view the search parameter of the URL. ie the users search terms.
    # if the user doesn't enter anything in a form using GET then search_text will return an empty string

    search_text = request.GET.get("search", "")
    return render(request, "search_result.html", {"search_text": search_text})
