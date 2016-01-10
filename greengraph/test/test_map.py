import numpy as np
from StringIO import StringIO
from matplotlib import image as img
import matplotlib
import requests
from nose.tools import assert_equal, assert_raises
from greengraph.map import Map
from mock import Mock, patch
import yaml
import os


@patch('matplotlib.image.imread')
@patch('StringIO.StringIO')
def test_build_map_params(mock_img,mock_string):
    with patch.object(requests,'get') as mock_get:
        trial_map = Map(50.0,50.0)
        mock_get.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",
        params={
            'sensor':'false',
            'zoom':10,
            'size':'400x400',
            'center':'50.0,50.0',
            'style':'feature:all|element:labels|visibility:off',
            'maptype':'satellite'
            }
        )


@patch('StringIO.StringIO')
def test_green(mock_string):
    with patch.object(matplotlib.image,'imread') as mock_get:
        with open(os.path.join(os.path.dirname(__file__),'fixtures','green.yaml')) as fixtures_file:
            fixtures=yaml.load(fixtures_file)
            for fixture in fixtures:
                mock_get.return_value = np.array(fixture.pop('pixles'))
                expected_green = fixture.pop('answer')
                trial_map = Map('junk','junk')
                actual_green = trial_map.green(1)
                # cannot assert_equal on arrays, instead loop over elements
                for x in range(2):
                    for y in range(2):
                        assert_equal(expected_green[x][y],actual_green[x][y])

@patch('StringIO.StringIO')
def test_count_green(mock_string):
    with patch.object(matplotlib.image,'imread') as mock_get:
        with open(os.path.join(os.path.dirname(__file__),'fixtures','green.yaml')) as fixtures_file:
            fixtures=yaml.load(fixtures_file)
            for fixture in fixtures:
                mock_get.return_value = np.array(fixture.pop('pixles'))
                expected_count = fixture.pop('count_answer')
                trial_map = Map('junk','junk')
                actual_count = trial_map.count_green(1)
                assert_equal(expected_count,actual_count)

   

