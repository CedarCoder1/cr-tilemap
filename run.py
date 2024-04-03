import csv
import os

import yaml
from box import Box
from reportlab.lib.units import pica
from reportlab.pdfgen import canvas


class App:
    colors = {
        '-1': (0.9, 0.9, 0.9),
        '0': (0.9, 0.9, 0.9),
        '1': (0.5, 0.9, 0.9),
        '2': (0.9, 0.9, 0.5),
        '16': (0.7, 0.5, 0.5),
        '17': (0.5, 0.7, 0.5),
        '18': (0.5, 0.5, 0.7),
        '32': (0.7, 0.7, 0.7),
        '33': (0.4, 0.9, 0.6),
        '34': (0.4, 0.7, 0.5),
        '48': (0.2, 0.8, 0.8),
        '49': (0.8, 0.2, 0.8),
        '50': (0.3, 0.6, 0.6),
        '64': (0.6, 0.4, 0.6)
    }

    def __init__(self, config_path=None):
        with open(config_path) as f:
            self.config = Box(yaml.safe_load(f))
        self.pdf_files = []

    def run(self):
        self.make_tilemap()

        if self.config.openfile:
            self.open_generated_pdfs()

    def draw_tile(self, c, x, y, value):
        w = 1
        h = 1
        s = 1 * pica
        x0 = 1 * pica
        y0 = 1 * pica
        c.setLineWidth(0.3)
        c.setStrokeColorRGB(0.2, 0.2, 0.2)
        c.setFillColorRGB(*self.colors[value])
        c.rect(x0 + x * s, y0 + y * s, w * s, h * s, fill=1)

    def make_tilemap(self):
        for csv_file in os.listdir(self.config.csv_folder):
            if csv_file.endswith('.csv'):
                pdf_file_name = os.path.splitext(csv_file)[0] + '.pdf'
                pdf_file = os.path.join(self.config.pdf_folder, pdf_file_name)
                c = canvas.Canvas(pdf_file, bottomup=0)

                with open(os.path.join(self.config.csv_folder, csv_file), 'r', encoding='latin-1') as f:
                    reader = csv.reader(f)
                    y = 0
                    start = -10000
                    for row in reader:
                        x = 0
                        if row[0] == 'Map':
                            start = -2

                        if row[0] == 'Layout':
                            start = -10000

                        if start > 0:
                            for value in row:
                                if x > 0:
                                    if value == '':
                                        value = '-1'
                                    self.draw_tile(c, x, start, value)
                                x += 1
                        y += 1
                        start += 1

                c.showPage()
                c.save()

                self.pdf_files.append(pdf_file)

    def open_generated_pdfs(self):
        for pdf_file in self.pdf_files:
            os.startfile(pdf_file)


if __name__ == '__main__':
    app = App(config_path='./config.yml')
    app.run()
