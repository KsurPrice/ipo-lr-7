# Импортируем все функции и класс ошибки из модуля rect_utils,
# чтобы при использовании пакета collision можно было писать:
# from collision import isCorrectRect, isCollisionRect, ...
from .rect_utils import (
    RectCorrectError,
    isCorrectRect,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect
)
