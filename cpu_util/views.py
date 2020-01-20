from cpu_util.serializers import MessageSerializer
from cpu_util.models import Record
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.pagination import LimitOffsetPagination


class CreateRecord(APIView):
    serializer_class = MessageSerializer
    permission_classes = (AllowAny,)

    def post(self, request,):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetRecords(APIView, LimitOffsetPagination):
    serializer_class = MessageSerializer
    template_name = 'results.html'
    renderer_classes = (TemplateHTMLRenderer,)
    model = serializer_class.Meta.model
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = self.model.objects.all().order_by('-record_datetime')[:100]
        return Response({'records': queryset})

    # def list(self, request, *args, **kwargs):
    #     response = super(GetRecords, self).list(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'data': response.data}, template_name='results.html')
    #     return response
