from pysamp import on_gamemode_init, send_rcon_command

SERVER_NAME: str = "Project Blue"
SERVER_MODE: str = "BlueGM (v0.1.0-alpha)"
SERVER_MAP: str = "San Andreas"
SERVER_WEB: str = "https://www.youtube.com/watch?v=EEjtzZjhqkk"
SERVER_DISCORD: str = "https://discord.gg/RDdJQ5KBuu"


@on_gamemode_init
def on_server_init() -> None:
    send_rcon_command(f"name {SERVER_NAME}")
    send_rcon_command(f"game.mode {SERVER_MODE}")
    send_rcon_command(f"game.map {SERVER_MAP}")
    send_rcon_command(f"website {SERVER_WEB}")
    send_rcon_command(f"discord.invite {SERVER_DISCORD}")
    print("Loaded: Server consts")
