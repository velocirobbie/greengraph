from greengraph.graph import Greengraph
from mock import Mock, patch
import geopy
from nose.tools import assert_equal

def test_graph_init():
    with patch.object(geopy.geocoders,'GoogleV3') as mock_get:
        trial_graph = Greengraph('London','Manchester')
        assert_equal(trial_graph.start, 'London')
        assert_equal(trial_graph.end, 'Manchester')
        mock_get.assert_called_with(domain="maps.google.co.uk")



