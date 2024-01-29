from django.utils import timezone
# from .models import TranscendenceUser
class TranscendenceUserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Update the user last activity to now
            if request.user:
                user = request.user
                user.last_activity = timezone.now()
                user.save()
        except Exception as e:
            print(f"Error in UserActivityMiddleware: {e}")

        response = self.get_response(request)
        return response