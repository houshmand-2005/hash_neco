from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
import reviews
from .forms import ReviewForm
from .models import Review
from django.views import View


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/reviews.html"
    success_url = "/thank_you"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/reviews.html", {
    #         "form": form
    #     })
    #
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank_you")
    #     return render(request, "reviews/reviews.html", {
    #         "form": form
    #     })


class ThankYou(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewList(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data


class DetailReview(DetailView):
    template_name = "reviews/detail_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
