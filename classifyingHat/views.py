from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .forms import ResultsIdForm

from .utils.house_data import get_house_data


def index(request):
    form = ResultsIdForm()

    return render(request, 'classifyingHat/index.html', {'form': form})


def results(request, results_id):
    data = get_house_data(results_id)

    return render(request, 'classifyingHat/results.html', data)

def get_results(request):
    results_id = request.GET["results_id"]
    data = get_house_data(results_id)

    return JsonResponse(data)