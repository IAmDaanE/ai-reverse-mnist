import pygame
import argparse
from pathlib import Path, PureWindowsPath
import numpy as np
import skyline

from generation import Generator
from utils import array_to_cords, normalize_array
from color_processing import sweet_zone_boost, exponential_rgb

parser = argparse.ArgumentParser(
    description="Generate a digit by reversing a MNIST classifier model."
)

parser.add_argument(
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
pygame.display.set_caption("AI Reverse Mnist")
clock = pygame.Clock()

panel1 = skyline.SkylinePanel(screen, 460, 20, 300, 296, display_frame=False, main_color=(150, 150, 150), left_padding=55, right_padding=8)
panel1.add_widget(skyline.SkyLabel("Network Inputs", "JetBrainsMono-Regular", left_padding=8))
sliders = []
for i in range(10):
    sliders.append(skyline.SkySlider(0, 1, display_text=True))
    panel1.add_widget(sliders[-1])

panel2 = skyline.SkylinePanel(screen, 460, 340, 300, 100, display_frame=False, main_color=(150, 150, 150), left_padding=55, right_padding=8)
panel2.add_widget(skyline.SkyLabel("Color Params", left_padding=8))
panel2.add_widget(skyline.SkySlider(1, 3, display_text=True))
panel2.add_widget(skyline.SkySlider(0, 2, display_text=True))

input_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
outputs = []
cell_size = 420 / 28
exp = panel2.widgets[1].get_value()
strength = panel2.widgets[2].get_value()

font = pygame.font.Font("../assets/JetBrainsMono-Regular.ttf", 15)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ui logic

    panel1.interact()
    for i, slider in enumerate(sliders):
        input_array[i] = slider.get_value()
    panel2.interact()
    exp = panel2.widgets[1].get_value()
    strength = panel2.widgets[2].get_value() 

    # ai logic

    np_outputs = generator.generate(input_array).flatten()
    outputs = normalize_array(np_outputs.tolist())
    outputs = sweet_zone_boost(outputs, strength=strength)
    outputs = exponential_rgb(outputs, exponent=exp)

    # displaying
    screen.fill((30,30,30))

    for i, value in enumerate(outputs):
        rgb_color = (255 * value, 255 * value, 255 * value)
        x, y = array_to_cords(i)
        pygame.draw.rect(screen, rgb_color, (20 + x * cell_size, 20 + y * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, (0, 0, 0), (460, 20, 300, 300))
    panel1.draw()
    for i in range(10):
        letter_text = font.render(f"[{i}]", True, (255, 255, 255))
        height_offset = 1
        hor_offset = 16
        screen.blit(letter_text, (460 + hor_offset, 20 + panel1.widget_height / 2 + (i + 1) * panel1.widget_height - letter_text.get_height() / 2 - height_offset))
    panel2.draw()
    text1 = font.render("exp:", True, (255,255,255))
    text2 = font.render("str:", True, (255,255,255))
    screen.blit(text1, (472, 377))
    screen.blit(text2, (472, 410))
    pygame.draw.rect(screen, (0, 173, 181), (20, 20, 420, 420), width=1)
    pygame.draw.rect(screen, (0, 173, 181), (460, 20, 300, 300), width=1)
    pygame.draw.rect(screen, (0, 173, 181), (460, 340, 300, 100), width=1)
    pygame.display.update()