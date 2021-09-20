from polar_convert.constants import (
    VALID_HEMISPHERES,
    VALID_GRID_SIZES,
)


def validate_grid_size(grid_size):
    if grid_size not in VALID_GRID_SIZES:
        raise ValueError(
            f'Got `grid_size` of {grid_size} but expected one of {VALID_GRID_SIZES}'
        )

    return grid_size


def validate_hemisphere(hemisphere):
    if not isinstance(hemisphere, str) or hemisphere.lower() not in VALID_HEMISPHERES:
        raise ValueError(
            f'Got `hemisphere` of {hemisphere} but expected one of {VALID_HEMISPHERES}'
        )

    return hemisphere.lower()
