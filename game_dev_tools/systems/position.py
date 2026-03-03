
def is_on_surface(sprite, offset=0.0):
    surface_width = sprite.surface.get_width()
    surface_height = sprite.surface.get_height()
    return ((offset < sprite.pos.x < surface_width - offset)
            and (offset < sprite.pos.y < surface_height - offset))

def keep_on_screen(sprite):
    pass