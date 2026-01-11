from app.features import hash_feature

def test_hash_feature_is_deterministic():
    assert hash_feature("abc", 100) == hash_feature("abc", 100)

def test_hash_feature_range():
    x = hash_feature("hello", 10)
    assert 0 <= x < 10
