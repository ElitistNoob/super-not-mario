from entities.state import State
from common.utils.asset_loader import get_image_path, load_image


def load_player_sprites(variant="small"):
    path = get_image_path("assets", "sprites", "mario", variant)
    return {
        State.IDLE: [load_image(path, "idle.png")],
        State.WALKING: [
            load_image(path, "walking0.png"),
            load_image(path, "walking1.png"),
        ],
        State.RUNNING: [
            load_image(path, "running0.png"),
            load_image(path, "running1.png"),
        ],
        State.JUMPING: [load_image(path, "jumping.png")],
    }
