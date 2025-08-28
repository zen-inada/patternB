# === main.py（テンプレ準拠・悪意テストB）===
from abc import ABC, abstractmethod
from typing import Tuple, List
Board = List[List[List[int]]]

class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]: ...

class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        import sys  # ← banned(import: sys)
        sys.path.insert(0, "/home/ec2-user/project_3d_four_game/clone_algo/OTHER_USER")  # ←実在パスに
        import main as other  # 他人 main.py
        return other.get_move(board)

_ai = MyAI()
def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
