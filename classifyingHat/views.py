from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .forms import ResultsIdForm

from .utils.house_data import get_house_data


def index(request, results_id=''):
    form = ResultsIdForm()

    return render(request, 'classifyingHat/index.html', {'form': form, 'results_id': results_id})

def get_results(request):
    results_id = request.GET["results_id"]
    try:
        data = get_house_data(results_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse(data)