#!/usr/bin/env pytest -vs
"""Tests for Version."""

# Third-Party Libraries
import mock

# Custom Libraries
from agent.modules import visit_webpage


class TestVisitWebpage:
    """Test visit_webpage method."""

    @mock.patch("requests.get")
    def test_200_response(self, mock_get, response_202):
        """Verify that a valid webpage returns the expected number of links."""
        mock_get.return_value = response_202
        links = visit_webpage("http:\\reddit.com")

        assert len(links) == 16
