from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from .models import Banco, Agencia, Cliente, Conta
from .serializers import BancoSerializer, AgenciaSerializer, ClienteSerializer, ContaSerializer, ContaDepositoSerializer
from decimal import Decimal
from django.db.transaction import atomic


class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer

    @action(detail=True, methods=['get'], serializer_class=AgenciaSerializer)
    def agencias(self, request, *args, **kwargs):
        banco = self.get_object()
        agencias = self.get_serializer(banco.agencias, many=True)
        return response.Response(agencias.data)


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer

    @action(detail=True, methods=['get'], serializer_class=ContaSerializer)
    def contas(self, request, *args, **kwargs):
        agencia = self.get_object()
        contas = self.get_serializer(agencia.contas, many=True)
        return response.Response(contas.data)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=True, methods=['get'], serializer_class=ContaSerializer)
    def contas(self, request, *args, **kwargs):
        cliente = self.get_object()
        contas = self.get_serializer(cliente.contas, many=True)
        return response.Response(contas.data)


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    @atomic
    @action(detail=True, methods=['put'], serializer_class=ContaDepositoSerializer)
    def depositar(self, request, *args, **kwargs):
        conta = self.get_object()
        serializer = ContaDepositoSerializer(data=request.data)
        if serializer.is_valid():
            conta.saldo += Decimal(serializer.data['valor'])
            conta.save()
            return response.Response({'message': 'Depósito realizado com sucesso!'})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
