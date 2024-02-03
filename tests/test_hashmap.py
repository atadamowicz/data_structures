import pytest
from ..hashmap import HashMap

def test_insert_and_get():
    hashmap = HashMap(10)
    hashmap.insert("key1", "value1")
    hashmap.insert("key2", "value2")
    assert hashmap.get("key1") == "value1"
    assert hashmap.get("key2") == "value2"
    assert hashmap.get("nonexistent_key") is None

def test_update_value():
    hashmap = HashMap(10)
    hashmap.insert("key", "value1")
    hashmap.insert("key", "value2")
    assert hashmap.get("key") == "value2"

def test_collision_handling():
    hashmap = HashMap(1)
    hashmap.insert("key1", "value1")
    hashmap.insert("key2", "value2")
    assert hashmap.get("key1") == "value1"
    assert hashmap.get("key2") == "value2"

def test_delete():
    hashmap = HashMap(10)
    hashmap.insert("key1", "value1")
    hashmap.insert("key2", "value2")
    assert hashmap.delete("key1") is True
    assert hashmap.get("key1") is None
    assert hashmap.delete("nonexistent_key") is False