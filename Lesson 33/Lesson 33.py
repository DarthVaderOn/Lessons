# Асинхронный Python: Написание простого сервиса. (downDetector)
# Ускорение простого сервиса. (downDetector)


"""
Асинхронный Python: Написание простого сервиса

    Пишем код:

        from aiohttp import web
        from aiohttp.web_middlewares import middleware
        from aiohttp.web_response import json_response


        async def ping(request):
            print(request.headers['User-Agent'])
            return {'message': 'pong'}


        @middleware
        async def middleware(request, handler):
            resp = await handler(request)
            return json_response(resp)


        app = web.Application(middlewares=[middleware])
        app.router.add_route('GET', "/ping", ping)                       # какой http метод, адрес, и сам header (функция)


        if __name__ == '__main__':
            web.run_app(app, host="127.0.0.1")


    Переходим по ссылке:

        http://127.0.0.1:8080/ping                                       # должно отобразиться {"message": "pong"}


    Блокирующие операции:

        - sleep()
        - send_mail()
        - request.get()


    Редактируем код:

        import requests
        from all.sites import sites
        from aiohttp import web
        from aiohttp.web_middlewares import middleware
        from aiohttp.web_request import Request
        from aiohttp.web_response import json_response


        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/81.0.4044.138 Safari/537.36'


        def send_request(url):
            response = requests.get(url, headers={'User-Agent': user_agent})
            return response.status_code


        async def ping(request: Request):
            result = {}
            for site in sites:
                result[site] = send_request(site)
            return result


        async def health(request: Request):
            return {'message': 'ok'}


        @middleware
        async def json_middleware(request, handler):
            resp = await handler(request)
            return json_response(resp)


        app = web.Application(middlewares=[json_middleware])
        app.router.add_route('GET', "/ping", ping)                          # какой http метод, адрес, и сам header (функция)


        if __name__ == '__main__':
            web.run_app(app, host="127.0.0.1")


        Переходим по ссылке:

            http://127.0.0.1:8080/ping                                      # должно отобразиться {"message": "pong"}


            Через промежуток времени должно отобразиться (в Mozilla Firefox будет красиво):

                {"https://gitlab.com": 200,
                 "https://www.notion.so": 200,
                 "https://sentry.io/": 200,
                 "https://django-darth-vader-on.herokuapp.com/api/token/": 405,
                 "https://django-darth-vader-on.herokuapp.com/api/schema/swagger-ui/#/": 200,
                 "https://django-darth-vader-on.herokuapp.com/admin/": 200,
                 "https://django-darth-vader-on.herokuapp.com/": 200,
                 "https://github.com/": 200,
                 "https://music.yandex.by/": 200,
                 "https://hd2.x-film.win/": 200,
                 "https://mail.yandex.ru/": 200,
                 "https://www.loveradio.ru/": 200,
                 "https://animego.org/": 200,
                 "https://www.youtube.com/": 200,
                 "https://www.pornhub.com/": 200,
                 "https://mail.google.com/": 200,
                 "https://www.google.com/maps/": 200,
                 "https://jwt.io/": 200,
                 "https://pypi.org/": 200,
                 "https://www.instagram.com/": 200,
                 "https://ru-ru.facebook.com/": 200,
                 "https://vk.com/": 200}
        

Ускорение простого сервиса. (downDetector)


    Для ускорения работы нашего приложения сделаем его асинхронным(редактируем код):


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
"""