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


## curent list <-2-><-1->
def test_display_list(dll):
    dll.display_list()


## curent list <-2-><-1->
def test_remove_get_first(dll):
    temp = dll.remove_get_first()
    assert temp == 2
    dll.display_list()

## curent list <-1->
def test_remove_get_last(dll):
    temp = dll.remove_get_last()
    assert temp == 1
    dll.display_list()
    dll.remove_get_last()

## curent list None
def test_remove_get_index():
    dll = DoubleLinkedList()
    dll.append_first(5)
    dll.append_first(4)
    dll.append_first(3)
    dll.append_first(2)
    dll.append_first(1)
    dll.remove_get_index(0)
    dll.remove_get_index(3)
    dll.remove_get_index(1)
    dll.display_list()

if __name__ == "__main__":
    test_append_first(dll)
    test_display_list(dll)
    test_remove_get_first(dll)
    test_remove_get_last(dll)
    test_remove_get_index()