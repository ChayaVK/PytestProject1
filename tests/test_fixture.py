import pytest

@pytest.fixture
def get_sampledata():
    return (3,4,5)

def test_data_from_fixture(get_sampledata):
    assert get_sampledata[0] == 3
    assert get_sampledata[1] == 4
    assert get_sampledata[2] == 5
    assert get_sampledata[0] + get_sampledata[1] + get_sampledata[2] == 12

