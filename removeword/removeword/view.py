from django.http  import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse(render(request,"index.html"))
def remove(request):
    original_text=request.POST.get("text","")
    s=""
    remove_charcter=request.POST.get("remove","")
    check_upper=request.POST.get("upper","off")
    remove_space=request.POST.get("space","off")
    for i in original_text:
        if i!=remove_charcter:
            s+=i
    if check_upper=="on":
        s=s.upper()
    if remove_space == "on":
        s=s.replace("  "," ")
    new = {"new_text":s, "removed": original_text.count(remove_charcter)}
    return HttpResponse(render(request, "new.html", new))