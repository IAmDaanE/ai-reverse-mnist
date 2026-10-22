import pygame
import argparse
from pathlib import Path, PureWindowsPath
import numpy as np

from generation import Generator
from utils import array_to_cords, normalize_array

parser = argparse.ArgumentParser(
    description="Generate a digit by reversing a MNIST classifier model."
)

parser.add_index = parser.add_argument(
        "model_path",
        type=str,
        help="The path to the pretrained model."
    )

args = parser.parse_args()
model_path = PureWindowsPath(Path(args.model_path))

generator = Generator(model_path)

WINDOW_WIDTH = 3 * 20 + 420 + 300
WINDOW_HEIGHT = 420 + 2 * 20

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.Clock()

input_array = [0, 0, 0, 0.99, 0, 0, 0, 0, 0, 0]
outputs = []
cell_size = 420 / 28

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ui logic

    # ai logic

    np_outputs = generator.generate(input_array).flatten()
    outputs = normalize_array(np_outputs.tolist())

    # displaying
    screen.fill((0,0,0))

    for i, value in enumerate(outputs):
        rgb_color = (255 * value, 255 * value, 255 * value)
        x, y = array_to_cords(i)
        pygame.draw.rect(screen, rgb_color, (20 + x * cell_size, 20 + y * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, (0, 173, 181), (20, 20, 420, 420), width=1)
    pygame.draw.rect(screen, (0, 173, 181), (460, 20, 300, 420), width=1)

    pygame.display.update()