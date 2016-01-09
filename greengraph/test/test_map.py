import numpy as np
from StringIO import StringIO
from matplotlib import image as img
import requests
from nose.tools import assert_equal, assert_raises
from greengraph.map import Map
from mock import Mock, patch

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




#def test_green_logical_array():
#    test_array = np.zeros((2,2,3))
#    test_array[0,0,:] = 0.5, 0, 1
#    test_array[0,1,:] = 0.5, 1, 0
#    test_array[1,0,:] = 1, 0.5, 0.5
#    test_array[1,1,:] = 1, 0.5, 0
#    test_map = Map(test_array
#    
#    test_logical_array = np.zeros((2, 2), dtype=bool)
#    test_logical_array[1,:] = True, True
#
#    assert_equal(Map.green(test_array,1.1),test_logical_array)
#

