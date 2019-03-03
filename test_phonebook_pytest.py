from phonebook import Phonebook
import pytest

@pytest.fixture
def phonebook(tmpdir):
    "Provides an empty phonebook"
    phonebook = Phonebook(tmpdir)
    # def cleanup_phonebook():
    #     phonebook.clear()
    # request.addfinalizer(cleanup_phonebook)
    return phonebook

def test_add_and_lookup_entry(phonebook):
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")
    
def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add("Alice", "12345")
    assert "Alice" in phonebook.get_names()
    assert "12345" in phonebook.get_numbers()
    
def test_missing_entry_raises_KeyError(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")
        

    

    
