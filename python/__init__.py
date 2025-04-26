import importlib
import traceback
from pysamp.callbacks import HookedCallback
from pystreamer import register_callbacks
from typing import Optional, Callable, Any
from dataclasses import dataclass


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


_loaded_modules = {}
_unloaded_modules = {}


def _handle_load_error(module_name: str, exception: Exception) -> None:
    print(f"Error loading module {module_name}:\n {traceback.format_exc()}")


def load_module(module_name: str):
    if module_name not in _unloaded_modules:
        try:
            module = importlib.import_module(f"{__name__}.{module_name}")

        except Exception as exception:
            _handle_load_error(module_name, exception)
            return

    else:
        module = _unloaded_modules[module_name]
        try:
            importlib.reload(module)

        except Exception as exception:
            _handle_load_error(module_name, exception)
            return

        else:
            del _unloaded_modules[module_name]

    _loaded_modules[module_name] = module
    if hasattr(module, "OnGameModeInit"):
        getattr(module, "OnGameModeInit")()


def unload_module(module_name: str) -> None:
    _unloaded_modules[module_name] = module = _loaded_modules[module_name]
    del _loaded_modules[module_name]

    if hasattr(module, "OnGameModeExit"):
        getattr(module, "OnGameModeExit")()


def OnGameModeInit() -> None:
    register_callbacks()
    ...
