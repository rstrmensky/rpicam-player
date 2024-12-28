class Streamer:
    def start(self, url, width, height, axis_x, axis_y, screen = 0):
        command = [
            "mpv",
            f"--video-aspect-override={width}:{height}",
            "--no-border",
            "--no-input-default-bindings",
            "--no-input-builtin-bindings",
            "--cursor-autohide=always",
            f"--screen={screen}",
            f"--geometry={width}x{height}+{axis_x}+{axis_y}",
            "--no-audio",
            f"{url}"
        ]
        return command