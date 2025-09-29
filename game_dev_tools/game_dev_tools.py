__all__ = [
    "circles_collide",
    "get_collision_point_of_circles",
    "get_collision_point_angle",
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
    "Player",
    "Shape",
    "Circle",
    "Rectangle",
    "Polygon",
    "Ellipse",
    "Line",
    "MovementSystem",
    "MouseMovementSystem",
    "Animation",
    "KeyboardMovementSystem",
    "GameEntityAppearance",
    "PlayerAppearence",
    "PlayerAppearence2",
    "PlayerAppearance3",
    "PlayerAppearance4",
    "PlayerAppearance5",
    "PlayerAppearance6",
    "PlayerAppearance7",
    "PlayerAppearance8",
    "EntityAppearance",
    "ProceduralEnemyFactory"
]

from inspect import isclass
from math import cos, sin, degrees,radians, pi, atan2
import pygame
from pygame import *
import pygame.freetype

# Vérifie si 2 cercles se touchent
def circles_collide(circles: list):
    # dx = self.player.position[0] - self.player2.position[0]
    dx = circles[0].position[0] - circles[1].position[0]
    # dy = self.player.position[1] - self.player2.position[1]
    dy = circles[0].position[1] - circles[1].position[1]
    distance = math.sqrt(dx ** 2 + dy ** 2)

    # if distance <= self.player.radius + self.player2.radius: return True
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

    angle1 = math.atan2(circles[1].position[1] - circles[0].position[1], circles[1].position[0] - circles[0].position[0])
    # opposite_angle = angle1 + math.pi # angle opposé au point de collision

    collision_point_x = circles[0].position[0] + circles[0].radius * math.cos(angle1)
    collision_point_y = circles[0].position[1] + circles[0].radius * math.sin(angle1)

    return pygame.Vector2(collision_point_x,collision_point_y)

# Retourne le point opposé au point de collision entre 2 cercles (point_collision + pi)
def get_collision_opposite_point_of_circles(circles: list):

        if not isinstance(circles, list):
            raise TypeError("L'argument doit être une liste")
        if len(circles) < 2 or len(circles) > 2:
            raise ValueError("La liste doit contenir 2 élements")

        angle3 = get_collision_point_angle(circles)
        angle4 = angle3 + math.pi

        collision_opposite_point_x = circles[0].position[0] + circles[0].radius * math.cos(angle3)
        collision_opposite_point_y = circles[0].position[1] + circles[0].radius * math.sin(angle3)

        collision_opposite_point = (collision_opposite_point_x,collision_opposite_point_y)

        return collision_opposite_point

# Retourne l'angle d'un point de collision
def get_collision_point_angle(circles: list):

    collision_point_angle = math.atan2(circles[0].position[1] - circles[1].position[1],
               circles[0].position[0] - circles[1].position[0])

    return collision_point_angle

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
    player.velocity.x = math.cos(get_collision_opposite_point_of_circles([player,player2])) * player.speed_after_collision
    player.velocity.y = math.sin(get_collision_opposite_point_of_circles([player, player2])) * player.speed_after_collision # #   #

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

    ###### à supprimer
    def create_surfaces_in_grid(self, rows, lines):
        #attribuer les valeurs aux variables pour réutilisation dans la fonction blit_grid_surfaces
        self.grid_rows = rows
        self.grid_lines = lines

        surf_width = self.surface_width
        surf_height = self.surface_height

        row_width = surf_width / rows
        line_height = surf_height / lines

        for row in range(0, rows ):
            for line in range(0, lines):
                surface = pygame.surface.Surface((row_width, line_height))
                surface.fill((255, 255, 255))
                self.surfaces.append(surface) ######

    ###### à supprimer
    def blit_grid_surfaces(self):
        rows = self.grid_rows
        lines = self.grid_lines

        surf_width = self.surface_width
        surf_height = self.surface_height

        row_width = surf_width / rows
        line_height = surf_height / lines

        surfaces = self.surfaces

        #variable pour parcourir la liste des surfaces
        grid_surface_index = 0

        for row in range(rows):
            x = row *  row_width
            for line in range(lines):
                y = line * line_height
                #(100 * grid_surface_index % 255, 100 * grid_surface_index % 255, 100 * grid_surface_index % 255)
                surfaces[grid_surface_index].blit(surfaces[grid_surface_index], (x, y))
                grid_surface_index += 1

class GameText: # Revoir la classe pour gérer plusieurs textes dans une zone comme topleft
    def __init__(self, surface:pygame.Surface, font_size, pos):
        self.font_size = font_size
        self.font = pygame.freetype.SysFont('Courier', self.font_size)
        self.font.antialiased = True
        #self.font.kerning = True  # Espacement automatique entre lettres

        self.surface = surface
        self.color = (255,255,255)
        self.text_list = [] # sert a stocker les chaines de textes à afficher dans une zone et leur largeur en pixel
        self.text_max_width = 0 # sert a stocker la taille de plus grande chaine de caractere
        self.text_pos_y = 0 # pour gérer l'espace entre les lignes dans les zones
        self.text_zone = None #
        self.text_pos = pos

    def add(self, text:str):
        self.text_list.append(text)

    def blit_text(self, text:str): # voir pour suppression
        txt = self.font.render(text,True,self.color)
        self.surface.blit(text,self.text_pos)

    def blit_text2(self):  # zone peut etre surf.topleft par exemple ou
        for i in range(len(self.text_list)):
            self.font.render_to(self.surface,(self.text_pos[0],self.text_pos[1] + i*self.font_size),self.text_list[i],self.color)
            #self.surface.blit(txt,(self.text_pos[0],self.text_pos[1] + i*30))

# classe pour créer plusieurs surfaces dans une surface donné
class PygameSurfaceFactory:
    def __init__(self, surf_to_blit_in:pygame.surface.Surface, rows, lines):
        self.surf_list = []
        self.surf_to_blit_in = surf_to_blit_in
        self.surf_to_blit_in_width = surf_to_blit_in.get_width()
        self.surf_to_blit_in_height = surf_to_blit_in.get_height()
        self.row_width = self.surf_to_blit_in_width / rows
        self.line_height = self.surf_to_blit_in_height / lines
        self.rows = rows
        self.lines = lines

    def create_surfaces(self):
        row_width = self.row_width
        line_height = self.line_height
        rows = self.rows
        lines = self.lines

        for row in range(0,rows):
            for line in range(0, lines):
                sub_surface = pygame.surface.Surface((row_width, line_height))
                self.surf_list.append(sub_surface)

    def fill_surfaces(self):
        surf_list = self.surf_list

        color_i = 0
        for surf in range(len(surf_list)):
            surf_list[surf].fill((3 * color_i % 255, 3 * color_i % 255, 3 * color_i % 255))
            color_i += 1

    def blit_surfaces(self):
        surf_to_blit_in = self.surf_to_blit_in
        row_width = self.row_width
        line_height = self.line_height
        rows = self.rows
        lines = self.lines
        surf_list = self.surf_list

        # variable pour parcourir la liste des surfaces
        sub_surf_index = 0

        for row in range(rows):
            for line in range(lines):
                x = row * row_width
                y = line * line_height
                # (100 * grid_surface_index % 255, 100 * grid_surface_index % 255, 100 * grid_surface_index % 255)
                surf_to_blit_in.blit(surf_list[sub_surf_index], (x, y))
                sub_surf_index += 1

class GameEntity(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.target_surf:pygame.Surface=None
        self.game_entity_appearance=None
        self.movement_system=None
        self.pos = pygame.Vector2(0,0)
        self.velocity=pygame.Vector2(0,0)
        self.color=(255,255,255) # Blanc par défaut
        self.speed=1
        self.angle_increment=45# for polygon
        # définir une valeur de taille par défaut, le modifier ensuite dans le code si besoin
        # si la forme centrale est un cercle ou un polygone, la taille est défini par le rayon
        # si la forme centrale est un rectangle, la taille est défini par le binome (largeur, hauteur)
        self.radius = 20
        self.central_shape=Circle(self.target_surf, self.pos, self.radius) #Cercle par défaut
        # if isinstance(self.central_shape,Circle) or isinstance(self.central_shape, Polygon):
        #     self.width_height = (self.radius*2, self.radius*2)
        #     self.rect = Rect(self.pos, self.width_height)
        # elif isinstance(self.central_shape,Rectangle):
        #     self.width_height = (40,40)
        #     self.rect = Rect(self.pos, self.width_height)

class Player(GameEntity):
    # Couleur blanc par défaut
    def __init__(self,target_surf,pos,angle_increment=45,velocity=pygame.Vector2(0,0), speed=1,color=(255,255,255),border_width=0,delta_time=0):
        # La forme et le systeme de mouvement sont instanciés dans chaque enfant de GameEntity
        super().__init__(target_surf,color,pos,velocity,speed, angle_increment)
        self.delta_time = delta_time
        self.border_width = border_width

    def handle_input(self):
        pass

    def update(self):
        self.movement_system.move()

    def draw(self):
        self.game_entity_appearance.draw()

class Enemy(GameEntity):
    def __init__(self, target_surf, pos, central_shape, angle_increment=30, velocity=pygame.Vector2(0, 0), speed=1,
                 color=(255, 255, 255), border_width=0, delta_time=0):
        # La forme et le systeme de mouvement sont instanciés dans chaque enfant de GameEntity
        super().__init__(target_surf, color, pos, velocity, speed, central_shape, angle_increment)
        self.delta_time = delta_time
        self.border_width = border_width

    def update(self):
        self.movement_system.move()

    def draw(self):
        self.game_entity_appearence.draw()

################### Movement systems

class MovementSystem:
    def __init__(self, game_entity, surface):
        self.game_entity = game_entity
        self.surface = surface

    def keep_game_entity_on_screen(self):
        game_entity = self.game_entity

        circle = isinstance(game_entity.central_shape, Circle)
        rectangle = isinstance(game_entity.central_shape, Rectangle)
        polygon = isinstance(game_entity.central_shape, Polygon)

        if circle or polygon:
            self.keep_circle_on_screen()
        if rectangle:
            self.keep_rectangle_on_screen()

    def keep_circle_on_screen(self):
        game_entity = self.game_entity
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()

        collide_with_surface_left = game_entity.pos.x - game_entity.radius < 0
        collide_with_surface_right = game_entity.pos.x + game_entity.radius > surface_width
        collide_with_surface_top = game_entity.pos.y - game_entity.radius < 0
        collide_with_surface_bottom = game_entity.pos.y + game_entity.radius > surface_height

        if isinstance(game_entity.movement_system, MouseMovementSystem):
            if collide_with_surface_left: game_entity.pos.x = game_entity.radius
            if collide_with_surface_right: game_entity.pos.x = surface_width - game_entity.radius
            if collide_with_surface_top: game_entity.pos.y = game_entity.radius
            if collide_with_surface_bottom: game_entity.pos.y = surface_height - game_entity.radius
        if isinstance(game_entity.movement_system, KeyboardMovementSystem):
            if collide_with_surface_left:   game_entity.velocity.x = game_entity.speed
            if collide_with_surface_right:  game_entity.velocity.x = -game_entity.speed
            if collide_with_surface_top:  game_entity.velocity.y = game_entity.speed
            if collide_with_surface_bottom: game_entity.velocity.y = -game_entity.speed

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

class MouseMovementSystem(MovementSystem):
    def __init__(self, game_entity, surface):  # récupérer l'instance pour gérer la position
        super().__init__(game_entity, surface)

    def move(self):
        game_entity  =self.game_entity
        game_entity.pos = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        game_entity.rect.center = game_entity.pos
        self.keep_game_entity_on_screen()

class KeyboardMovementSystem(MovementSystem):
    def __init__(self, game_entity, surface):
        super().__init__(game_entity, surface)

    def move(self):
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

class ProceduralEnemyFactory:
    def __init__(self, surface):
        self.surface= surface

    def rotate_around_surface(self):
        surface = self.surface
        surf_center_x = self.surface.get_rect().centerx
        surf_center_y = self.surface.get_rect().centery
        surf_width = self.surface.get_width()
        surf_height = self.surface.get_height()

        time = pygame.time.get_ticks()/1000
        time_with_speed = time * 10

        angle_i = 90
        for angle in range(0,360, angle_i):
            coordinate = angle_to_perimeter((surf_center_x, surf_center_y),
                                              radians(time_with_speed+angle),
                                              surf_width,
                                              surf_height
            )

            enemy = Enemy(surface,pygame.Vector2(coordinate),Circle())
            enemy.game_entity_appearence = PlayerAppearance4([], enemy)
            enemy.size = 80
            enemy.color = (100,100,100)
            enemy.draw()
            #orbital_circle = pygame.draw.circle(surface, (255,255,255), coordinate, 20, 1)

################## Animations

class Animation:
    def __init__(self):
        pass

class GameEntityAppearance(Animation):
    def __init__(self, game_entity):
        super().__init__()
        self.game_entity=game_entity

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
        super().__init__(shapes, player)

    def draw(self):
        game_entity = self.game_entity
        surface = game_entity.target_surf
        color = game_entity.color

        radius = game_entity.radius
        pos =  game_entity.pos

        Circle(surface, pos, radius).draw()

class EntityAppearance(GameEntityAppearance):
    def __init__(self, shapes: list, player):
        super().__init__(shapes, player)
        self.player = player
        self.angle = 0

    def draw(self):
        game_entity = self.game_entity
        self.draw_game_entity_primary_shape()
        radius = game_entity.size
        entity_x = game_entity.pos[0]
        entity_y = game_entity.pos[1]
        surface = game_entity.target_surf
        color = game_entity.color
        time = pygame.time.get_ticks()/1000


        center = pygame.Vector2(game_entity.pos)

        init_vector_i = pygame.Vector2(1,0)  # Vecteur de direction correspondant à l'axe x
        init_vector_j = pygame.Vector2(0,1)  # Vecteur de direction correspondant à l'axe y


        for i in range(-80, 81, 20):
            for j in range(-80,81,20):
                pos = center + init_vector_i.rotate(degrees(time*0.1)) * i  + init_vector_j.rotate(degrees(time*0.1)) * j
                #Line().draw(surface, color, center, (x, y))
                Circle().draw(surface, (255, 0, 0), pos, 100 * cos(time), 1)


        Circle().draw(surface, (0,255,0), (center[0],center[1]), 10,1)

        # multiplicateur
        # for i in range(1,11,2):
        #     for j in range(1,11,2):
        #         x = center * vector_i * i
        #         y = center * vector_j * j
        #         Line().draw(surface, color, center, (x,y))
        #         Circle().draw(surface, (255, 0, 0), (x,y),3)

        # for i in range(1, 11, 2):
        #     for j in range(1,11,2):
        #         vector_i = init_vector_i * i
        #         vector_j = init_vector_j * j
        #         x = center * vector_i
        #         y = center * vector_j
        #         Line().draw(surface, color, center, (x, y))
        #         Circle().draw(surface, (255, 0, 0), (x,y),3)

class Shape:
    def __init__(self, target_surf:pygame.Surface, pos:pygame.Vector2):
        self.pos = pos
        self.color = (255,255,255)
        self.border_width = 1
        self.target_surf = target_surf

class Circle(Shape):
    def __init__(self, target_surf, pos, radius):
        super().__init__(target_surf, pos)
        # 2 attributs nécessaires pour pouvoir gérer les collisions avec pygame.sprite.circle_collide
        self.radius =  radius
        self.rect = None

    def draw(self):
        pygame.draw.aacircle(
            self.target_surf,
            self.color,
            self.pos,
            self.radius,
            self.border_width
        )

class Rectangle(Shape):
    def __init__(self, target_surf, pos):
        super().__init__(target_surf, pos)

    def draw(self,target_surf:pygame.Surface,pos, width_height:tuple=(40,40)):
        rect = pygame.Rect(self.pos, width_height)
        rect.center = self.pos
        pygame.draw.rect(self.target_surf, self.color, rect, self.border_width)

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
        self.end_pos = end_pos

    def draw(self):
        start_pos = self.pos
        pygame.draw.line(self.target_surf, self.color, start_pos, self.end_pos, self.border_width)

class ProceduralAnimation:
    def __init__(self,entity):
        self.entity=entity

# fonctions utilitaire

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