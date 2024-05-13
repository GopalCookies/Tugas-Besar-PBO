#!/usr/bin/env python3

"""menu.py: Menu class and subclasses."""

from __future__ import annotations

import os
import pygame

import src.paths as paths
from src.constants import SCREEN_WIDTH
from src.utils import scale_to_resolution

from src.scenes.state import Scene
from src.ui.button import Button, ButtonPlay, ButtonQuit

class MenuState(Scene):
    TITLE_IMG: str = os.path.join(paths.SPRITES, "title.png")
    TITLE_Y: int = scale_to_resolution(74)
    TITLE_HEIGHT: int = scale_to_resolution(210)

    def __init__(self, game: Game) -> None:
        super().__init__(game)

        scale: float
        width: int
        height: int

        self.title: pygame.Surface = pygame.image.load(MenuState.TITLE_IMG).convert_alpha()
        
        scale = MenuState.TITLE_HEIGHT / self.title.get_height()
        width = round(self.title.get_width() * scale)
        height = round(self.title.get_height() * scale)
        self.title = pygame.transform.scale(self.title, (width, height))

        self.title_rect: pygame.Rect = self.title.get_rect()
        self.title_rect.x = round(SCREEN_WIDTH / 2 - self.title_rect.width / 2)
        self.title_rect.y = MenuState.TITLE_Y

        self.button_play: ButtonPlay = ButtonPlay(self.game)
        self.button_quit: ButtonQuit = ButtonQuit(self.game)

        self.buttons: pygame.sprite.Group[Button] = pygame.sprite.Group()
        self.buttons.add(self.button_play)
        self.buttons.add(self.button_quit)

        self.selected_button_index: int = 0
        self.selected_button: Button = self.buttons.sprites()[self.selected_button_index]

    def events(self, event: pygame.event.Event) -> None:
        super().events(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_button_index -= 1
            if event.key == pygame.K_DOWN:
                self.selected_button_index += 1

    def update(self) -> None:
        super().update()
        
        if self.selected_button_index < 0:
            self.selected_button_index = len(self.buttons) - 1
        if self.selected_button_index > len(self.buttons) - 1:
            self.selected_button_index = 0

        # self.selected_button_index = max(0, min(self.selected_button_index, len(self.buttons) - 1))
        
        self.selected_button = self.buttons.sprites()[self.selected_button_index]
        for button in self.buttons:
            button.change_state("unselected")
        self.selected_button.change_state("selected")

        for button in self.buttons:
            button.update()

    def draw(self) -> None:
        super().draw()

        self.game.display.blit(self.title, self.title_rect)
        for button in self.buttons:
            button.draw(self.game.display)

from src.game import Game
