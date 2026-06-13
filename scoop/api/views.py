import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

load_dotenv()

orders = [] # list of dictionaries/JSON objects representing each order that needs to be done

@csrf_exempt
def add_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        orders.append(data)
        return JsonResponse({'status': 'success', 'waiting': len(orders)})
    else:
        print("Received a non-POST request")

@csrf_exempt
def get_orders(request):
    if request.method != 'GET':
        print("Received a non-GET request")
        return JsonResponse({'status': 'error'}, status=400)
    return JsonResponse({'orders': orders})

@csrf_exempt
def finish_order(request):
    if request.method == 'POST':
        if len(orders) != 0:
            orders.pop(0)
            return JsonResponse({'status': 'success'})
        else:
            print("No orders to finish")
            return JsonResponse({'status': 'error'}, status=400)
    else:
        print("Received a non-POST request")
        return JsonResponse({'status': 'error'}, status=400)

#   try {
#     const res = await fetch('/verses/get_verses', {
#       method: 'POST',
#       headers: { 'Content-Type': 'application/json' },
#       body: JSON.stringify({ sermon, tone })
#     });

#     if (!res.ok) throw new Error('Request failed');

#     const data = await res.json();
#     verses = data.verses || [];
#     renderVerses();
#     setStatus(false);
#   } catch (err) {
#     console.error(err);
#     verses = [];
#     document.getElementById('verses-list').innerHTML = `
#       <div class="panel-empty">
#         <div class="icon">⚠</div>
#         <p>Could not fetch passages. Please try again shortly.</p>
#       </div>`;
#     setStatus(false);
#   }

