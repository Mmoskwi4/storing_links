import logging

import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile

logger = logging.getLogger(__name__)


def get_page_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else ''
            description = soup.find('meta', attrs={'name': 'description'})
            description = description.get('content').strip() if description else ''
            image = soup.find('meta', attrs={'property': 'og:image'})
            image = image.get('content').strip() if image else ''
            type_ = soup.find('meta', attrs={'property': 'og:type'})
            type_ = type_.get('content').strip() if type_ else ''

            # Если тип содержит "video", устанавливаем его на "video"
            if 'video' in type_:
                type_ = 'video'
            # Если тип не определен или отличается от списка типов, устанавливаем его на "website" по умолчанию
            if type_ not in ['website', 'book', 'article', 'music', 'video'] or type_ is None:
                type_ = 'website'
            # Скачиваем изображение и позднее сохраняем его в поле preview
            if image:
                image_response = requests.get(image)
                if image_response.status_code == 200:
                    return {
                        'title': title,
                        'description': description,
                        'image': ContentFile(image_response.content),
                        'type': type_
                    }
                else:
                    logger.error(f"Не удалось получить превью из {image}. Status code: {image_response.status_code}")
            else:
                return {
                    'title': title,
                    'description': description,
                    'image': None,
                    'type': type_
                }
        else:
            logger.error(f"Не удалось получить данные страницы из {url}. Status code: {response.status_code}")
    except Exception as e:
        logger.exception(f"Ошибка при получении данных страницы из {url}: {e}")
    return {}