"""scripts/build_repo_pages.py keeps the Bible-authored text on every rebuild.

The nightly-sync workflow rebuilds every repo page from INVENTORY and live
repository data. These checks run the generator offline, with synthetic
repository data, and make sure a rebuild emits each hand-kept note and role
again and leaves the hand-kept repos/_index.md alone, so the dispositions that
tests/test_mirror_contract.py requires survive the nightly.
"""

import importlib.util
import sys

import pytest

from .conftest import REPO_ROOT

SCRIPTS = REPO_ROOT / "scripts"


def _load_generator():
    sys.path.insert(0, str(SCRIPTS))
    try:
        from pii_terms import PIIRosterNotConfigured

        spec = importlib.util.spec_from_file_location(
            "build_repo_pages_under_test", SCRIPTS / "build_repo_pages.py"
        )
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except PIIRosterNotConfigured:
            pytest.skip("PII roster not configured (CI injects it)")
        return module
    finally:
        sys.path.remove(str(SCRIPTS))


def _offline(gen, monkeypatch, root):
    monkeypatch.setattr(gen, "REPO_ROOT", root)
    monkeypatch.setattr(
        gen,
        "gh_repo",
        lambda name: {
            "private": False,
            "description": "Synthetic description.",
            "default_branch": "main",
            "updated_at": "2026-01-01T00:00:00Z",
            "license": {"spdx_id": "MIT"},
            "homepage": None,
        },
    )
    monkeypatch.setattr(gen, "gh_readme", lambda name: "# Title\n\nSynthetic summary.\n")


def test_hand_kept_text_matches_the_committed_pages():
    gen = _load_generator()
    for table in (gen.HAND_KEPT_NOTES, gen.HAND_KEPT_ROLES):
        for name, text in table.items():
            page = (REPO_ROOT / "repos" / f"{name}.md").read_text(encoding="utf-8")
            assert text in page, f"repos/{name}.md no longer carries its hand-kept text"


def test_rebuild_keeps_hand_kept_notes_and_roles(tmp_path, monkeypatch):
    gen = _load_generator()
    (tmp_path / "repos").mkdir()
    _offline(gen, monkeypatch, tmp_path)
    entries = {name: (tier, role) for name, tier, role in gen.INVENTORY}
    for name in sorted(set(gen.HAND_KEPT_NOTES) | set(gen.HAND_KEPT_ROLES)):
        tier, role = entries[name]
        ok, message = gen.build_one(name, tier, role)
        assert ok, message
        page = (tmp_path / "repos" / f"{name}.md").read_text(encoding="utf-8")
        assert gen.HAND_KEPT_NOTES.get(name, "") in page
        assert gen.HAND_KEPT_ROLES.get(name, "") in page
    rebuilt_rar = (tmp_path / "repos" / "RAR.md").read_text(encoding="utf-8").lower()
    assert "mirror contract is retired" in rebuilt_rar


def test_build_index_leaves_the_hand_kept_index_alone(tmp_path, monkeypatch):
    gen = _load_generator()
    committed = (REPO_ROOT / "repos" / "_index.md").read_text(encoding="utf-8")
    assert gen.INDEX_KEEP_MARKER in committed
    (tmp_path / "repos").mkdir()
    (tmp_path / "repos" / "_index.md").write_text(committed, encoding="utf-8")
    _offline(gen, monkeypatch, tmp_path)
    gen.build_index([(name, tier, role, True, "") for name, tier, role in gen.INVENTORY])
    assert (tmp_path / "repos" / "_index.md").read_text(encoding="utf-8") == committed
