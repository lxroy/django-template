from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import add


class MyAPIView(APIView):
    def get(self, request):
        result = add.delay(2, 3)
        return Response({"task_id": result.id})
