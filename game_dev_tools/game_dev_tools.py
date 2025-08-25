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

def draw_rect(window:pygame.Surface,surf:pygame.Surface, divisions):
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

    for numerator in range(0, denominator + 1):gi
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