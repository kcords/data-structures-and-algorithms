import pytest
from data_structures.linked_list import LinkedList, Node, TargetError


def test_exists():
    assert LinkedList


def test_instantiate():
    assert LinkedList()


def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


def test_append_existing_list(default_linked_list):
    new_item = "cherry"
    default_linked_list.append(new_item)
    assert default_linked_list.includes(new_item)
    assert str(default_linked_list) == f"{{ apple }} -> {{ banana }} -> {{ pear }} -> {{ {new_item} }} -> NULL"


def test_append_empty_list():
    linked_list = LinkedList()
    new_item = "new_item"
    linked_list.append(new_item)
    assert linked_list.includes(new_item)
    assert str(linked_list) == f"{{ {new_item} }} -> NULL"


def test_insert_before_valid(default_linked_list):
    new_item = "cherry"
    default_linked_list.insert_before("banana", new_item)
    assert default_linked_list.includes(new_item)
    assert str(default_linked_list) == f"{{ apple }} -> {{ {new_item} }} -> {{ banana }} -> {{ pear }} -> NULL"


def test_insert_before_invalid(default_linked_list):
    new_item = "new item"
    invalid_item = "invalid item"
    with pytest.raises(TargetError):
        default_linked_list.insert_before(invalid_item, new_item)


def test_insert_after_valid(default_linked_list):
    new_item = "cherry"
    default_linked_list.insert_after("banana", new_item)
    assert default_linked_list.includes(new_item)
    assert str(default_linked_list) == f"{{ apple }} -> {{ banana }} -> {{ {new_item} }} -> {{ pear }} -> NULL"


def test_insert_after_invalid(default_linked_list):
    new_item = "new item"
    invalid_item = "invalid item"
    with pytest.raises(TargetError):
        default_linked_list.insert_after(invalid_item, new_item)


@pytest.fixture
def default_linked_list():
    linked_list = LinkedList()
    linked_list.head = Node("apple")
    linked_list.head.next = Node("banana")
    linked_list.head.next.next = Node("pear")
    return linked_list

