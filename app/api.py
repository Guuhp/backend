from functools import reduce
from app.config import API_URL
from app.models import Media
from requests import Response, Session
from requests.adapters import HTTPAdapter, Retry
from requests import RequestException
from PIL import Image
from io import BytesIO


class NasaApi:

    def __init__(self) -> None:
        self.__status = (429, 500, 502, 503, 504)
        self.__retry = Retry(5, backoff_factor=1, status_forcelist=self.__status)
        self.__adapter = HTTPAdapter(max_retries=self.__retry)

    def __api_call(self, url: str) -> Response:
        try:
            with Session() as session:
                session.mount("https://", self.__adapter)
                response = session.get(url)

                if response is None or not response or response.status_code != 200:
                    raise RuntimeError("Error in getting images from API")

                return response
        except RequestException:
            raise RuntimeError("\033[33mAAA\033[m")

    def __api_call_get_medias(self) -> list[dict]:
        response = self.__api_call(API_URL)

        if response.json() is None:
            raise RuntimeError("Error in getting body data from response")

        return response.json()["collection"]["items"]

    def __api_call_get_image(self, url: str) -> bytes:
        response = self.__api_call(url)

        if response.content is None:
            raise RuntimeError("Error in getting body data from response")

        return response.content

    def __map_json(self, result: list, item: dict) -> None:
        href: str = item["links"][0]["href"].replace("thumb", "orig")
        media = Media(**item["data"][0])

        if len(media.nasa_id) == 8:
            media.href = href
            result.append(media.dict())

        return result

    def load_data(self):
        items = self.__api_call_get_medias()
        return reduce(self.__map_json, items, [])

    def get_image(self, href: str) -> Image.Image:
        content = self.__api_call_get_image(href)
        return Image.open(BytesIO(content))
