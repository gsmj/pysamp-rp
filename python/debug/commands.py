from ..player import Player


@Player.command
@Player.using_registry
def dinterior(player: Player, interior_id: int) -> None:
    try:
        interior_id = int(interior_id)
    except:  # noqa: E722
        return player.send_error_message("Введите число!")

    player.set_interior(interior_id)


@Player.command
@Player.using_registry
def dsetpos(player: Player, x: float, y: float, z: float) -> None:
    try:
        x = float(x)
        y = float(y)
        z = float(z)
    except:  # noqa: E722
        return player.send_error_message("Введите число!")

    player.set_pos(x, y, z)
