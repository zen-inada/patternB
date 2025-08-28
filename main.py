# main.py（悪意テスト：sys.path 改ざん→他人 import）
from typing import List, Tuple
Board = List[List[List[int]]]

import sys  # ← banned(import: sys)
sys.path.insert(0, "/home/ec2-user/project_3d_four_game/clone_algo/OTHER_USER")

import main as other  # 他人の main.py を狙う

def get_move(board: Board) -> Tuple[int, int]:
    return other.get_move(board)
