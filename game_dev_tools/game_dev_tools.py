__all__ = [
    'angle_to_perimeter',
    "circles_collide",
    "get_collision_point_of_circles",
    "get_collision_point_angle",
    "get_midpoint",
    "get_right_angle_point",
    "draw_rect",
    "draw_grid",
    "draw_dots",
    "draw_coordinate_fraction",
    "float_range",
    "create_surface",
    "show_coordinate",
    "show_surface",
    "keep_circle_on_screen",
    "VisualHelper",
    "GameText",
    "PygameSurfaceFactory",
    "GameEntity",
    "Shape",
    "Circle",
    "Rectangle",
    "Polygon",
    "Ellipse",
    "Line",
    "MovementSystem",
    "MouseMovementSystem",
    "DragAndDrop",
    "MoveWhereMouseIsClicked",
    "Animation",
    "KeyboardMovementSystem",
    "KeyboardMovementSystem2",
    "ImpactSystem",
    "StreakSystem",
    "GameEntityAppearance",
    "PlayerAppearence",
    "PlayerAppearence2",
    "PlayerAppearance3",
    "PlayerAppearance4",
    "PlayerAppearance5",
    "PlayerAppearance6",
    "PlayerAppearance7",
    "PlayerAppearance8",
    "GameEntityFactory",
    "EventAnimation",
    "EntityDefaultAppearance",
    "EntityAppearanceOnTrigger",
    'EntityEffectsSystem',
    'get_span',
    'oscillate_value',
    'Easing',
    'ease',
    'lerp',
    'lerp_smooth',
    'get_angle'
]

from inspect import isclass
from math import cos, sin, degrees,radians, pi, atan2,sqrt
import pygame
from pygame import *
import pygame.freetype
import copy
import os

# Vérifie si 2 cercles se touchent
def circles_collide(circles: list):
    dx = circles[0].position[0] - circles[1].position[0]
    dy = circles[0].position[1] - circles[1].position[1]
    distance = sqrt(dx ** 2 + dy ** 2)

    if distance <= circles[0].radius + circles[1].radius:
        return True
    else:
        return False

# Retourne le point de collision entre 2 cercles
def get_collision_point_of_circles(circles: list):

    if not isinstance(circles, list):
        raise TypeError("L'argument doit être une liste")
    if len(circles) < 2 or len(circles) > 2:
        raise ValueError("La liste doit contenir 2 élements")

    angle1 = atan2(circles[1].position[1] - circles[0].position[1], circles[1].position[0] - circles[0].position[0])
    # opposite_angle = angle1 + math.pi # angle opposé au point de collision

    collision_point_x = circles[0].position[0] + circles[0].radius * cos(angle1)
    collision_point_y = circles[0].position[1] + circles[0].radius * sin(angle1)

    return pygame.Vector2(collision_point_x,collision_point_y)

# Retourne le point opposé au point de collision entre 2 cercles (point_collision + pi)
def get_collision_opposite_point_of_circles(circles: list):
        if not isinstance(circles, list):
            raise TypeError("L'argument doit être une liste")
        if len(circles) < 2 or len(circles) > 2:
            raise ValueError("La liste doit contenir 2 élements")

        angle3 = get_collision_point_angle(circles)
        angle4 = angle3 + pi

        collision_opposite_point_x = circles[0].position[0] + circles[0].radius * cos(angle3)
        collision_opposite_point_y = circles[0].position[1] + circles[0].radius * sin(angle3)

        collision_opposite_point = (collision_opposite_point_x,collision_opposite_point_y)

        return collision_opposite_point

# Retourne l'angle d'un point de collision
def get_collision_point_angle(circles: list):

    collision_point_angle = atan2(circles[0].position[1] - circles[1].position[1],
               circles[0].position[0] - circles[1].position[0])

    return collision_point_angle

def get_midpoint(point1, point2):
    return pygame.Vector2((point1.x+point2.x) / 2, (point1.y+point2.y) / 2)

def get_right_angle_point(point1, point2):
    return pygame.Vector2((point1.x, point2.y))

# la logique est correcte mais ne fonctionne pas pour l'instant
def change_circles_direction_after_collision(circles: list):
    # pointer la nouvelle direction vers le point opposé au point de collision
    player = self.player
    player2 = self.player2

    collision_point = self.find_collision_point_of_circles([player,player2])
    collision_opposite_point = self.find_collision_opposite_point_of_circles([player,player2])

    player_direction = collision_point - collision_opposite_point
    #print (player_direction)

    #player.position.x =
    player.velocity.x = cos(get_collision_opposite_point_of_circles([player,player2])) * player.speed_after_collision
    player.velocity.y = sin(get_collision_opposite_point_of_circles([player, player2])) * player.speed_after_collision # #   #

def keep_circle_on_screen(circle_center: tuple,circle_radius, surface_width,surface_height):

        circle_x = circle_center[0]
        circle_y = circle_center[1]

        if circle_x - circle_radius < 0:
            circle_x = circle_radius
        if circle_x + circle_radius > surface_width:
            circle_x =  surface_width - circle_radius
        if circle_y - circle_radius < 0:
            circle_y = circle_radius
        if circle_y + circle_radius > surface_height:
            circle_y = surface_height - circle_radius

def draw_rect(surf:pygame.Surface, divisions):
    #exemple 2x2, 4x4 ou 8x8
    surfaces = []

    surf_width = surf.get_width()
    surf_height = surf.get_height()

    rect_width = surf_width / divisions
    rect_height = surf_height / divisions

    for row in range(divisions):
        for line in range(divisions):
            surface = pygame.surface.Surface((rect_width, rect_height))
            surfaces.append(surface)
    return surfaces

def draw_dots(surface: pygame.Surface, divisions, color, radius):
    # 2x2, 4x4 ou 8x8
    denominator = divisions
    dot_color = color
    dot_radius = radius

    surf_width = surface.get_width()
    surf_height = surface.get_height()

    # dessiner les points
    for numerator1 in range(0, denominator + 1):
        for numerator2 in range(0, denominator + 1):
            pygame.draw.aacircle(surface,
                                 color,
                                 (surf_width * numerator2 / denominator, surf_height * numerator1 / denominator),
                                 radius)

def draw_coordinate_fraction(surface:pygame.Surface, divisions, font_size, font_color):
    denominator = divisions
    surf_width = surface.get_width()
    surf_height = surface.get_height()
    font = pygame.font.Font(None, font_size)

    for numerator1 in range(0, denominator + 1):
        for numerator2 in range(0, denominator + 1):

            text = f"({numerator2}/{denominator},{numerator1}/{denominator})"
            coordinates_text = font.render(text,True,font_color)
            x = surf_width * numerator2 / denominator
            y = surf_height * numerator1 / denominator
            pos_offset = 5
            surface.blit(coordinates_text,(x+pos_offset,y+pos_offset))

def draw_grid(surface: pygame.Surface, divisions, color):
    # 2x2, 4x4 ou 8x8
    denominator = divisions
    line_color = color

    surf_width = surface.get_width()
    surf_height = surface.get_height()

    for numerator in range(0, denominator + 1):
        # lignes horizontales
        pygame.draw.line(
            surface,
            line_color,
            (0, surf_height * numerator / denominator),
            (surf_width, surf_height * numerator / denominator))

        # lignes verticales
        pygame.draw.line(surface,
                           line_color,
                           (surf_width * numerator / denominator, 0),
                           (surf_width * numerator / denominator, surf_height))

def create_surface(window:pygame.Surface,marge_width):
    window_width = window.get_width()
    window_height = window.get_height()

    surface = pygame.surface.Surface((window_width - marge_width*2 , window_height - marge_width*2))
    return surface

def show_surface(window:pygame.Surface,surface:pygame.Surface,marge_width):
    window.blit(surface, (marge_width,marge_width))

def show_coordinate(window:pygame.Surface, surface:pygame.Surface, font:pygame.font.Font, color:pygame.color.Color,surf_marge_width):
    offset_vector = pygame.Vector2(surf_marge_width, surf_marge_width)
    offset = surf_marge_width

    surf_top_left = surface.get_rect().topleft
    surf_top_right = surface.get_rect().topright
    surf_bottomleft = surface.get_rect().bottomleft
    surf_bottomright = surface.get_rect().bottomright
    surf_center = surface.get_rect().center

    top_txt_pos_offset = surf_marge_width-25
    bottom_txt_pos_offset = surf_marge_width+10

    pygame.draw.aacircle(window, color ,surf_top_left + offset_vector,5)
    coordinate1 = font.render(f"({surf_top_left[0]},{surf_top_left[1]})",True,color)
    window.blit(coordinate1, (surf_top_left[0]+ top_txt_pos_offset, surf_top_left[1]+ top_txt_pos_offset))

    pygame.draw.aacircle(window, color,surf_top_right + offset_vector,5)
    coordinate2 = font.render(f"({surf_top_right[0]},{surf_top_right[1]})", True,color)
    window.blit(coordinate2, (surf_top_right[0]+top_txt_pos_offset+25, surf_top_right[1]+top_txt_pos_offset ))

    pygame.draw.aacircle(window, color,surf_bottomleft + offset_vector, 5)
    coordinate3 = font.render(f"({surf_bottomleft[0]},{surf_bottomleft[1]})", True, color)
    window.blit(coordinate3, (surf_bottomleft[0] + bottom_txt_pos_offset - 50 , surf_bottomleft[1]+ bottom_txt_pos_offset))

    pygame.draw.aacircle(window, color,surf_bottomright + offset_vector,5)
    coordinate4 = font.render(f"({surf_bottomright[0]},{surf_bottomright[1]})", True, color)
    window.blit(coordinate4, (surf_bottomright[0] + bottom_txt_pos_offset -20, surf_bottomleft[1] +bottom_txt_pos_offset))

#Fonctions pour float
# Remplace la fonction range n'autorise pas le type float
def float_range(start, stop, step):
    """Génère une séquence avec des steps décimaux"""
    result = []
    current = start
    while current < stop:
        result.append(current)
        current += step
    return result

# Classes

class VisualHelper:
    def __init__(self, surface:pygame.Surface):
        self.surface = surface
        self.surface_width = surface.get_width()
        self.surface_height = surface.get_height()
        #sert à stocker les surfaces de la grille
        self.surfaces = []

        # Variables servant à stocker les valeurs pour blit_grid_surfaces
        self.grid_rows = 0
        self.grid_lines = 0
        self.grid_color = (255,255,255)

    def draw_grid(self, rows, lines):
        surface = self.surface
        surf_width = self.surface_width
        surf_height = self.surface_height
        row_width = surf_width / rows
        line_height = surf_height / lines

        for row in range(1,rows):
            line_start = (row * row_width,0)
            line_end = (row * row_width,surf_height)
            pygame.draw.line(surface, self.grid_color, line_start, line_end)

        for line in range(1, lines):
            line_start = (0, line * line_height)
            line_end = (surf_width, line * line_height)
            pygame.draw.line(surface, self.grid_color, line_start, line_end )

    def draw_dots(self, rows, lines):
        surface = self.surface
        surf_width = self.surface_width
        surf_height = self.surface_height

        row_width = surf_width / rows
        line_height = surf_height / lines

        for i in range(0, rows + 1):
            for j in range(0, lines + 1):
                pygame.draw.aacircle(surface, (255, 255, 255), (i * row_width, j * line_height), 3)

    def draw_coordinate_fraction(self, rows, lines, font_size):
        surface = self.surface
        surf_width = self.surface_width
        surf_height = self.surface_height

        row_width = surf_width / rows
        line_height = surf_height / lines

        font = pygame.font.Font(None, font_size)

        for row in range(0, rows + 1):
            for line in range(0, lines + 1):
                x = row_width * row
                y = line_height* line
                text = f"({row},{line})"
                #text = f"({x},{y})"
                coordinates_text = font.render(text, True, (255,255,255))
                pos_offset = 5
                surface.blit(coordinates_text, (x + pos_offset, y + pos_offset))

class GameText: # Revoir la classe pour gérer plusieurs textes dans une zone comme topleft
    def __init__(self, surface:pygame.Surface, pos, font_size, color=(255,255,255)):
        self.font_size = font_size
        self.font = pygame.freetype.SysFont('Courier', self.font_size)
        self.color = color
        self.font.antialiased = True
        self.font.kerning = True  # Espacement automatique entre lettres

        self.surface = surface
        self.color = color

        self.var_list = []
        self.text_pos = pos # position initiale a mettre a jour dans update

    # def add(self, text:str):
    #     self.text_list.append(text)
    def update(self, var_list):
        self.var_list = var_list

    def blit_text(self, text:str): # voir pour suppression
        txt = self.font.render(text,True,self.color)
        self.surface.blit(text,self.text_pos)

    def draw(self):
        for i, value in enumerate(self.var_list):
            if value.__class__.__name__ != 'str': string = f"{value}"
            else: string = value

            self.font.render_to(
                self.surface,(self.text_pos[0],self.text_pos[1] + i*self.font_size),
                string ,
                self.color
            )
            #self.surface.blit(txt,(self.text_pos[0],self.text_pos[1] + i*30))

# classe pour créer plusieurs surfaces dans une surface donné
class PygameSurfaceFactory:
    def __init__(self, surf_to_blit_in:pygame.surface.Surface, columns, lines):
        self.surf_list = []
        self.surf_to_blit_in = surf_to_blit_in
        self.surf_to_blit_in_width = surf_to_blit_in.get_width()
        self.surf_to_blit_in_height = surf_to_blit_in.get_height()
        self.column_width = self.surf_to_blit_in_width / columns
        self.line_height = self.surf_to_blit_in_height / lines
        self.columns = columns
        self.lines = lines

    def create_surfaces(self):
        column_width = self.column_width
        line_height = self.line_height
        columns = self.columns
        lines = self.lines

        for _ in range(columns):
            for _ in range(lines):
                sub_surface = pygame.surface.Surface((column_width, line_height))
                self.surf_list.append(sub_surface)

    def fill_surfaces(self):
        surf_list = self.surf_list

        for surf in surf_list:
            surf.fill((0,0,0))

    def blit_surfaces(self):
        surf_to_blit_in = self.surf_to_blit_in
        column_width = self.column_width
        line_height = self.line_height
        columns = self.columns
        lines = self.lines
        surf_list = self.surf_list

        # variable pour parcourir la liste des surfaces
        sub_surf_index = 0

        for column in range(columns):
            for line in range(lines):
                x = column * column_width
                y = line * line_height
                # (100 * grid_surface_index % 255, 100 * grid_surface_index % 255, 100 * grid_surface_index % 255)
                surf_to_blit_in.blit(surf_list[sub_surf_index], (x, y))
                sub_surf_index += 1

######################################################################################
# Classe d'entités et d'apparences
######################################################################################

class GameEntity(pygame.sprite.Sprite):
    def __init__(self, surface, pos):
        super().__init__()

        self.target_surf:pygame.Surface=surface
        self.movement_system=None
        self.pos = pos
        self.velocity=pygame.Vector2(0,0) # a supprimer et déplacer dans default_movement_system
        self.color=(255,255,255) # Blanc par défaut # a supprimer et déplacer dans apparence
        self.border_width = 0 # a supprimer et déplacer dans apparence
        self.speed  = 0 # a supprimer et déplacer dans default_movement_system
        self.appearance = None # Sert à stocker l'apparence au cours du jeu
        self.collision_active = True # permet de désactiver les collisions dans certains cas

        #self.angle_increment=45 # for polygon
        # définir une valeur de taille par défaut, le modifier ensuite dans le code si besoin
        # si la forme centrale est un cercle ou un polygone, la taille est défini par le rayon
        # si la forme centrale est un rectangle, la taille est défini par le binome (largeur, hauteur)

        #gestion du rayon et du rect de collision
        self.radius = 0
        self.rect = Rect(self.pos, (self.radius * 2, self.radius * 2))
        self.rect.center = self.pos

        self.impact_effect = None
        self.streak = None

        # valeurs par défaut qu'il faut réinitialiser au cours du programme
        self.defaults = {}

        #####################################################################################
        # appeler init_defaults_values pour créer les attributs à partir des valeurs par défaut
        #####################################################################################

        # dict qui rassemble toutes les formes composant l'entité
        # dict de liste pour parcourir plus facilement
        self.appearance_components = {}

        # dict de config des composants d'apparence
        self.appearance_config = {}

        #####################################################################################
        # appeler init_appearance pour initialiser les composants d'apparence
        # à partir de la config
        #####################################################################################

        # prévoir HealthSystem
        self.hp = 0

        # doit etre update dans les apparences
        # à récuperer dans chaque apparence pour initialisation

        # dict des apparences des entités ################
        # exemples : 'on_collision_with'
        self.appearances = {}

    def handle_events(self,event):
        pass

    def update(self, dt):
        self.reinitialize_to_defaults_values()
        self.appearance.update(dt)
        self.update_rect()

    def check_collisions(self, entities):
        pass

    def draw(self):
        self.appearance.draw()
        # affichage du rect de collision pour debugging
        #pygame.draw.rect(self.target_surf, (0,255,0), self.rect)
        # affichage du cercle de collision (rayon de collision)
        #pygame.draw.circle(self.target_surf, (255,255,0), self.pos, self.radius)

    def reinitialize_to_defaults_values(self):
        # si self.appearance n'est pas une instance de l'apparence par défaut :
        # si le délai de l'apparence est dépassé
        # on réinitialise les valeurs par défauts
        # on réinitialise les valeurs par défauts
        if not 'DefaultAppearance' in self.appearance.__class__.__name__ :
            if self.appearance.time_over:
                self.appearance.elapsed_time = 0.0
                self.appearance.time_over = False
                self.init_defaults_values()
    # initialiser les attributs des composants d'apparences a partir d'un dict

    # def init_appearance(self):
    #     for key in self.appearance_components:
    #         self.init_appearance_component(self.appearance_components[key], self.appearance_config[key])
    # # initialiser les attributs d'un objet à partir d'un dict

    # def init_appearance_component(self, components_group:list, attrs_to_init:dict):
    #     for component in components_group:
    #         self.init_object(component, attrs_to_init)

    # def init_object(self, object, attrs_to_init):
    #     for attr, value in attrs_to_init.items():
    #         # si attribut imbriqué -> split en liste -> récupérer dernier élément
    #         if '.' in attr:
    #             temp_obj = object
    #             attribute_names = attr.split('.')
    #             for attribute in attribute_names[:-1]:
    #                 temp_obj = getattr(temp_obj, attribute)
    #             setattr(temp_obj, attribute_names[-1], value)
    #         else:
    #             setattr(object, attr, value)
    #
    # def update_entity_appearance_component(self, keys:list, attrs_to_update:dict):
    #     for key in keys:
    #         self.init_appearance_component(self.appearance_components[key], attrs_to_update)
    #
    # def update_orbital_objects(self, components_group:list, attrs_to_update:dict):
    #     angle_increment = 2 * pi / len(components_group)
    #     time = pygame.time.get_ticks() / 1000
    #
    #     for index, component in enumerate(components_group):
    #         angle = angle_increment * index
    #         self.init_object(component, attrs_to_update)

    def update_rect(self): # Encore utile?
        self.rect.size = (self.radius * 2, self.radius * 2)
        self.rect.center = self.pos
    # def reinitialize_appearance(self):
    #     # si self.appearance n'est pas une instance de l'apparence par défaut :
    #     # si le délai de l'apparence est dépassé
    #     # on réinitialise les valeurs par défauts
    #     # if not 'DefaultAppearance' in self.appearance.__class__.__name__:
    #     #     if self.appearance.time_over:
    #     #         self.appearance.time_over=False
    #     #         self.appearance.trigger=False
    #     #         self.appearance = self.defaults['appearance']
    #
    #     # une seule apparence à la fois sinon bordel
    #     for key in self.appearances:
    #         appearance = self.appearances[key]
    #         if appearance.time_over:
    #             appearance.time_over = False
    #             #appearance.trigger = False
    #             self.appearance = self.defaults['appearance']
    #

    # def draw_appearance_components(self):
    #     for component in self.appearance_components:
    #         for shape in self.appearance_components[component]:
    #             shape.draw()

    def init_defaults_values(self):
        for key, value in self.defaults.items():
            setattr(self, key, value)

class EntityAppearance:
    # __slots__ = ['radius', 'pos']

    def __init__(self, entity):
        self.entity = entity
        self.target_surf = entity.target_surf
        self.pos = entity.pos
        self.rect = entity.rect
        self.time = 0.0

        self.components = {}
        self.config = {}
        #self.init_components()

    def init_time(self):
        self.time = pygame.time.get_ticks() / 1000

    def handle_events(self, event):
        pass

    def init_components(self):
        for key in self.components:
            self.init_component(self.components[key], self.config[key])

        # initialiser les attributs des composants d'apparences a partir d'un dict

    def init_component(self, components_group: list, attrs_to_init: dict):
        for component in components_group:
            self.init_object(component, attrs_to_init)

    # initialiser les attributs d'un objet à partir d'un dict
    def init_object(self, object, attrs_to_init):
        for attr, value in attrs_to_init.items():
            # si attribut imbriqué -> split en liste -> récupérer dernier élément
            if '.' in attr:
                temp_obj = object
                attribute_names = attr.split('.')
                for attribute in attribute_names[:-1]:
                    temp_obj = getattr(temp_obj, attribute)
                setattr(temp_obj, attribute_names[-1], value)
            else:
                setattr(object, attr, value)

    def update_component(self, keys: list, attrs_to_update: dict):
        for key in keys:
            self.init_component(self.components[key], attrs_to_update)

    def update_orbital_objects(self, components_group: list, attrs_to_update: dict):
        angle_increment = 2 * pi / len(components_group)
        time = pygame.time.get_ticks() / 1000

        for index, component in enumerate(components_group):
            angle = angle_increment * index
            self.init_object(component, attrs_to_update)

    def update(self, dt):
        self.update_rect()
        # self.central_shape.pos = self.pos

    def draw(self):
        self.draw_components()  ###################
        # mettre plutot self.appearance.draw() !!!!!!!!!!!!!!!!!!!

    def draw_components(self):
        for component in self.components:
            for shape in self.components[component]:
                shape.draw()

    # centrer le rect de collision par rapport au cercle
    def update_rect(self):  # Encore utile?
        self.rect.size = (self.radius * 2, self.radius * 2)
        self.rect.center = self.pos

class EntityDefaultAppearance(EntityAppearance):
    #__slots__ = ['radius', 'pos']

    def __init__(self, entity):
        super().__init__(entity)

class EntityAppearanceOnTrigger(EntityAppearance):
    # __slots__ = ['radius', 'pos']

    def __init__(self, entity):
        super().__init__(entity)
        self.duration = 0.0
        self.elapsed_time = 0.0
        self.time_over = False

        #copier la liste des composants
        self.components = self.entity.defaults['appearance'].components.copy()

        #copier la config des composants de l'apparence par défaut de l'entité
        self.config = self.entity.defaults['appearance'].config.copy()

        #copier les composants de l'apparence par défaut de l'entité
        for component in self.entity.defaults['appearance'].components:
            for i,shape in enumerate(self.entity.defaults['appearance'].components[component]):
                self.components[component][i] = copy.copy(shape)

        #On initialise ici
        #la classe d'apparence par défaut de l'entité concerné doit être créer
        self.init_components()

    def reinit(self):
        self.elapsed_time = 0.0
        self.time_over = True

    def update(self, dt):
        self.elapsed_time += dt
        if self.elapsed_time >= self.duration:
            self.reinit()

class EntityEffectsSystem:
    def __init__(self, entity):
        self.entity = entity
        self.active_effects_stacks = {}
        self.triggers = [] # déclencheurs d'effets
        self.effects = {}
        self.stack_limits = {}

    def update(self, dt):
        for trigger in self.triggers:
            self.active_effects_stacks[trigger] = [effect for effect in self.active_effects_stacks[trigger] if effect.alive]

            if len(self.active_effects_stacks[trigger]) >= self.stack_limits[trigger]:
                self.active_effects_stacks[trigger].pop(0)

            for active_effect in self.active_effects_stacks[trigger]:
                active_effect.update(dt)

    def draw(self):
        for trigger in self.triggers:
            for effects in self.active_effects_stacks[trigger]:
                effects.draw()

    def create_active_effects_stacks(self):
        # pour chaque déclencheur, créer une liste d'effets actifs
        for trigger in self.triggers:
            self.active_effects_stacks[trigger] = []

    def create_effects(self, trigger_key:str):
        stack = self.active_effects_stacks[trigger_key]
        stack.append(self.effects[trigger_key])

######################################################################################
# Factories
######################################################################################

class GameEntityFactory:
    def __init__(self, target_class, count:int, *args, **kwargs):
        self.target_class = target_class
        self.count = count
        self.instances = []
        self.args = args
        self.kwargs = kwargs

    def create_multiple_instances(self):
        return [self.target_class(*self.args,**self.kwargs) for _ in range(self.count)]

######################################################################################
# Movement systems
######################################################################################

class MovementSystem:
    def __init__(self, game_entity, surface):
        self.game_entity = game_entity
        self.surface = surface

    def handle_events(self, event):
        pass

    def keep_game_entity_on_screen(self):
        game_entity = self.game_entity

        self.keep_circle_on_screen()

        # circle = isinstance(game_entity.central_shape, Circle)
        # rectangle = isinstance(game_entity.central_shape, Rectangle)
        # polygon = isinstance(game_entity.central_shape, Polygon)
        #
        # if circle or polygon:
        #     #self.keep_circle_on_screen()
        # if rectangle:
        #     self.keep_rectangle_on_screen()

    def keep_circle_on_screen(self):
        game_entity = self.game_entity
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()

        collide_with_surface_left = game_entity.pos.x - game_entity.radius < 0
        collide_with_surface_right = game_entity.pos.x + game_entity.radius > surface_width
        collide_with_surface_top = game_entity.pos.y - game_entity.radius < 0
        collide_with_surface_bottom = game_entity.pos.y + game_entity.radius > surface_height

        if isinstance(game_entity.movement_system, MouseMovementSystem) or isinstance(game_entity.movement_system, DragAndDrop):
            if collide_with_surface_left: game_entity.pos.x = game_entity.radius
            if collide_with_surface_right: game_entity.pos.x = surface_width - game_entity.radius
            if collide_with_surface_top: game_entity.pos.y = game_entity.radius
            if collide_with_surface_bottom: game_entity.pos.y = surface_height - game_entity.radius
        if isinstance(game_entity.movement_system, KeyboardMovementSystem):
            if collide_with_surface_left:   game_entity.velocity.x = game_entity.speed
            if collide_with_surface_right:  game_entity.velocity.x = -game_entity.speed
            if collide_with_surface_top:  game_entity.velocity.y = game_entity.speed
            if collide_with_surface_bottom: game_entity.velocity.y = -game_entity.speed
        if isinstance(game_entity.movement_system, KeyboardMovementSystem2):
            if collide_with_surface_left: game_entity.pos.x = game_entity.radius
            if collide_with_surface_right: game_entity.pos.x = surface_width - game_entity.radius
            if collide_with_surface_top: game_entity.pos.y = game_entity.radius
            if collide_with_surface_bottom: game_entity.pos.y = surface_height - game_entity.radius

    def keep_rectangle_on_screen(self):
        game_entity = self.game_entity
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()
        rect_width = game_entity.width_height[0]
        rect_height = game_entity.width_height[1]

        collide_with_surface_left = game_entity.pos.x - rect_width/2 < 0
        collide_with_surface_right = game_entity.pos.x + rect_width/2 > surface_width
        collide_with_surface_top = game_entity.pos.y - rect_height/2 < 0
        collide_with_surface_bottom = game_entity.pos.y + rect_height/2 > surface_height

        mouse_movement_system = isinstance(game_entity.movement_system, MouseMovementSystem)
        keyboard_movement_system = isinstance(game_entity.movement_system, KeyboardMovementSystem)
        keyboard_movement_system2 = isinstance(game_entity.movement_system, KeyboardMovementSystem2)

        if mouse_movement_system :
            if collide_with_surface_left: game_entity.pos.x = game_entity.width_height
            if collide_with_surface_right: game_entity.pos.x = surface_width - game_entity.width_height
            if collide_with_surface_bottom: game_entity.pos.y = game_entity.width_height
            if collide_with_surface_top:game_entity.pos.y = surface_height - game_entity.width_height
        if keyboard_movement_system:
            if collide_with_surface_left: game_entity.velocity.x = game_entity.speed
            if collide_with_surface_right: game_entity.velocity.x = -game_entity.speed
            if collide_with_surface_bottom: game_entity.velocity.y = -game_entity.speed
            if collide_with_surface_top: game_entity.velocity.y = game_entity.speed
        if keyboard_movement_system2:
            if collide_with_surface_left: game_entity.pos.x = game_entity.width_height
            if collide_with_surface_right: game_entity.pos.x = surface_width - game_entity.width_height
            if collide_with_surface_bottom: game_entity.pos.y = game_entity.width_height
            if collide_with_surface_top:game_entity.pos.y = surface_height - game_entity.width_heigh

class MouseMovementSystem(MovementSystem):
    def __init__(self, game_entity, surface):  # récupérer l'instance pour gérer la position
        super().__init__(game_entity, surface)

    def update(self, dt):
        game_entity  = self.game_entity
        game_entity.pos = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        game_entity.rect.center = game_entity.pos
        self.keep_game_entity_on_screen()

class DragAndDrop(MovementSystem):
    def __init__(self, game_entity, surface):  # récupérer l'instance pour gérer la position
        super().__init__(game_entity, surface)
        self.dragging =  False

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            print('clic')
            if self.game_entity.rect.collidepoint(event.pos):
                self.dragging = True
        if event.type == MOUSEBUTTONUP:
            if self.game_entity.rect.collidepoint(event.pos):
                self.dragging = False

    def update(self, dt):
        if self.dragging:
            game_entity = self.game_entity
            game_entity.pos = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            game_entity.rect.center = game_entity.pos
            self.keep_game_entity_on_screen()

class MoveWhereMouseIsClicked(MovementSystem):
    def __init__(self, game_entity, surface):  # récupérer l'instance pour gérer la position
        super().__init__(game_entity, surface)
        self.new_pos = pygame.Vector2(0,0)
        self.event_pos = pygame.Vector2(0,0)
        self.is_clicked = False

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.is_clicked = True
            self.new_pos.x = event.pos[0]
            self.new_pos.y = event.pos[1]

    def update(self, dt):
        if self.is_clicked:
            self.game_entity.pos.x = pygame.math.lerp(self.game_entity.pos.x, self.new_pos.x, 10 * dt)
            self.game_entity.pos.y = pygame.math.lerp(self.game_entity.pos.y, self.new_pos.y, 10 * dt)
            self.game_entity.rect.center = self.game_entity.pos
        self.keep_game_entity_on_screen()

class KeyboardMovementSystem(MovementSystem):
    def __init__(self, game_entity, surface):
        super().__init__(game_entity, surface)

    def update(self):
        game_entity =self.game_entity
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_LEFT]
        right = keys[pygame.K_RIGHT]
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]

        if left: game_entity.velocity.x = -game_entity.speed
        if right: game_entity.velocity.x = game_entity.speed
        if up: game_entity.velocity.y = -game_entity.speed
        if down: game_entity.velocity.y = game_entity.speed

        self.keep_game_entity_on_screen()

        game_entity.pos += game_entity.velocity

# déplacement au clavier seulement si la touche de direction est enfoncé
class KeyboardMovementSystem2(MovementSystem):
    def __init__(self, game_entity, surface):
        super().__init__(game_entity, surface)

    def update(self, dt):
        game_entity =self.game_entity
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_LEFT]
        right = keys[pygame.K_RIGHT]
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]

        game_entity.velocity.x = 0
        game_entity.velocity.y = 0

        if left: game_entity.velocity.x = -game_entity.speed
        if right: game_entity.velocity.x = game_entity.speed
        if up: game_entity.velocity.y = -game_entity.speed
        if down: game_entity.velocity.y = game_entity.speed

        self.keep_game_entity_on_screen()

        if game_entity.velocity.length() > 0:
            game_entity.velocity = game_entity.velocity.normalize()

        game_entity.pos += game_entity.velocity * game_entity.speed * dt
        game_entity.rect.center = game_entity.pos

class ImpactSystem:
    def __init__(self, game_entity):
        self.game_entity = game_entity
        self.surface = self.game_entity.target_surf
        self.surface_width = self.surface.get_width()
        self.surface_height= self.surface.get_height()

        # gestion explosion sans lerp #################################################

        self.explosion_radius1 = 0  # à réinitialiser dans la boucle de jeu aprés explosion
        self.explosion_radius2 = 0  # à réinitialiser dans la boucle de jeu aprés explosion
        self.explosion_radius3 = 0  # à réinitialiser dans la boucle de jeu aprés explosion
        self.explosion_radius4 = 0  # à réinitialiser dans la boucle de jeu aprés explosion
        self.top_collision_happened = False  # deviens vrai quand il y a collision, à réinitialiser aprés explosion
        self.bottom_collision_happened = False  # deviens vrai quand il y a collision, à réinitialiser aprés explosio
        self.left_collision_happened = False  # deviens vrai quand il y a collision, à réinitialiser aprés explosion
        self.right_collision_happened = False  # deviens vrai quand il y a collision, à réinitialiser aprés explosion
        self.explosion_pos1 = None
        self.explosion_pos2 = None
        self.explosion_pos3 = None
        self.explosion_pos4 = None

        self.explosion_end_radius1 = 200
        self.explosion_end_radius2 = 200
        self.explosion_end_radius3 = 200
        self.explosion_end_radius4 = 200

        self.explosion_speed = 10

    def update(self,dt):
        if self.game_entity.pos.x - self.game_entity.radius <= 0:
            self.left_collision_happened = True
            self.explosion_pos3 = self.game_entity.pos.copy()
            #circle_velocity.x += circle_speed
        if self.game_entity.pos.x + self.game_entity.radius > self.surface_width:
            self.right_collision_happened = True
            self.explosion_pos4 = self.game_entity.pos.copy()
            #circle_velocity.x += -circle_speed
        if self.game_entity.pos.y - self.game_entity.radius < 0:
            self.top_collision_happened = True
            self.explosion_pos1 = self.game_entity.pos.copy()
            #circle_velocity.y = circle_speed
        if self.game_entity.pos.y + self.game_entity.radius > self.surface_height:
            self.bottom_collision_happened = True
            self.explosion_pos2 = self.game_entity.pos.copy()
            #circle_velocity.y = -circle_speed

    def draw(self):
        if self.top_collision_happened and self.explosion_radius1 <= self.explosion_end_radius1:
            self.explosion_radius1 += self.explosion_speed
            #pygame.draw.circle(surface, (0, 255, 255), explosion_pos1, explosion_radius1, 1)
            top_impact_animation = Circle(self.game_entity.target_surf,self.explosion_pos1, self.explosion_radius1)
            top_impact_animation.color = (0, 255, 255)
            top_impact_animation.draw()
            #pygame.draw.circle(surface, (0, 255, 255), explosion_pos1, explosion_radius1 - 25, 1)

        if self.bottom_collision_happened and self.explosion_radius2 <= self.explosion_end_radius2:
            self.explosion_radius2 += self.explosion_speed
            #pygame.draw.circle(surface, (255, 255, 0), explosion_pos2, explosion_radius2, 1)
            bottom_impact_animation = Circle(self.game_entity.target_surf, self.explosion_pos2, self.explosion_radius2)
            bottom_impact_animation.color = (255, 255, 0)
            bottom_impact_animation.draw()
            #pygame.draw.circle(surface, (255, 255, 0), explosion_pos2, explosion_radius2 - 25, 1)

        if self.left_collision_happened and self.explosion_radius3 <= self.explosion_end_radius3:
            self.explosion_radius3 += self.explosion_speed
            #pygame.draw.circle(surface, (255, 0, 0), explosion_pos3, explosion_radius3, 1)
            left_impact_animation = Circle(self.game_entity.target_surf, self.explosion_pos3, self.explosion_radius3)
            left_impact_animation.color = (255, 0, 0)
            left_impact_animation.draw()
            #pygame.draw.circle(surface, (255, 0, 0), explosion_pos3, explosion_radius3 - 25, 1)

        if self.right_collision_happened and self.explosion_radius4 <= self.explosion_end_radius4:
            self.explosion_radius4 += self.explosion_speed
            #pygame.draw.circle(surface, (0, 0, 255), explosion_pos4, explosion_radius4, 1)
            right_impact_animation = Circle(self.game_entity.target_surf, self.explosion_pos4, self.explosion_radius4)
            right_impact_animation.color = (255, 255, 255)
            right_impact_animation.draw()
            #pygame.draw.circle(surface, (0, 0, 255), explosion_pos4, explosion_radius4 - 25, 1)

        if self.explosion_radius1 >= self.explosion_end_radius1:
            self.explosion_radius1 = 0
            self.top_collision_happened = False

        if self.explosion_radius2 >= self.explosion_end_radius2:
            self.explosion_radius2 = 0
            self.bottom_collision_happened = False

        if self.explosion_radius3 >= self.explosion_end_radius3:
            self.explosion_radius3 = 0
            self.left_collision_happened = False

        if self.explosion_radius4 >= self.explosion_end_radius4:
            self.explosion_radius4 = 0
            self.right_collision_happened = False

        #circle = pygame.draw.circle(surface, color_palette['primary'], circle_pos, radius)
        #circle = Circle(self.surface, self.game_entity.pos, self.game_entity.radius)
        #circle.color = (0,255,255)
        #circle.draw()

class ImpactSystem2:
    def __init__(self, game_entity):

        self.game_entity = game_entity
        self.surface = self.game_entity.target_surf
        self.surface_width = self.surface.get_width()
        self.surface_height= self.surface.get_height()

        # gestion explosion sans lerp #################################################

        self.explosion_radius1 = 0  # à réinitialiser dans la boucle de jeu aprés explosion
        self.explosion_radius2 = 0  # à réinitialiser dans la boucle de jeu aprés explosion
        self.explosion_radius3 = 0  # à réinitialiser dans la boucle de jeu aprés explosion
        self.explosion_radius4 = 0  # à réinitialiser dans la boucle de jeu aprés explosion
        self.top_collision_happened = False  # deviens vrai quand il y a collision, à réinitialiser aprés explosion
        self.bottom_collision_happened = False  # deviens vrai quand il y a collision, à réinitialiser aprés explosio
        self.left_collision_happened = False  # deviens vrai quand il y a collision, à réinitialiser aprés explosion
        self.right_collision_happened = False  # deviens vrai quand il y a collision, à réinitialiser aprés explosion
        self.explosion_pos1 = None
        self.explosion_pos2 = None
        self.explosion_pos3 = None
        self.explosion_pos4 = None

        self.explosion_end_radius1 = 200
        self.explosion_end_radius2 = 200
        self.explosion_end_radius3 = 200
        self.explosion_end_radius4 = 200

        self.explosion_speed = 25

    def update(self):

        if self.game_entity.pos.x - self.game_entity.radius <= 0:
            self.left_collision_happened = True
            self.explosion_pos3 = self.game_entity.pos
            #circle_velocity.x += circle_speed
        if self.game_entity.pos.x + self.game_entity.radius > self.surface_width:
            self.right_collision_happened = True
            self.explosion_pos4 = self.game_entity.pos
            #circle_velocity.x += -circle_speed
        if self.game_entity.pos.y - self.game_entity.radius < 0:
            self.top_collision_happened = True
            self.explosion_pos1 = self.game_entity.pos
            #circle_velocity.y = circle_speed
        if self.game_entity.pos.y + self.game_entity.radius > self.surface_height:
            self.bottom_collision_happened = True
            self.explosion_pos2 = self.game_entity.pos
            #circle_velocity.y = -circle_speed


    def draw(self):
        if self.top_collision_happened and self.explosion_radius1 <= self.explosion_end_radius1:
            self.explosion_radius1 += self.explosion_speed
            #pygame.draw.circle(surface, (0, 255, 255), explosion_pos1, explosion_radius1, 1)
            top_impact_animation = Circle(self.game_entity.target_surf,self.game_entity.pos, self.explosion_radius1)
            top_impact_animation.color = (0, 255, 255)
            top_impact_animation.draw()
            #pygame.draw.circle(surface, (0, 255, 255), explosion_pos1, explosion_radius1 - 25, 1)

        if self.bottom_collision_happened and self.explosion_radius2 <= self.explosion_end_radius2:
            self.explosion_radius2 += self.explosion_speed
            #pygame.draw.circle(surface, (255, 255, 0), explosion_pos2, explosion_radius2, 1)
            bottom_impact_animation = Circle(self.game_entity.target_surf, self.game_entity.pos, self.explosion_radius2)
            bottom_impact_animation.color = (255, 255, 0)
            bottom_impact_animation.draw()
            #pygame.draw.circle(surface, (255, 255, 0), explosion_pos2, explosion_radius2 - 25, 1)

        if self.left_collision_happened and self.explosion_radius3 <= self.explosion_end_radius3:
            self.explosion_radius3 += self.explosion_speed
            #pygame.draw.circle(surface, (255, 0, 0), explosion_pos3, explosion_radius3, 1)
            left_impact_animation = Circle(self.game_entity.target_surf, self.game_entity.pos, self.explosion_radius3)
            left_impact_animation.color = (255, 0, 0)
            left_impact_animation.draw()
            #pygame.draw.circle(surface, (255, 0, 0), explosion_pos3, explosion_radius3 - 25, 1)

        if self.right_collision_happened and self.explosion_radius4 <= self.explosion_end_radius4:
            self.explosion_radius4 += self.explosion_speed
            #pygame.draw.circle(surface, (0, 0, 255), explosion_pos4, explosion_radius4, 1)
            right_impact_animation = Circle(self.game_entity.target_surf, self.game_entity.pos, self.explosion_radius4)
            right_impact_animation.color = (255, 255, 255)
            right_impact_animation.draw()
            #pygame.draw.circle(surface, (0, 0, 255), explosion_pos4, explosion_radius4 - 25, 1)

        if self.explosion_radius1 >= self.explosion_end_radius1:
            self.explosion_radius1 = 0
            self.top_collision_happened = False

        if self.explosion_radius2 >= self.explosion_end_radius2:
            self.explosion_radius2 = 0
            self.bottom_collision_happened = False

        if self.explosion_radius3 >= self.explosion_end_radius3:
            self.explosion_radius3 = 0
            self.left_collision_happened = False

        if self.explosion_radius4 >= self.explosion_end_radius4:
            self.explosion_radius4 = 0
            self.right_collision_happened = False

        #circle = pygame.draw.circle(surface, color_palette['primary'], circle_pos, radius)
        #circle = Circle(self.surface, self.game_entity.pos, self.game_entity.radius)
        #circle.color = (0,255,255)
        #circle.draw()

class StreakSystem:   # ou trail?
    def __init__(self, game_entity, trail_length):
        self.game_entity = game_entity
        self.surface = self.game_entity.target_surf
        self.trail_length = trail_length
        # gestion streak
        # liste pour stocker les cercles et dessiner
        self.circles = []
        self.color = pygame.Color(255, 255, 255)
        self.entity_appearance_elapsed_time = 0.0
        self.entity_appearance_duration = 0.0

    def update(self, dt):
        #récupérer la position en cours
        current_pos = self.game_entity.pos.copy()

        # Créer un cercle avec cette position
        circle = Circle(self.surface, current_pos, self.game_entity.radius, True)
        circle.border_width = 0

        # ajouter la liste des cercles
        self.circles.append(circle)

        # combler les l'espace entre les cercles
        # if len(self.circles) >= 2:
        #     last_pos = self.circles[-2].pos
        #     distance = int(current_pos.distance_to(last_pos))
        #     if distance >= 5:
        #         for i in range(distance):
        #             progress = i / distance
        #             pos = lerp(last_pos, current_pos, progress)
        #             c = Circle(self.surface, pos, self.game_entity.radius)
        #             c.border_width = 0
        #             self.circles.append(c)

        # si le nombre de cercle atteint le max
        # supprimer la l'entrée la plus ancienne
        if len(self.circles) >= self.trail_length:
            self.circles.pop(0)

        for circle in self.circles:
            i = self.circles.index(circle)
            progress = 1 - (i / self.trail_length)
            circle.color.r = int(pygame.math.lerp(self.game_entity.color.r, 0, progress, True))
            circle.color.g = int(pygame.math.lerp(self.game_entity.color.g, 0, progress, True))
            circle.color.b = int(pygame.math.lerp(self.game_entity.color.b, 0, progress, True))


            progress = (1 - (i / self.trail_length))
            circle.color.a = int(pygame.math.lerp(self.game_entity.color.a, 0, progress, True))
            if 1 <= i < len(self.circles) - 1:
                pass
                # print(circle.pos.distance_to(self.circles[i + 1].pos))
                # distance = circle.pos.distance_to(self.circles[i + 1].pos)

    def draw(self):
        # prévoir dessin seulement pendant déplacement
        # créer un cercle pour chacune des dernieres pos
        for circle in self.circles:
            circle.draw()

################## Animations

# animation de collision entre 2 entités
class Animation:
    def __init__(self, game_entity1, game_entity2, duration):
        self.game_entity1 = game_entity1
        self.game_entity2 = game_entity2
        self.duration = duration # en secondes
        self.alive = True
        self.time = 0.0
        self.elapsed_time = 0.0

    def init_time(self):
        self.time = pygame.time.get_ticks() / 1000

    def update(self, dt):
        self.elapsed_time += dt

        if self.elapsed_time >= self.duration:
            self.alive = False

# animation de selon un evenement donné
class EventAnimation:
    def __init__(self, target_surf, event_type):
        self.target_surf = target_surf
        self.duration = 0.0
        self.happened = False
        self.time = 0.0
        self.elapsed_time = 0.0
        self.event_type = event_type
        self.event_pos = None

    def handle_events(self, event):
        if event.type == self.event_type:
            self.happened = True
            self.elapsed_time = 0
            self.event_pos = event.pos

    def init_time(self):
        self.time = pygame.time.get_ticks() / 1000

    def update(self, dt):
        if self.happened:
           # print(round(self.elapsed_time, 0))
            self.elapsed_time += dt

            if self.elapsed_time >= self.duration:
                self.happened = False
                self.elapsed_time = 0.0

    def draw(self):
        self.init_time()

# class ExplosionEffect(EventAnimation):
#     def __init__(self, event_type):
#         super().__init__(event_type)

# A supprimer #########################
class GameEntityAppearance:
    def __init__(self, game_entity):
        self.game_entity=game_entity
        self.target_surf = game_entity.target_surf
        self.pos = self.game_entity.pos  # copie, utiliser self.game_entity.pos pour update
        self.radius = self.game_entity.radius
        self.streak_appearance = None
        self.impact_appearance = None

    def update(self, dt):
        #self.central_shape.pos = self.game_entity.pos
        if self.impact_appearance is not None:
            self.impact_appearance.update(dt)
        if self.streak_appearance is not None:
            self.streak_appearance.update(dt)
        # Afficher le rectangle de collision pour debugging
        # pygame.draw.rect(surf, (0, 255, 255), game_entity.rect)

    def draw(self):
        if self.impact_appearance is not None:
            self.impact_appearance.draw()
        if self.streak_appearance is not None:
            self.streak_appearance.draw()

    def draw_game_entity_primary_shape(self):
        game_entity = self.game_entity

        circle = isinstance(game_entity.central_shape, Circle)
        rectangle = isinstance(game_entity.central_shape, Rectangle)
        polygon = isinstance(game_entity.central_shape, Polygon)

        if circle: self.draw_game_entity_primary_circle()
        if rectangle: self.draw_game_entity_primary_rect()
        if polygon: self.draw_game_entity_primary_polygon()

    def draw_game_entity_primary_circle(self):
        game_entity = self.game_entity
        game_entity.central_shape.draw(
            game_entity.target_surf,
            game_entity.color,
            game_entity.pos,
            game_entity.radius,
            game_entity.border_width
        )

    def draw_game_entity_primary_rect(self):
        game_entity = self.game_entity
        game_entity.central_shape.draw(
            game_entity.target_surf,
            game_entity.color,
            game_entity.pos,
            game_entity.width_height,
            game_entity.border_width
        )

    def draw_game_entity_primary_polygon(self):
        game_entity = self.game_entity
        game_entity.central_shape.draw(
            game_entity.target_surf,
            game_entity.color,
            game_entity.pos,
            game_entity.radius,
            game_entity.angle_increment,
            game_entity.border_width
        )

class PlayerAppearence(GameEntityAppearance):
    def __init__(self, player):
        super().__init__(player)

    def draw(self):
        game_entity = self.game_entity
        self.draw_game_entity_primary_shape()
        radius = game_entity.size
        player_x = game_entity.pos[0]
        player_y = game_entity.pos[1]
        surface = game_entity.target_surf
        color = game_entity.color

        step = radius / 4
        start = player_y - radius
        stop = player_y

        i = 1
        for y in float_range(player_y - radius, stop, step):
            Ellipse().draw(surface, color, (player_x, y), (radius*i, 10), 1)
            i+=1

class PlayerAppearence2(GameEntityAppearance):
    def __init__(self, shapes:list, player):
        super().__init__(shapes, player)
        self.player=player

    def draw(self):
        self.draw_game_entity_primary_shape()
        # rect = Rectangle()
        # time = pygame.time.get_ticks()/1000
        # rect.draw(self.player.target_surf,self.player.color,self.player.pos,self.player.size,self.player.border_width)
        # angle_i = 10
        # rep = 360/angle_i
        # i=0
        # color_in_range = 255//rep
        # for angle in range(0,360, angle_i):
        #     x = self.player.pos[0]+ (math.tan(time)) * math.cos(time+math.radians(angle))
        #     y = self.player.pos[1] + (math.tan(time)) * math.sin(time+math.radians(angle))
        #     orbital_rect = Rectangle()
        #     orbital_rect.draw(self.player.target_surf, ((255-i),0,0), (x,y),self.player.size, 1)
        #     i+=1
        #     print(i)

class PlayerAppearance3(GameEntityAppearance):
    def __init__(self, shapes:list, player):
        super().__init__(shapes, player)

    def draw(self):
        game_entity = self.game_entity
        self.draw_game_entity_primary_shape()
        self.draw_object_around_radius(
            game_entity.target_surf,
            game_entity.pos,
            game_entity.color,
            90,
            100,
            30,
            Circle()
        )
        # angle_increment = 45
        # for angle in range(0,360,angle_increment):
        #     x = game_entity.pos.x + game_entity.size * (cos(radians(angle)))
        #     y = game_entity.pos.y + game_entity.size * (sin(radians(angle)))
        #     Circle().draw(game_entity.target_surf,game_entity.color,(x,y), game_entity.size)

    def draw_object_around_radius(self,surface,pos,color,angle_increment,radius, radius2,shape):
        for angle in range(0,360,angle_increment):
            x = pos.x + radius * (cos(radians(angle)))
            y = pos.y + radius * (sin(radians(angle)))
            shape.draw(surface, color, (x,y), radius2)

class PlayerAppearance4(GameEntityAppearance):
    def __init__(self, shapes: list, player):
        super().__init__(shapes, player)
        self.player = player

    def draw(self):
        game_entity = self.game_entity
        self.draw_game_entity_primary_shape()
        time  = pygame.time.get_ticks()/1000

        angle_i = 10
        for angle in range(0,360,angle_i):
            x = game_entity.pos[0] + game_entity.size * cos(radians(angle))
            y = game_entity.pos[1] + game_entity.size * sin(time+radians(angle))
            Circle().draw(game_entity.target_surf,game_entity.color,(x,y),5 )
            Circle().draw(game_entity.target_surf,game_entity.color,(x,y),20, 1 )

        for angle in range(0, 360, angle_i):
            x = game_entity.pos[0] + game_entity.size * sin(radians(angle))
            y = game_entity.pos[1] + game_entity.size * cos(time + radians(angle))
            Circle().draw(game_entity.target_surf,game_entity.color,(x,y),20, 1 )
            Circle().draw(game_entity.target_surf, game_entity.color, (x, y), 5, )

class PlayerAppearance5(GameEntityAppearance):
    def __init__(self, shapes: list, player):
        super().__init__(shapes, player)
        self.player = player

    def draw(self):
        game_entity = self.game_entity
        self.draw_game_entity_primary_shape()
        radius = game_entity.size
        player_x = game_entity.pos[0]
        player_y = game_entity.pos[1]
        surface = game_entity.target_surf
        color = game_entity.color


        step = radius / 10
        start = player_y-radius
        stop = player_y+radius+step

        for y in float_range(player_y-radius,stop, step):
            Ellipse().draw(surface,color,(player_x,y),(y,10+y),1)

class PlayerAppearance6(GameEntityAppearance):
    def __init__(self, shapes: list, player):
        super().__init__(shapes, player)
        self.player = player
        self.angle = 0

    def draw(self):
        game_entity = self.game_entity
        self.draw_game_entity_primary_shape()
        radius = game_entity.size
        player_x = game_entity.pos[0]
        player_y = game_entity.pos[1]
        surface = game_entity.target_surf
        color = game_entity.color

        time = pygame.time.get_ticks()/1000
        dt = pygame.Clock().tick(60)/1000
        #centre

        game_text  = GameText(surface, 20)
        game_text.blit_text(str(dt),(5,5))

        start_pos = game_entity.pos
        initial_direction = pygame.Vector2(1,0) #

        angle_i = 30

        for angle in range(0, 360, angle_i):
            direction = initial_direction.rotate(-(time*100)+angle)
            end_pos = start_pos + direction * radius
            Line().draw(surface,color, start_pos, end_pos)

class PlayerAppearance7(GameEntityAppearance):
    def __init__(self, shapes: list, player):
        super().__init__(shapes, player)
        self.player = player
        self.angle = 0

    def draw(self):
        game_entity = self.game_entity
        self.draw_game_entity_primary_shape()
        radius = game_entity.size
        player_x = game_entity.pos[0]
        player_y = game_entity.pos[1]
        surface = game_entity.target_surf
        color = game_entity.color

        time = pygame.time.get_ticks()/1000
        angle = time
        start_pos = game_entity.pos
        direction = pygame.Vector2(cos(angle), sin(angle))  #
        end_pos = start_pos + direction * radius
        angle_i = 30

        for angle in range(0,360,angle_i):
            start_pos = game_entity.pos
            direction = pygame.Vector2(cos(radians(angle)), sin(radians(angle)))  #
            end_pos = start_pos + direction * radius
            Line().draw(surface, color, start_pos, end_pos)

class PlayerAppearance8(GameEntityAppearance):

    def __init__(self, shapes:list, player):
        super().__init__(shapes)
        self.player = player

    def draw(self):
        player = self.player
        surface = player.target_surf
        color = player.color

        radius = player.radius
        pos =  player.pos

        Circle(surface, pos, radius).draw()

class Shape:
    __slots__ = ['pos', 'color', 'border_width', 'target_surf']
    def __init__(self, target_surf:pygame.Surface, pos:pygame.Vector2):
        self.pos = pos
        self.color = Color(255,255,255)
        self.border_width = 1
        self.target_surf = target_surf

class Circle(Shape):
    #__slots__ = ['radius', 'rect']

    def __init__(self, target_surf, pos, radius, alpha=False):
        super().__init__(target_surf, pos)
        # 2 attributs nécessaires pour pouvoir gérer les collisions avec pygame.sprite.circle_collide
        self.radius =  radius
        self.rect = None
        self.alpha = alpha

        # gestion transparence
        if self.alpha:
            self.alpha_surf = pygame.Surface((self.radius * 4, self.radius * 4), pygame.SRCALPHA)
            self.alpha_surf_width = self.alpha_surf.get_rect().width
            self.alpha_surf_height = self.alpha_surf.get_rect().height

    def update(self, dt):
        # mise à jour de la surface alpha
        if self.alpha and self.radius > 0:
            self.alpha_surf = pygame.Surface((self.radius * 4, self.radius * 4), pygame.SRCALPHA)
            self.alpha_surf_width = self.alpha_surf.get_rect().width
            self.alpha_surf_height = self.alpha_surf.get_rect().height

    def draw(self):
        if not self.alpha:
            pygame.draw.circle(
                self.target_surf,
                self.color,
                self.pos,
                self.radius,
                self.border_width
            )
        else:
            pos_in_alpha_surf = pygame.Vector2(self.alpha_surf_width / 2, self.alpha_surf_height / 2)
            self.alpha_surf.fill((0, 0, 0, 0))
            # # positionnement de l'alpha surf sur la fenetre
            pygame.draw.circle(
                self.alpha_surf,
                self.color,
                pos_in_alpha_surf,
                self.radius,
                self.border_width
            )
            #
            self.target_surf.blit(self.alpha_surf, self.alpha_surf.get_rect(center=self.pos))
        ###########################################
class Rectangle(Shape):
    def __init__(self, target_surf, pos):
        super().__init__(target_surf, pos)
        self.size = (0,0)
        self.rect = pygame.Rect(self.pos, self.size)
        self.rect.center = self.pos

    def draw(self):
        self.rect.size = self.size
        self.rect.center = self.pos
        pygame.draw.rect(self.target_surf, self.color, self.rect, self.border_width)

class Polygon(Shape):
    def __init__(self, target_surf, pos):
        super().__init__(target_surf, pos)

    def draw(self, radius:int, angle_increment):
        # transmettre les angles correspondant aux points

        points = []
        for angle in range(0,360, angle_increment):
            x = self.pos.x + radius * cos(radians(angle))
            y = self.pos.y + radius * sin(radians(angle))
            points.append((x,y))

        pygame.draw.polygon(self.target_surf, self.color, points, self.border_width)

class Ellipse(Shape):
    def __init__(self, target_surf, pos):
        super().__init__(target_surf, pos)

    def draw(self, width_height: tuple = (40, 20)):
        rect = pygame.Rect((0, 0), width_height)
        rect.center = self.pos
        pygame.draw.ellipse(self.target_surf, self.color, rect, self.border_width)

class Line(Shape):
    def __init__(self, target_surf,start_pos:pygame.Vector2,end_pos:pygame.Vector2):
        super().__init__(target_surf, start_pos)
        self.start_pos = start_pos
        self.end_pos = end_pos

    def draw(self):
        #start_pos = self.pos
        pygame.draw.line(self.target_surf, self.color, self.start_pos, self.end_pos, self.border_width)

import math
from typing import Callable

class Easing:
    """
    Bibliothèque de fonctions d'easing pour interpolations.
    Toutes les fonctions prennent un float t entre 0.0 et 1.0
    et retournent un float entre 0.0 et 1.0
    """

    # ========== LINEAR ==========
    @staticmethod
    def linear(t: float) -> float:
        """Interpolation linéaire (pas d'easing)"""
        return t

    # ========== QUADRATIC ==========
    @staticmethod
    def ease_in_quad(t: float) -> float:
        """Accélération quadratique"""
        return t ** 2

    @staticmethod
    def ease_out_quad(t: float) -> float:
        """Décélération quadratique"""
        return 1 - (1 - t) ** 2

    @staticmethod
    def ease_in_out_quad(t: float) -> float:
        """Accélération puis décélération quadratique"""
        if t < 0.5:
            return 2 * t ** 2
        else:
            return 1 - 2 * (1 - t) ** 2

    # ========== CUBIC ==========
    @staticmethod
    def ease_in_cubic(t: float) -> float:
        """Accélération cubique (plus prononcée)"""
        return t ** 3

    @staticmethod
    def ease_out_cubic(t: float) -> float:
        """Décélération cubique"""
        return 1 - (1 - t) ** 3

    @staticmethod
    def ease_in_out_cubic(t: float) -> float:
        """Accélération puis décélération cubique"""
        if t < 0.5:
            return 4 * t ** 3
        else:
            return 1 - 4 * (1 - t) ** 3

    # ========== QUARTIC ==========
    @staticmethod
    def ease_in_quart(t: float) -> float:
        """Accélération quartique (très prononcée)"""
        return t ** 4

    @staticmethod
    def ease_out_quart(t: float) -> float:
        """Décélération quartique"""
        return 1 - (1 - t) ** 4

    @staticmethod
    def ease_in_out_quart(t: float) -> float:
        """Accélération puis décélération quartique"""
        if t < 0.5:
            return 8 * t ** 4
        else:
            return 1 - 8 * (1 - t) ** 4

    # ========== QUINTIC ==========
    @staticmethod
    def ease_in_quint(t: float) -> float:
        """Accélération quintique (extrêmement prononcée)"""
        return t ** 5

    @staticmethod
    def ease_out_quint(t: float) -> float:
        """Décélération quintique"""
        return 1 - (1 - t) ** 5

    @staticmethod
    def ease_in_out_quint(t: float) -> float:
        """Accélération puis décélération quintique"""
        if t < 0.5:
            return 16 * t ** 5
        else:
            return 1 - 16 * (1 - t) ** 5

    # ========== SINUSOIDAL ==========
    @staticmethod
    def ease_in_sine(t: float) -> float:
        """Accélération sinusoïdale (douce)"""
        return 1 - math.cos(t * math.pi / 2)

    @staticmethod
    def ease_out_sine(t: float) -> float:
        """Décélération sinusoïdale (douce)"""
        return math.sin(t * math.pi / 2)

    @staticmethod
    def ease_in_out_sine(t: float) -> float:
        """Accélération puis décélération sinusoïdale (très douce)"""
        return 0.5 - 0.5 * math.cos(t * math.pi)

    # ========== EXPONENTIAL ==========
    @staticmethod
    def ease_in_expo(t: float) -> float:
        """Accélération exponentielle (très dramatique)"""
        return 0 if t == 0 else 2 ** (10 * (t - 1))

    @staticmethod
    def ease_out_expo(t: float) -> float:
        """Décélération exponentielle"""
        return 1 if t == 1 else 1 - 2 ** (-10 * t)

    @staticmethod
    def ease_in_out_expo(t: float) -> float:
        """Accélération puis décélération exponentielle"""
        if t == 0 or t == 1:
            return t
        if t < 0.5:
            return 0.5 * 2 ** (20 * t - 10)
        else:
            return 1 - 0.5 * 2 ** (-20 * t + 10)

    # ========== CIRCULAR ==========
    @staticmethod
    def ease_in_circ(t: float) -> float:
        """Accélération circulaire"""
        return 1 - math.sqrt(1 - t ** 2)

    @staticmethod
    def ease_out_circ(t: float) -> float:
        """Décélération circulaire"""
        return math.sqrt(1 - (1 - t) ** 2)

    @staticmethod
    def ease_in_out_circ(t: float) -> float:
        """Accélération puis décélération circulaire"""
        if t < 0.5:
            return 0.5 * (1 - math.sqrt(1 - 4 * t ** 2))
        else:
            return 0.5 * (math.sqrt(1 - 4 * (1 - t) ** 2) + 1)

    # ========== BACK (dépassement) ==========
    @staticmethod
    def ease_in_back(t: float, s: float = 1.70158) -> float:
        """Accélération avec recul initial"""
        return t * t * ((s + 1) * t - s)

    @staticmethod
    def ease_out_back(t: float, s: float = 1.70158) -> float:
        """Décélération avec dépassement final"""
        t -= 1
        return t * t * ((s + 1) * t + s) + 1

    @staticmethod
    def ease_in_out_back(t: float, s: float = 1.70158) -> float:
        """Recul initial et dépassement final"""
        s *= 1.525
        t *= 2
        if t < 1:
            return 0.5 * (t * t * ((s + 1) * t - s))
        t -= 2
        return 0.5 * (t * t * ((s + 1) * t + s) + 2)

    # ========== ELASTIC (rebond) ==========
    @staticmethod
    def ease_in_elastic(t: float) -> float:
        """Accélération avec effet élastique"""
        if t == 0 or t == 1:
            return t
        return -(2 ** (10 * (t - 1))) * math.sin((t - 1.1) * 5 * math.pi)

    @staticmethod
    def ease_out_elastic(t: float) -> float:
        """Décélération avec effet élastique (rebond)"""
        if t == 0 or t == 1:
            return t
        return 2 ** (-10 * t) * math.sin((t - 0.1) * 5 * math.pi) + 1

    @staticmethod
    def ease_in_out_elastic(t: float) -> float:
        """Élastique des deux côtés"""
        if t == 0 or t == 1:
            return t
        t *= 2
        if t < 1:
            return -0.5 * (2 ** (10 * (t - 1))) * math.sin((t - 1.1) * 5 * math.pi)
        return 0.5 * (2 ** (-10 * (t - 1))) * math.sin((t - 1.1) * 5 * math.pi) + 1

    # ========== BOUNCE (rebond) ==========
    @staticmethod
    def ease_out_bounce(t: float) -> float:
        """Décélération avec effet de rebond"""
        if t < 1 / 2.75:
            return 7.5625 * t * t
        elif t < 2 / 2.75:
            t -= 1.5 / 2.75
            return 7.5625 * t * t + 0.75
        elif t < 2.5 / 2.75:
            t -= 2.25 / 2.75
            return 7.5625 * t * t + 0.9375
        else:
            t -= 2.625 / 2.75
            return 7.5625 * t * t + 0.984375

    @staticmethod
    def ease_in_bounce(t: float) -> float:
        """Accélération avec effet de rebond"""
        return 1 - Easing.ease_out_bounce(1 - t)

    @staticmethod
    def ease_in_out_bounce(t: float) -> float:
        """Rebond des deux côtés"""
        if t < 0.5:
            return Easing.ease_in_bounce(t * 2) * 0.5
        return Easing.ease_out_bounce(t * 2 - 1) * 0.5 + 0.5

# fonctions utilitaire

def ease(start: float, end: float, t: float, easing_func: Callable = None) -> float:
    """
    Interpolation avec fonction d'easing

    Args:
        start: Valeur de départ
        end: Valeur d'arrivée
        t: Progression (0.0 à 1.0)
        easing_func: Fonction d'easing à appliquer (par défaut: linear)

    Returns:
        Valeur interpolée
    """
    if easing_func is None:
        easing_func = Easing.linear

    eased_t = easing_func(t)
    return lerp(start, end, eased_t)

def angle_to_perimeter( center, angle, largeur, hauteur):
    """Méthode unifiée pour carré ET rectangle"""
    angle = angle % (2 * pi)
    if angle < 0:
        angle += 2 * pi

    demi_largeur = largeur / 2
    demi_hauteur = hauteur / 2
    perimetre = 2 * (largeur + hauteur)

    # Position sur le périmètre (0 à perimetre)
    pos_perimetre = (angle / (2 * pi)) * perimetre

    if pos_perimetre <= largeur:
        # Côté bas (de gauche à droite)
        x = -demi_largeur + pos_perimetre
        y = -demi_hauteur
    elif pos_perimetre <= largeur + hauteur:
        # Côté droit (de bas en haut)
        x = demi_largeur
        y = -demi_hauteur + (pos_perimetre - largeur)
    elif pos_perimetre <= 2 * largeur + hauteur:
        # Côté haut (de droite à gauche)
        x = demi_largeur - (pos_perimetre - largeur - hauteur)
        y = demi_hauteur
    else:
        # Côté gauche (de haut en bas)
        x = -demi_largeur
        y = demi_hauteur - (pos_perimetre - 2 * largeur - hauteur)

    return center[0] + x, center[1] + y

def get_span(x_basis, y_basis, origin, start, end, step ) -> list:
    positions = []
    for i in float_range(start, end + step, step):
        for j in float_range(start, end + step, step):
            positions.append(origin + x_basis * i + y_basis * j)

    return positions

def oscillate_value(min, max, time, trigo_function) -> float:
    return (min + max) / 2 + trigo_function(time) * (max - min) / 2

def lerp(a, b, t):
    return a + ( b - a ) * t

def lerp_smooth(a, b, t, smooth_factor):
    return lerp(a, b, smooth_factor * t)

def get_angle(target:pygame.Vector2, origin:pygame.Vector2):
    vector = pygame.Vector2(target.x - origin.x, target.y - origin.y)
    return math.atan2(vector.y, vector.x)




