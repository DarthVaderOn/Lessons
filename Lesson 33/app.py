import asyncio
from all.sites import sites
from aiohttp import web, request
from aiohttp.web_middlewares import middleware
from aiohttp.web_request import Request
from aiohttp.web_response import json_response


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/81.0.4044.138 Safari/537.36'


async def send_request(url):                                                            # выполняет http запрос и возращает статус
    async with request('GET', url, headers={'User-Agent': user_agent}) as response:
        return url, response.status


async def ping(request: Request):
    result = {}
    tasks = [send_request(site) for site in sites]                                      # вызываем корутины
    done, pending = await asyncio.wait(tasks)                                           # два генератора done, pending
    for task in done:                                                                   # итерируемся по генератору задачи которые выполнились
        url, status = task.result()                                                     # когда в генераторе pending задачи закончиваются генератор done остановится
        result[url] = status
    return result


async def health(request: Request):
    return {'message': 'ok'}


@middleware
async def json_middleware(request, handler):
    resp = await handler(request)
    return json_response(resp)


app = web.Application(middlewares=[json_middleware])
app.router.add_route('GET', "/ping", ping)                                              # какой http метод, адрес, и сам header (функция)


if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1")