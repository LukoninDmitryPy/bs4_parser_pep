class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class UncorrentStatusException(Exception):
    """Вызывается, когда когда статус в
    общем списке и на странице не совпадают."""
    pass
