from utils import array_to_cords

def exponential_rgb(array, exponent):
    safe_array = []
    for val in array:
        float_val = float(val)
        clipped_val = max(0.0, float_val)
        result = min(1.0, clipped_val ** exponent)
        safe_array.append(result)
    return safe_array

def sweet_zone_boost(array, target_radius=6.75, strength=1.0):
    boosted_array = []
    center_x, center_y = 13.5, 13.5
    max_radius = 13.5
    for index, val in enumerate(array):
        x, y = array_to_cords(index)
        square_distance = max(abs(x - center_x), abs(y - center_y))
        if square_distance <= target_radius:
            if target_radius > 0:
                zone_factor = square_distance / target_radius
            else:
                zone_factor = 1.0
        else:
            denom = max_radius - target_radius
            if denom > 0:
                zone_factor = 1.0 - ((square_distance - target_radius) / denom)
            else:
                zone_factor = 0.0
        zone_factor = max(0.0, min(1.0, zone_factor))
        aangepaste_factor = 1.0 + strength * (zone_factor - 1.0)
        boosted_val = val * aangepaste_factor
        boosted_array.append(boosted_val)
    return boosted_array
