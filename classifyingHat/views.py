from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.templatetags.static import static

from .forms import ResultsIdForm

from .utils.predict_house import predict_house
from .utils.big_five_scraper import get_test_results
from .utils.house_traits import all_house_traits


def index(request):
    if request.method == 'POST':
        form = ResultsIdForm(request.POST)
        if form.is_valid():
            results_id = form.cleaned_data['results_id']
            return HttpResponseRedirect(reverse('classifyingHat:results', args=(results_id,)))
    else:
        form = ResultsIdForm()

    return render(request, 'classifyingHat/index.html', {'form': form})


def results(request, results_id):
    results = get_test_results(results_id)
    house_name = predict_house(**results)

    house_logo = static(f'classifyingHat/house_logos/{house_name.lower()}.png')

    house_traits = ', '.join(all_house_traits[house_name.lower()])

    return render(request, 'classifyingHat/results.html', {'house_name': house_name, 'house_logo': house_logo, 'house_traits': house_traits})
