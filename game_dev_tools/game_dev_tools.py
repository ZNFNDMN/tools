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
    "PygameSurfaceFactory"
]

import math
import pygame

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

    denominator = divisions

    surf_width = surf.get_width()
    surf_height = surf.get_height()

    rect_width = surf_width * 1 / denominator
    rect_height = surf_height * 1 / denominator

    # draw the rects
    blue_variations = []
    for color_name in pygame.color.THECOLORS:
        if 'blue' in color_name.lower():
            blue_variations.append((color_name, pygame.color.THECOLORS[color_name]))

    color_index = 0

    for numerator1 in range(0, denominator):
        color_index += 1
        for numerator2 in range(0, denominator):
            color_index += 1
            #rects.append(pygame.draw.rect(surface, blue_variations[color_index][1], (surf_width * numerator2/denominator, surf_height * numerator1/denominator, rect_width, rect_height)))
            surface = pygame.surface.Surface((rect_width, rect_height))
            #surface.fill(blue_variations[-color_index][1])
            #surf.blit(surface, (surf_width * numerator2 / denominator, surf_height * numerator1 / denominator))
            #print(f"x : {surf_width * numerator2 / denominator}, y : {surf_height * numerator1 / denominator}")
            surfaces.append(surface)
            if color_index == len(blue_variations)-1:
                color_index = 0

    #print("------------------------------------------------")
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

    def draw_grid(self, rows, lines):
        surface = self.surface
        surf_width = self.surface_width
        surf_height = self.surface_height
        row_width = surf_width / rows
        line_height = surf_height / lines

        for row in range(1,rows):
            line_start = (row * row_width,0)
            line_end = (row * row_width,surf_height)
            pygame.draw.line(surface, (255,255,255), line_start, line_end)

        for line in range(1, lines):
            line_start = (0, line * line_height)
            line_end = (surf_width, line * line_height)
            pygame.draw.line(surface, (255, 255, 255), line_start, line_end )

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
                self.surfaces.append(surface)

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
        surf_to_blit_in = self.surf_to_blit_in
        row_width = self.row_width
        line_height = self.line_height
        rows = self.rows
        lines = self.lines

        color_i = 0
        for row in range(0,rows):
            for line in range(0, lines):
                sub_surface = pygame.surface.Surface((row_width, line_height))
                sub_surface.fill((100*color_i%255, 100*color_i%255, 100*color_i%255))
                self.surf_list.append(sub_surface)
                color_i+=1

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