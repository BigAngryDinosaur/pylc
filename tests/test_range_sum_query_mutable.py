
from pylc.range_sum_query_mutable import NumArray

def test_basic():
    nums = [1, 3, 5]
    s = NumArray(nums)
    assert s.sumRange(0, 2) == 9
    s.update(1, 2)
    assert s.sumRange(0, 2) == 8
