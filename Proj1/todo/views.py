from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import TodoItem
from .utils import safe_exec  # Import the safe_exec function



def home(request):
    return render(request, "home.html")

def about(request, *a, **u):
    print(request.user)
    test = 1234
    
    code = "test = 456"
    exec(code, {})
    #test = 4567
    #test = 456

    globals_dict = {}
    exec(code, globals_dict)
    #dynamic_function = types.FunctionType(globals_dict['dynamic_function'].__code__, globals_dict)


    return render(request, "about.html", {"test": test})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos" : items})

def doclist(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos" : items})

def doc(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos" : items})

@csrf_exempt
def execute_code(request):
    
    if request.method == "POST":
        code = request.POST.get('code', '')
        
        if not code:
            return HttpResponse("No code provided.", status=400)
        
        globals_dict, locals_dict = {}, {}
        
        try:
            globals_dict, locals_dict = safe_exec(code, globals_dict, locals_dict)
            dynamic_function = locals_dict.get('dynamic_function')
            
            if not dynamic_function:
                return HttpResponse("No function 'dynamic_function' found in the code.", status=400)
            
            # Example parameters for dynamic_function
            result = dynamic_function(10, 20)
            
            return JsonResponse({'result': result})
        except Exception as e:
            return HttpResponse(f"Error executing code: {str(e)}", status=500)
    
    return HttpResponse("Send a POST request with 'code' in the body.", status=405)
