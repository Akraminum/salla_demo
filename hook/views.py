from rest_framework import generics
from rest_framework.response import Response
import json

from hook.event_handlers.event_mapper import EventMapper
from hook.serialiserzes import WebhookPayloadSerializer

from django.db import connection


class EventAPIView(generics.GenericAPIView):

    def post(self, request):
        # log data to file
        # print(request.data)
        with open('events.json', 'a') as f:
            f.write(json.dumps(request.data, indent=4) + '\n\n')


        serializer = WebhookPayloadSerializer(data=request.data)
        if not serializer.is_valid():
            # log errors
            return Response()


        event = serializer.validated_data.get("event")
        merchant = serializer.validated_data.get("merchant")
        data = serializer.validated_data.get("data")
        

        event_handler = EventMapper.get_event_handler(event) # object
        if event_handler:
            succsess = event_handler.handle_event(merchant, data)
            if succsess:
                [print(q,'\n') for q in connection.queries]; print(len(connection.queries))      
                return Response({"handled": succsess})

        # errors logic
        # ...    
        [print(q,'\n') for q in connection.queries]; print(len(connection.queries))   
        return Response({"handled": succsess})