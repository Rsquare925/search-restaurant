from django.shortcuts import render
from django.db.models import Q
from search_dishes.models import Restaurant

# Create your views here.


def search(request):
    query = request.GET.get("query", "")
    results = []

    if query:
        restaurants = Restaurant.objects.filter(Q(items__icontains=query))
        for restaurant in restaurants:
            items = restaurant.items  # No need to parse JSON
            matching_items = {
                key: value
                for key, value in items.items()
                if query.lower() in key.lower()
            }
            if matching_items:
                results.append(
                    {
                        "name": restaurant.name,
                        "location": restaurant.location,
                        "items": matching_items,
                    }
                )

    context = {
        "results": results,
        "query": query,
    }
    return render(request, "search.html", context)
