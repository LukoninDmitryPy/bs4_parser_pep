import logging
from requests import RequestException
from exceptions import ParserFindTagException, UncorrentStatusException
from constants import PEP_URL, EXPECTED_STATUS


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def check_status_for_rule(from_main_page, from_page, href):
    status_list = EXPECTED_STATUS[from_main_page[1:]]
    if from_page not in status_list:
        raise UncorrentStatusException(
            f'{PEP_URL + href}'
            f'Статус в карточке: {from_page} '
            f'Ожидаемые статусы: {status_list}'
        )
    return True
