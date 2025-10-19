import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Agent, Position

@csrf_exempt
def update_location(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)
    try:
        data = json.loads(request.body)
        name = data["name"]
        lat = float(data["latitude"])
        lon = float(data["longitude"])
    except Exception as e:
        return JsonResponse({"error": f"Bad payload: {e}"}, status=400)

    agent, _ = Agent.objects.update_or_create(
        name=name, defaults={"latitude": lat, "longitude": lon}
    )
    Position.objects.create(agent=agent, latitude=lat, longitude=lon)
    return JsonResponse({"ok": True})

def get_positions(request):
    """Tarix nuqtalari (so‘nggi N dona). ?name=Malika&limit=200"""
    name = request.GET.get("name")
    limit = int(request.GET.get("limit", 200))
    qs = Position.objects.select_related("agent")
    if name:
        qs = qs.filter(agent__name=name)
    pts = [
        {
            "name": p.agent.name,
            "latitude": p.latitude,
            "longitude": p.longitude,
            "timestamp": p.timestamp.isoformat(),
        }
        for p in qs.order_by("-timestamp")[:limit]
    ]
    pts.reverse()  # vaqt bo‘yicha ko‘tarilish
    return JsonResponse({"positions": pts})

#def map_view(request):
    agent_name = request.GET.get("name", "Malika")
    return render(request, "map.html", {"agent_name": agent_name})

def map_view(request):
    agent_name = request.GET.get("name", "Malika")
    print("DEBUG agent_name repr:", repr(agent_name))
    return render (request, "map.html", {"agent_name": agent_name})