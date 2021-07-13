import csv
import io

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# ViewSets define the view behavior.
from api_csv.models import Transaction
from .serializer import UploadSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        csv_file = request.FILES['file_uploaded']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Transaction.objects.update_or_create(
                customer=column[0],
                item=column[1],
                total=column[2],
                quantity=column[3],
                date=column[4],
            )
        response = "POST API and you have uploaded a  file"
        return Response(response)


