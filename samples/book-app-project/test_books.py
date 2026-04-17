import importlib.util
from pathlib import Path
import json
import pytest


def load_books_module(books_path: Path):
    spec = importlib.util.spec_from_file_location("books_module", str(books_path))
    books_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(books_mod)
    return books_mod


def test_add_and_list_books(tmp_path):
    books_path = Path(__file__).parent / "books.py"
    mod = load_books_module(books_path)
    mod.DATA_FILE = str(tmp_path / "data.json")

    coll = mod.BookCollection()
    assert coll.list_books() == []

    book = coll.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    assert book.title == "The Hobbit"
    assert book.author == "J.R.R. Tolkien"
    assert book.year == 1937

    all_books = coll.list_books()
    assert len(all_books) == 1
    assert all_books[0].title == "The Hobbit"

    # persisted to disk
    data = json.loads((tmp_path / "data.json").read_text())
    assert data[0]["title"] == "The Hobbit"


def test_find_mark_remove_and_case_insensitive(tmp_path):
    books_path = Path(__file__).parent / "books.py"
    mod = load_books_module(books_path)
    mod.DATA_FILE = str(tmp_path / "data.json")

    coll = mod.BookCollection()
    coll.add_book("Dune", "Frank Herbert", 1965)
    coll.add_book("dune Messiah", "Frank Herbert", 1969)

    found = coll.find_book_by_title("DUNE")
    assert found is not None
    assert found.title.lower() == "dune"

    # mark as read
    assert coll.mark_as_read("dune") is True
    found = coll.find_book_by_title("dune")
    assert found.read is True

    # remove
    assert coll.remove_book("dune") is True
    assert coll.find_book_by_title("dune") is None


def test_find_by_author(tmp_path):
    books_path = Path(__file__).parent / "books.py"
    mod = load_books_module(books_path)
    mod.DATA_FILE = str(tmp_path / "data.json")

    coll = mod.BookCollection()
    coll.add_book("Book One", "Alice", 2000)
    coll.add_book("Book Two", "alice", 2002)

    results = coll.find_by_author("ALICE")
    assert len(results) == 2


def test_load_corrupted_json(tmp_path, capsys):
    books_path = Path(__file__).parent / "books.py"
    mod = load_books_module(books_path)
    bad_file = tmp_path / "data.json"
    bad_file.write_text("{ this is not: valid json }")
    mod.DATA_FILE = str(bad_file)

    coll = mod.BookCollection()

    # warning printed and empty collection
    captured = capsys.readouterr()
    assert "corrupted" in captured.out.lower()
    assert coll.list_books() == []


def test_persistence_between_instances(tmp_path):
    books_path = Path(__file__).parent / "books.py"
    mod = load_books_module(books_path)
    mod.DATA_FILE = str(tmp_path / "data.json")

    coll1 = mod.BookCollection()
    coll1.add_book("1984", "George Orwell", 1949)

    coll2 = mod.BookCollection()
    found = coll2.find_book_by_title("1984")
    assert found is not None
    assert found.author == "George Orwell"
