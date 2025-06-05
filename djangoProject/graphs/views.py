from django.shortcuts import render
from django.views import View
from .bokeh_plot import create_scatter_plot
#from .python_code import create_scatter_plot

# Create your views here.
class CreatePlot(View):
    template_name = "graphs/create_plot.html"
    context_object_name = "object"
    success_message = "Successfully Updated!"
    def get(self, request):
        script, div = create_scatter_plot()
        return render(request, self.template_name, {"script": script, "div": div})
        #return render(request, self.template_name)