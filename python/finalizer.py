from pysamp.callbacks import HookedCallback
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