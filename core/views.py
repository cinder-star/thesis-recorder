from rest_framework import generics
from rest_framework.response import Response


class InventoryListCreateAPIView(generics.ListCreateAPIView):
    def get_serializer(self, *args, **kwargs):
        kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        resp = super().list(self, request, *args, **kwargs)
        ret_resp = {"status": resp.status_code, "data": resp.data}
        return Response(ret_resp)
