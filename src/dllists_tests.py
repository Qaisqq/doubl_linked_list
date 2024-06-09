from dllists import DoubleLinkedList

dll = DoubleLinkedList()

def test_append_first(dll):
    assert dll.head == None, "header exists in empty list"
    dll.append_first(1)
    assert dll.head.data == 1, "header value doesnt match first append"
    assert dll.tail.data == 1, "tail value doesnt match first append"
    dll.append_first(2)
    assert dll.head.data == 2, "order isnt correct"
    assert dll.head.nxt.data == 1, "order isnt correct"
    assert dll.tail.data == 1, "order isnt correct"
    assert dll.tail.prev.data == 2, "order isnt correct"

def test_display_list(dll):
    dll.display_list()


if __name__ == "__main__":
    test_append_first(dll)
    test_display_list(dll)