from django.http import JsonResponse
from .models import User

def user_info(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            'id': user.id,
            'name': user.name,
            'addresses': list(user.addresses.all().values())
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=404)
