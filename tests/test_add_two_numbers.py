
from pylc.add_two_numbers import Solution, create_list, to_vec

def test_basic():
    s = Solution()

    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])

    res = s.addTwoNumbers(l1, l2)

    assert to_vec(res) == [7, 0, 8]


    l1 = create_list([1, 8])
    l2 = create_list([0])

    res = s.addTwoNumbers(l1, l2)

    assert to_vec(res) == [1, 8]
