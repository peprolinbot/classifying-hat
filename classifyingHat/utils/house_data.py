from django.templatetags.static import static

from .predict_house import predict_house
from .big_five_scraper import get_test_results

HOUSE_TRAITS = {
    "hufflepuff": ['Hard-working', 'Patience', 'Fairness', 'Just', 'Loyalty', 'Modesty'],
    "slytherin": ['Resourcefulness', 'Determination', 'Pride', 'Cunning', 'Ambition', 'Self-preservation'],
    "gryffindor": ['Courage', 'Bravery', 'Determination', 'Daring', 'Nerve', 'Chivalry'],
    "ravenclaw": ['Wit', 'Learning', 'Wisdom', 'Acceptance', 'Intelligence', 'Creativity']
}

def get_house_data(results_id):
    results = get_test_results(results_id)
    name = predict_house(**results)

    logo = static(f'classifyingHat/house_logos/{name.lower()}.png')

    traits = ', '.join(HOUSE_TRAITS[name.lower()])

    return {'house_name': name, 
            'house_logo': logo,
            'house_traits': traits}