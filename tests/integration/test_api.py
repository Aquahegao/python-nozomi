"""Test the functionality of the api functions."""

import pytest

from nozomi import api
from nozomi.data import Post


@pytest.mark.integration
@pytest.mark.parametrize('positive_tags', [
    (['akali', 'sakimichan']),
    (['veigar'])
])
def test_retrieval_positive_tags(positive_tags):
    for post in api.get_posts(positive_tags=positive_tags, negative_tags=[]):
        assert isinstance(post, Post)


@pytest.mark.integration
@pytest.mark.parametrize('positive_tags, negative_tags', [
    (['akali', 'sakimichan'], ['nudity']),
    (['veigar'], ['nudity'])
])
def test_retrieval_negative_tags(positive_tags, negative_tags):
    for post in api.get_posts(positive_tags=positive_tags, negative_tags=negative_tags):
        assert isinstance(post, Post)
