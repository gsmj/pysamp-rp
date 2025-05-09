from pysamp.callbacks import HookedCallback
from pystreamer import register_callbacks
from typing import Optional, Callable, Any
from dataclasses import dataclass
from pysamp import on_gamemode_init, set_world_time
from datetime import datetime

from . import selection


@dataclass
class CallbackWithFinalizer(HookedCallback):
    finalizer: Optional[Callable[..., None]] = None

    def __call__(self, *args: tuple[Any], **kwargs: dict[str, Any]) -> None:
        ret = super().__call__(*args, **kwargs)
        if self.finalizer:
            finalizer_ret = self.finalizer(*args, **kwargs)
            if finalizer_ret is not None:
                print(finalizer_ret)
                return finalizer_ret

        return ret


@on_gamemode_init
def on_ready() -> None:
    register_callbacks()
    print("Loaded")
    set_world_time(datetime.now().hour)
