
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination

from records.serializers import RecordSerializer
from records.models import Record

# Create your views here.


class GetRecordsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    pagination_class.max_page_size = 100
    pagination_class.page_size_query_param = 'size'
    pagination_class.page_query_param = 'page'

    def get(self, request):
        records = Record.objects.filter(user=request.user, is_deleted=False)
        paginated_queryset = self.pagination_class().paginate_queryset(records, request)
        serializer = RecordSerializer(paginated_queryset, many=True)
        return Response({
            "count": records.count(),
            "results": serializer.data,    
        }, status=status.HTTP_200_OK)
