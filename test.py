class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self._get_w_h()

    def _get_w_h(self):  # внутренний метод. Не для пользователя
        self.w = self.x1 - self.x0
        self.h = self.y1 - self.y0

bbox_1 = Bbox(0, 0, 2, 3)
print(bbox_1.w)