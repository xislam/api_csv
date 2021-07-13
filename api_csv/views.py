import csv
import io

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# ViewSets define the view behavior.
from api_csv.models import Transaction, Gem, User
from .serializer import UploadSerializer, TransactionSerializer, GemSerializer, UsersSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    # def get(self, request):
    #     pass

    def create(self, request):
        file_serializer = UploadSerializer(data=request.data)
        file_serializer.is_valid(raise_exception=True)
        file = file_serializer.validated_data['file_uploaded']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        tran = []
        for row in reader:
            dict_row = dict(row)
            user_serializer = UsersSerializer(data=dict_row)
            user_serializer.is_valid(raise_exception=True)
            user, created = User.objects.get_or_create(username=user_serializer.validated_data['username'])

            gem_serializer = GemSerializer(data=dict_row)
            gem_serializer.is_valid(raise_exception=True)
            gem, created = Gem.objects.get_or_create(text=gem_serializer.validated_data['text'])

            tran_serializer = TransactionSerializer(data=dict_row)
            tran_serializer.is_valid(raise_exception=True)

            recording = Transaction(
                customer=user,
                item=gem,
                total=tran_serializer.validated_data['total'],
                quantity=tran_serializer.validated_data['quantity'],
                date=tran_serializer.validated_data['date'],
            )
            tran.append(recording)

        Transaction.objects.bulk_create(tran)

        content = []
        for recordings in tran:
            response_serializer = TransactionSerializer(recordings)
            content.append(response_serializer.data)
        return Response(content, status=status.HTTP_201_CREATED)

    # def create(self, request):
    #     csv_file = request.FILES['file_uploaded']
    #     data_set = csv_file.read().decode('UTF-8')
    #     io_string = io.StringIO(data_set)
    #     next(io_string)
    #     for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #         _, created = Transaction.objects.update_or_create(
    #             customer=column[0],
    #             item=column[1],
    #             total=column[2],
    #             quantity=column[3],
    #             date=column[4],
    #         )
    #     response = "POST API and you have uploaded a  file"
    #     return Response(response)
