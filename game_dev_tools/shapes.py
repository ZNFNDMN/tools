from dataclasses import dataclass, field
from pygame import Color, Surface, Rect, Vector2

@dataclass
class Arc:
    surface: Surface
    pos: Vector2
    radius: int
    color: Color
    start_angle: float
    stop_angle: float

    def __post_init__(self):
        self.rect = Rect(self.pos.x, self.pos.y,self.radius*2, self.radius * 2)
        self.rect.center = self.pos

@dataclass
class Circle:
    surface: Surface
    pos: Vector2
    color: Color
    radius: int = field(default=10)
    border_width: int = field(default=0)
    alpha: bool = field(default=False)

    def __post_init__(self):
        self.alpha_surf =  None

@dataclass
class Ellipse:
    surface: Surface
    pos: Vector2

@dataclass
class Line:
    surface: Surface
    start_pos: Vector2
    end_pos: Vector2
    color: Color

@dataclass
class Polygon:
    surface: Surface
    pos: Vector2
    color: Color
    points: list


@dataclass
class Rectangle:
    surface: Surface
    pos : Vector2
    width: float
    height: float
    color: Color
    border_width: int
    border_radius: int = field(default= -1)
    border_top_left_radius: int = field(default= -1)
    border_top_right_radius: int = field(default= -1)
    border_bottom_left_radius: int = field(default= -1)
    border_bottom_right_radius: int = field(default= -1)

    def __post_init__(self):
        self.rect = Rect(self.pos, (self.width, self.height))
        self.rect.center = self.pos


