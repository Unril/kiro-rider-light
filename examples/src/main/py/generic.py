"""Generic syntax showcase for Python token scopes."""

import math
from abc import ABC, abstractmethod
from collections.abc import Callable, Iterator
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Generic, NewType, TypeVar, override

T = TypeVar("T")
MAX_RETRIES: int = 3
PyUserId = NewType("PyUserId", int)


class PyRepository(ABC, Generic[T]):
    """Generic repository interface."""

    @abstractmethod
    def find_by_id(self, entity_id: int) -> T | None: ...


class PyRole(StrEnum):
    ADMIN = "admin"


@dataclass
class PyUser:
    id: PyUserId
    name: str
    roles: set[PyRole] = field(default_factory=set)

    def display_name(self) -> str:
        return f"{self.name} (id={self.id})"

    @property
    def is_admin(self) -> bool:
        return PyRole.ADMIN in self.roles

    @staticmethod
    def guest() -> "PyUser":
        return PyUser(id=PyUserId(0), name="guest")


class PyUserRepository(PyRepository[PyUser]):
    def __init__(self) -> None:
        self._store: dict[PyUserId, PyUser] = {}

    @override
    def find_by_id(self, entity_id: int) -> PyUser | None:
        return self._store.get(PyUserId(entity_id))

    @classmethod
    def create(cls) -> "PyUserRepository":
        return cls()

    def save(self, user: PyUser) -> PyUser:
        self._store[user.id] = user
        return user

    def find_all(self) -> list[PyUser]:
        return list(self._store.values())


def py_users(repo: PyUserRepository) -> Iterator[PyUser]:
    yield from repo.find_all()


def py_retry(block: Callable[[], T], max_attempts: int = MAX_RETRIES) -> T:
    last: Exception | None = None
    for _ in range(max_attempts):
        try:
            return block()
        except Exception as e:  # noqa: BLE001  # pylint: disable=broad-except
            last = e
    raise last or RuntimeError(f"failed after {max_attempts} attempts")


async def py_showcase(obj: object, repo: PyUserRepository) -> str:
    match obj:
        case PyUser(name=n) if PyRole.ADMIN in obj.roles:  # type: ignore[union-attr]
            kind = f"admin:{n}"
        case PyUser(name=n):
            kind = f"user:{n}"
        case int(i):
            kind = f"int:{i}"
        case _:
            kind = "other"
    names: list[str] = []
    if users := list(py_users(repo)):
        names = [u.name for u in users]
    hex_val = 0xFF
    fp = 3.14
    ch = "P"
    raw = math.sqrt(2.0)
    return f"{kind} {hex_val} {fp} {ch} {raw} {names if users else []}"


# In-memory user repository with pagination support
type PyPredicate[U] = Callable[[U], bool]


class InMemoryUserRepository(PyUserRepository):
    """In-memory user repository with pagination support."""

    def find_by_role(self, role: PyRole) -> list[PyUser]:
        return [u for u in self._store.values() if role in u.roles]

    def find_all_filtered(self, predicate: PyPredicate[PyUser] = lambda _: True) -> list[PyUser]:
        return [u for u in self._store.values() if predicate(u)]

    @property
    def count(self) -> int:
        return len(self._store)

    def summary(self) -> str:
        total = self.count
        admin_count = len(self.find_by_role(PyRole.ADMIN))
        ratio = admin_count * 100 // total if total > 0 else 0
        return f"Repository: {total} users, {admin_count} admins ({ratio}%)"
