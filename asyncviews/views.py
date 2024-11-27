import asyncio
import httpx
from django.http import HttpResponse

#FUNCAO HTTP
async def http_call_async():
    #FOR DE 1 A 6
    for num in range(1,6):
        await asyncio.sleep(1)
        print(num)
    #???
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

#MINHA VIEW
async def async_view(request):
    #LOOPING
    loop = asyncio.get_event_loop()
    #RECEBENDO A FUNCAO HTTP
    loop.create_task(http_call_async())
    #RETORNO
    return HttpResponse("Minha View HTTP Async")
