from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, "ruzilya3_1/index.html")

def about(request):
    fio = "Салимова Рузиля Азатовна"
    height = "160 см"
    weight = "43 кг"
    age = "16 лет"
    data = {"fio" : fio, "height" : height, "weight" : weight, "age" : age}
    return TemplateResponse(request, "ruzilya3_1/about.html", context = data)

def contacts(request):
    tel = "+79875876196"
    cont = "@Ruziya0_0"
    data = {"tel" : tel, "cont" : cont}
    return TemplateResponse(request, "ruzilya3_1/contacts.html", context = {"info": data})
