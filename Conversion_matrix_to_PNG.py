from PIL import Image, ImageDraw


class Converter:
    def __init__(self, matrix):
        self._matrix = matrix
        self._img = Image.new('RGB', (len(matrix), len(matrix[0])), color=(255, 255, 255))
        self._d = ImageDraw.Draw(self._img)

    def create_points(self):
        for y, row in enumerate(self._matrix):
            for x, numb in enumerate(row):
                if numb == 2:
                    self._d.point([x, y], fill='red')
        self._img.save('result.png')
