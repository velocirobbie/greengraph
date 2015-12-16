import numpy as np
from StringIO import StrinIO
from matplotlib import image as img
import requests
from nose.tools import assert_raises
from map import Map
from mock import Mock, patch

def test_build_map_params():
    with patch.object(requests,'get') as mock_get:
        default_map = map_at(51.0,0.0)
        mock_get.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",
        params={
            'senson':'false',
            'zoom':12,
            'size':'400x400',
            'center':'51.0,0.0'
            'style':'feature:all|element:labels|visibility:off'
            }
        )
        test_build_default_params()
