from game_dev_tools import *
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

    collision_point = (collision_point_x,collision_point_y)

    return collision_point

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

    collision_opposite_point_angle = math.atan2(circles[0].position[1] - circles[1].position[1], circles[0].position[0] - circles[1].position[0])

    return collision_opposite_point_angle

def draw_circles_collision(surface: pygame.Surface,circles: list):
    circle1 = circles[0]
    circle2 = circles[1]
    surface_width = surface.get_width()
    surface_height = surface.get_height()

    #circle1.color = ""
    #circle2.color = ""

    # récupérer point de collision entre 2 cercles
    collision_point = get_collision_point_of_circles(circles)
    collision_point_x = collision_point[0]
    collision_point_y = collision_point[1]

    # trouver le point opposé au point de collision
    collision_opposite_point = get_collision_opposite_point_of_circles(circles)
    collision_opposite_point_x = collision_opposite_point[0]
    collision_opposite_point_y = collision_opposite_point[1]

    # Dessiner un cercle plein autour du point de collision
    pygame.draw.circle(surface, pygame.color.Color("white"), (collision_point_x, collision_point_y), 5)

    # Dessiner un cercle plein autour du point opposé au point de collision
    pygame.draw.circle(surface, pygame.color.Color("white"), (collision_opposite_point[0], collision_opposite_point[1]), 5)

    #lignes horizontal et vertical passant par le point de collision
    pygame.draw.line(surface, pygame.color.Color("white"), (collision_point_x, 0),
                     (collision_point_x,), 1)
    pygame.draw.line(surface, pygame.color.Color("white"), (0, collision_point_y), (surface_width, collision_point_y),
                     1)

    # lignes du point opposé
    pygame.draw.line(surface, pygame.color.Color("white"), (collision_opposite_point_x, 0),
                     (collision_opposite_point_x, surface_height), 1)
    pygame.draw.line(surface, pygame.color.Color("white"), (0, collision_opposite_point_y), (surface_width, collision_opposite_point_y),
                     1)

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