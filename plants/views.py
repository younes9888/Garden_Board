from django.urls import reverse
from multiprocessing import context
from django.views.generic import View,TemplateView,ListView,DetailView
from django.shortcuts import render
from .models import Plant,Garden,Garden_tips
from django.shortcuts import redirect

from plants.form import CommentForm

# Create your views here.
def index_view(request):
    index_tips=Garden_tips.objects.all().last()
    index_feature_garden=Garden.objects.all().order_by('id')[:4][::-1]
    index_plant_of_theweek=Plant.objects.all().last()
    index_top_three_plants=Plant.objects.all().order_by('id')[:3][::-1]

    context={'index_tips':index_tips,'index_feature_garden':index_feature_garden,'index_plant_of_theweek':index_plant_of_theweek,'index_top_three_plants':index_top_three_plants}
    return render(request, 'index.html',context)
    

class PlantListView(ListView):
    template_name='plant_list.html'
    model=Plant
    context_object_name='Plant'

class PlantDetailView(DetailView):
    template_name= 'plant_detail.html'
    model=Plant
    context_object_name='Plantt'
    form=CommentForm

    def post(self,request,*args,**kwargs):
        print('entre to post_comment functionnnnnnnnnnnnnnnnnnnnnnnnnn ')
        form=CommentForm(request.POST)
        if form.is_valid():
            print('form is validddddddd')
            plant_commentt=self.get_object()
            form.instance.user=request.user
            form.instance.plant_comment=plant_commentt
            form.save()
            print('form====================',form)
            return redirect(reverse('plants:plant', kwargs={'pk':plant_commentt.id}))

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=self.form
        print('contex===',context)
        return context







class GardenListView(ListView):
    template_name='garden_list.html'
    model=Garden
    context_object_name='Garden'

class GardenDetailView(DetailView):
    template_name= 'garden_detail.html'
    model=Garden
    context_object_name='Gardenn'

      
class Garden_tips_ListView(ListView):
    template_name='gardening_tips_list.html'
    model=Garden_tips
    context_object_name='Garden_tips'

class Garden_tips_DetailView(DetailView):
    template_name= 'gardening_tips_detail.html'
    model=Garden_tips
    context_object_name='Garden_tip'