from django.http import JsonResponse
import requests

def get_sorted_shops(request):
    if request.method == 'GET':
        # Send HTTP GET request to the API endpoint
        response = requests.get("https://api.offch.com/api/shops?limit=10")
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the JSON data from the response
            data = response.json()
            
            # Sort the shops based on the number of coupons
            sorted_shops = sorted(data['results'], key=lambda x: x['num_of_coupons'], reverse=True)
            
            return JsonResponse(sorted_shops, safe=False)
        else:
            # If the request was unsuccessful, return an error message
            return JsonResponse({'error': 'Unable to fetch data from the API'}, status=500)
    
    elif request.method == 'POST':
        # Handle POST request if needed
        # Example: If you want to post something to the API
        # post_data = request.POST.get('data')
        # response = requests.post("https://api.offch.com/api/", data=post_data)
        # return JsonResponse(response.json())

        return JsonResponse({'error': 'POST method not supported'}, status=405)

    