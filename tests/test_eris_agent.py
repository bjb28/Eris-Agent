#!/usr/bin/env pytest -vs
"""Tests for Version."""

# Standard Python Libraries
import logging
import sys
from unittest.mock import patch

# Third-Party Libraries
import pytest

# Custom Libraries
# Customer Libraries
from agent import _version, eris_agent

PROJECT_VERSION = _version.__version__

log_levels = (
    "debug",
    "info",
    "warning",
    "error",
    "critical",
)


class TestSupportFunctions:
    """Test support functions like version."""

    def test_clean_run(self):
        """Verify that 0 is returned when eris_agents is successful."""
        with pytest.raises(SystemExit):
            with patch.object(sys, "argv", ["bogus", "--version"]):
                assert eris_agent.main() == 0

    @pytest.mark.parametrize("level", log_levels)
    def test_log_levels(self, level):
        """Validate commandline log-level arguments."""
        with patch.object(sys, "argv", ["bogus", f"--log-level={level}"]):
            with patch.object(logging.root, "handlers", []):
                assert (
                    logging.root.hasHandlers() is False
                ), "root logger should not have handlers yet"
                return_code = eris_agent.main()
                assert (
                    logging.root.hasHandlers() is True
                ), "root logger should now have a handler"
                assert return_code == 0, "main() should return success (0)"

    def test_bad_log_level(self):
        """Validate bad log-level argument returns error."""
        with patch.object(sys, "argv", ["bogus", "--log-level=emergency"]):
            return_code = eris_agent.main()
            assert return_code == 1, "main() should return failure"

    def test_stdout_version(self, capsys):
        """Verify that version string sent to stdout agrees with the module version."""
        with pytest.raises(SystemExit):
            with patch.object(sys, "argv", ["bogus", "--version"]):
                eris_agent.main()
        captured = capsys.readouterr()
        assert (
            captured.out == f"{PROJECT_VERSION}\n"
        ), "standard output by '--version' should agree with module.__version__"
