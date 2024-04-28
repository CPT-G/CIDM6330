# python
import asyncio
import datetime
import json

# Django
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.generic.http import AsyncHttpConsumer

# Local
from em_planning_api.models import EMData


class SimpleEMDataConsumer(AsyncConsumer):
    async def print_emdata(self, message):
        print(f"WORKER: EM Emission: {message['data']}")


class EMDataConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        # Get all EM Data
        em_data = EMData.objects.all()
        # Serialize the EM Data
        data = json.dumps(
            [{"lat": em_data.lat, "long": em_data.long,
                "frequency": em_data.frequency} for em_data in em_data]
        )
        # Send the serialized data as a JSON response
        await self.send_response(
            200, data, headers=[(b"Content-Type", b"application/json")]
        )

    # Server-send event https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events
    async def handle(self, body):
        await self.send_headers(
            headers=[
                (b"Cache-Control", b"no-cache"),
                (b"Content-Type", b"text/event-stream"),
                (b"Transfer-Encoding", b"chunked"),
            ]
        )
        while True:
            payload = "data: %s\n\n" % datetime.now().isoformat()
            await self.send_body(payload.encode("utf-8"), more_body=True)
            await asyncio.sleep(1)

    async def send_em_data(self, bookmark):
        # Serialize the bookmark
        data = json.dumps(
            {"lat": em_data.lat, "long": em_data.long, "frequency": em_data.frequency})
        # Send the serialized data as a JSON response
        await self.channel_layer.send(
            "em-data-add", {"type": "send.em_data", "data": data}
        )
        # await self.send_response(
        #     200, data, headers=[(b"Content-Type", b"application/json")]
        # )
