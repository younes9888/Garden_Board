from tkinter.messagebox import NO
from django.views.generic import CreateView,UpdateView
from django.http import HttpResponseRedirect
from .models import Action_garden,Action_garden_tips,Action_plant
from plants.models import Garden,Plant,Garden_tips
from django.urls import reverse_lazy
# Create your views here.


class LikeplantView(CreateView,UpdateView):
    http_method_names= ['post']
    model= Action_plant
    success_url=reverse_lazy('plants:plants')
    fields=['liked']

    def get_object(self, queryset=None):
        return Action_plant.objects.get_or_create(
            user=self.request.user,
            plant=Plant.objects.get(
                id=self.kwargs.get('plant_id')
            )
        )[0]
    def _like_or_dislike(self):
        if self.request.POST.get('like'):
            return True
        if self.request.POST.get('dislike'):
            return False
        return None
    def form_valid(self,form):
        interaction=self.get_object()
        interaction.liked=self._like_or_dislike()
        interaction.save()
        return HttpResponseRedirect(self.success_url)





class LikegardenView(CreateView,UpdateView):
    http_method_names= ['post']
    model= Action_garden
    success_url=reverse_lazy('plants:gardens')
    fields=['liked']

    def get_object(self, queryset=None):
        return Action_garden.objects.get_or_create(
            user=self.request.user,
            garden=Garden.objects.get(
                id=self.kwargs.get('garden_id')
            )
        )[0]
    def _like_or_dislike(self):
        if self.request.POST.get('like'):
            return True
        if self.request.POST.get('dislike'):
            return False
        return None
    def form_valid(self,form):
        interaction=self.get_object()
        interaction.liked=self._like_or_dislike()
        interaction.save()
        return HttpResponseRedirect(self.success_url)


class LikeGarden_tips_View(CreateView,UpdateView):
    http_method_names= ['post']
    model= Action_garden_tips
    success_url=reverse_lazy('plants:garden_tips')
    fields=['liked']

    def get_object(self, queryset=None):
        return Action_garden_tips.objects.get_or_create(
            user=self.request.user,
            garden_tips=Garden_tips.objects.get(
                id=self.kwargs.get('garden_tips_id')
            )
        )[0]
    def _like_or_dislike(self):
        if self.request.POST.get('like'):
            return True
        if self.request.POST.get('dislike'):
            return False
        return None
    def form_valid(self,form):
        interaction=self.get_object()
        interaction.liked=self._like_or_dislike()
        interaction.save()
        return HttpResponseRedirect(self.success_url)



