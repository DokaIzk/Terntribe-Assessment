from .serializers import *
from rest_framework import response, status, viewsets

class CauseViewSet(viewsets.ModelViewSet):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['cause_id'] = self.kwargs.get("pk")
        return context