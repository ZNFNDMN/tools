def is_on_surface(obj):
    surface_width = obj.surface.get_width()
    surface_height = obj.surface.get_height()
    return (0.0 < obj.pos.x < surface_width) and (0.0 < obj.pos.y < surface_height)