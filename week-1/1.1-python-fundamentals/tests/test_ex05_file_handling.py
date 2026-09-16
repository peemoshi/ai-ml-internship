import csv

from ex05_file_handling import append_log, load_notes, read_scores_csv, save_notes, write_summary_csv


def test_save_and_load_notes(tmp_path):
    path = tmp_path / "notes.txt"
    save_notes(path, ["first", "second"])
    assert load_notes(path) == ["first", "second"]


def test_save_notes_overwrites(tmp_path):
    path = tmp_path / "notes.txt"
    save_notes(path, ["old"])
    save_notes(path, ["new"])
    assert load_notes(path) == ["new"]


def test_load_notes_skips_blank_lines(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("a\n\n   \nb\n", encoding="utf-8")
    assert load_notes(path) == ["a", "b"]


def test_load_notes_missing_file(tmp_path):
    assert load_notes(tmp_path / "missing.txt") == []


def test_read_scores_csv(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("name,score\n Aru ,88\nDana,abc\nTimur,\nMei,91\n", encoding="utf-8")
    rows, bad = read_scores_csv(path)
    assert rows == [{"name": "Aru", "score": 88}, {"name": "Mei", "score": 91}]
    assert bad == [3, 4]


def test_write_summary_csv(tmp_path):
    path = tmp_path / "summary.csv"
    write_summary_csv(path, {"Mei": 87.7, "Aru": 86.3})
    with open(path, newline="", encoding="utf-8") as f:
        assert list(csv.reader(f)) == [["name", "average"], ["Aru", "86.3"], ["Mei", "87.7"]]


def test_append_log(tmp_path):
    path = tmp_path / "log.txt"
    assert append_log(path, "started") == 1
    assert append_log(path, "finished") == 2
    assert path.read_text(encoding="utf-8") == "started\nfinished\n"
