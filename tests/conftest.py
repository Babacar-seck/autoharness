import pytest

from autoharness import config


@pytest.fixture(autouse=True)
def _no_real_notifier(monkeypatch):
    # config reads AUTOHARNESS_NOTIFY* at import: without this, a contributor's own notifier (a team
    # Slack hook, desktop popups) would fire for every drain the suite runs
    monkeypatch.setattr(config, "NOTIFY", "")
    monkeypatch.setattr(config, "NOTIFY_CMD", "")
