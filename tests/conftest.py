"""pytest plugin configuration.

https://docs.pytest.org/en/latest/writing_plugins.html#conftest-py-plugins
"""
# Standard Python Libraries
# Ingore as module is used with set data file in testing only.
import pickle  # nosec

# Third-Party Libraries
import pytest
from requests.models import Response

""" Proeject Fixtures """


@pytest.fixture
def response_202() -> Response:
    """Return a Request repsone object."""
    with open("tests/mock_request.pickle", "rb") as input_file:
        # Ingore as method is used with set data file in testing only.
        req: Response = pickle.load(input_file)  # nosec
    return req
