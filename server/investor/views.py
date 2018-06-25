from django.shortcuts import render

## View methods

# Registration
def investor_register_view(request):
    context = {}
    return render(request, 'investor/register.html', context)
