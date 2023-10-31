import abc

class UserRepositoryInterface(abc.ABC):
  def __init__(self) -> None:
    self.seen = set()

  @abc.abstractmethod
  def _add(self, user):
    raise NotImplementedError