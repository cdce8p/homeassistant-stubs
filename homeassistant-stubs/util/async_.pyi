import concurrent.futures
from _typeshed import Incomplete
from asyncio import AbstractEventLoop, Future, Task, TimerHandle
from collections.abc import Callable as Callable, Coroutine
from typing import Any

_LOGGER: Incomplete
_SHUTDOWN_RUN_CALLBACK_THREADSAFE: str

def create_eager_task(coro: Coroutine[Any, Any, _T], *, name: str | None = None, loop: AbstractEventLoop | None = None) -> Task[_T]: ...
def cancelling(task: Future[Any]) -> bool: ...
def run_callback_threadsafe(loop: AbstractEventLoop, callback: Callable[[Unpack[_Ts]], _T], *args: Unpack[_Ts]) -> concurrent.futures.Future[_T]: ...
async def gather_with_limited_concurrency(limit: int, *tasks: Any, return_exceptions: bool = False) -> Any: ...
def shutdown_run_callback_threadsafe(loop: AbstractEventLoop) -> None: ...
def get_scheduled_timer_handles(loop: AbstractEventLoop) -> list[TimerHandle]: ...
