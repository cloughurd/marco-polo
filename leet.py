# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'({self.val}, {self.next})'
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1 and lists[0] is None:
            return None

        first = ListNode()
        current = first
        prev = None
        import pdb; pdb.set_trace()
        while True:
            round_min = None
            min_idx = -1
            changed = False
            for idx in range(len(lists)):
                if lists[idx] is None:
                    continue
                if lists[idx].val  == prev:
                    current.next = ListNode(prev)
                    current = current.next
                    lists[idx] = lists[idx].next
                    changed = True
                if lists[idx] is None:
                    continue
                if round_min is None or lists[idx].val < round_min:
                    round_min = lists[idx].val
                    min_idx = idx
            if round_min is not None:
                current.next = ListNode(round_min)
                current = current.next
                lists[min_idx] = lists[min_idx].next
                prev = round_min
            elif not changed:
                break

case = [[1,4,5],[1,3,4],[2,6]]
real_case = []
for l in case:
    current = ListNode(l[0])
    real_case.append(current)
    for i in range(1, len(l)):
        current.next = ListNode(l[i])

print(Solution().mergeKLists(real_case))
