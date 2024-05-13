#!/usr/bin/env python3

"""game.py: Game class."""

from __future__ import annotations

import os
import pygame
import sys
import time

# Library untuk OpenGL
import moderngl
import numpy as np

import src.paths as paths
from src.constants import \
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TIMER
from src.utils import surface_to_texture

class Game:
    FLAGS: int = pygame.DOUBLEBUF | pygame.OPENGL
    TITLE: str = "Gopal Cookies"
    ICON: str = os.path.join(paths.IMAGES, "icon.png")

    VERT_SHADER: str = os.path.join(paths.SHADERS, "vert_shader.vert")
    FRAG_SHADER: str = os.path.join(paths.SHADERS, "frag_shader.frag")

    def __init__(self) -> None:
        from src.scenes.scene_manager import SceneManager

        from src.scenes.loading import LoadingState
        from src.scenes.transition import TransitionStateIn, TransitionStateOut
        from src.scenes.menu import MenuState

        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), Game.FLAGS)
        self.display: pygame.Surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.ctx: moderngl.Context = moderngl.create_context()

        self.vbo: moderngl.Buffer = self.ctx.buffer(np.array([
            # posisi (x, y), koordinat uv (x, y)
            -1.0, -1.0, 0.0, 1.0,   # bawahkiri
            1.0, -1.0, 1.0, 1.0,    # bawahkanan
            1.0,  1.0, 1.0, 0.0,    # ataskanan
            -1.0,  1.0, 0.0, 0.0    # ataskiri
            ], dtype='f4'))
        
        self.vert_shader: str = open(Game.VERT_SHADER, 'r').read()
        self.frag_shader: str = open(Game.FRAG_SHADER, 'r').read()

        self.program: moderngl.Program = self.ctx.program(vertex_shader=self.vert_shader,
                                                          fragment_shader=self.frag_shader)
        self.render_object: moderngl.VertexArray = self.ctx.vertex_array(self.program,
                                                                         [(self.vbo, '2f 2f', 'vert', 'texcoord')])

        self.clock: pygame.time.Clock = pygame.time.Clock()

        pygame.display.set_caption(Game.TITLE)
        pygame.display.set_icon(pygame.image.load(Game.ICON))

        self.scene_manager: SceneManager = SceneManager(self)

        self.scene_manager.push(MenuState(self))
        self.scene_manager.push(TransitionStateOut(self, self.get_next_state()))
        self.scene_manager.push(TransitionStateIn(self))
        self.scene_manager.push(LoadingState(self))

        self.state: State
        self.next_state()
    
    def next_state(self) -> None:
        from src.scenes.menu import MenuState

        if not self.scene_manager.is_empty():
            self.state = self.scene_manager.pop()
        else:
            self.state = MenuState(self)
    
    def get_next_state(self) -> State:
        from src.scenes.menu import MenuState

        if not self.scene_manager.is_empty():
            return self.scene_manager.scene_stack[-1]
        else:
            return MenuState(self)

    def run(self) -> None:
        while True:
            global TIMER

            TIMER.DELTA_TIME = (time.time() - TIMER.LAST_TIME) * FPS
            TIMER.LAST_TIME = time.time()
            
            self.events()
            self.update()
            self.draw()
    
    def quit(self) -> None:
        pygame.quit()
        sys.exit()
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            self.state.events(event)
        
    def update(self) -> None:
        self.state.update()

        frame_texture: moderngl.Texture = surface_to_texture(self.ctx, self.display)
        frame_texture.use(0)
        self.program['tex'] = 0
        self.render_object.render(mode=moderngl.TRIANGLE_FAN)
        
        pygame.display.flip()
        frame_texture.release()

        self.clock.tick(FPS)

    def draw(self) -> None:
        self.state.draw()

from src.scenes.state import State
