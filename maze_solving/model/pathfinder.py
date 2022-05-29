from __future__ import annotations
from typing import Generic, T, Optional, List

import sys

class Node(Generic[T]):
    def __init__(self,
                 state: T,
                 parent: Optional[Node],
                 cost: float = 0.0,
                 heuristic: float = 0.0) -> None:
        self.state: T = state # Mazelocation(1, 1)
        self.parent: Optional[Node] = parent # None
        self.cost: float = cost
        self.heuristic: float = heuristic
    
    def __lt__(self, other: Node) -> bool:
        return(self.cost + self.heuristic) < (other.cost + other.heuristic)

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def  empty(self) -> bool:
        return not self._container
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()

def dfs(initial, goal_test, successors):
    if not successors(Node(initial, None).state):
        return

    frontier = Stack()
    frontier.push(Node(initial, None))

    explored = {initial}
    state_count = 0
    
    while not frontier.empty:
        state_count += 1
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            print(f'Solusi telah ditemukan di pencarian ke {state_count}')
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
        
    return None

def node_to_path(node):
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
