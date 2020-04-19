from PIL import Image, ImageDraw


class Converter:
    def __init__(self, matrix):
        self.matrix = matrix
        self.img = Image.new('RGB', (len(matrix), len(matrix[0])), color=(255, 255, 255))
        self.d = ImageDraw.Draw(self.img)
        self.create_points()

    def create_points(self):
        for y, row in enumerate(self.matrix):
            for x, numb in enumerate(row):
                if numb == 2:
                    self.d.point([x, y], fill='black')
        self.img.save('result.png')
