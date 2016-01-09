from greengraph.graph import Greengraph
from mock import Mock, patch
import geopy
from nose.tools import assert_equal
import yaml
import os
import numpy as np


start = 'London'
end = 'Manchester'

def test_graph_init():
    with patch.object(geopy.geocoders,'GoogleV3') as mock_get:
        trial_graph = Greengraph(start,end)
        assert_equal(trial_graph.start, 'London')
        assert_equal(trial_graph.end, 'Manchester')
        mock_get.assert_called_with(domain="maps.google.co.uk")

def test_geolocate():
    with patch.object(geopy.geocoders.GoogleV3, 'geocode') as mock_get:
        trail_graph = Greengraph(start,end)
        trail_graph.geolocate(start)
        mock_get.assert_called_with('London', exactly_one=False)

def test_location_sequence():
    with open(os.path.join(os.path.dirname(__file__),'fixtures','location_sequence.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        trial_graph = Greengraph(start,end)
        for fixture in fixtures:
            steps = fixture.pop('steps')
            expected = np.asarray(fixture.pop('answer'))
            answer = trial_graph.location_sequence(fixture.pop('start'),fixture.pop('end'),steps)
            print expected, answer
            for step in range(steps): 
                for coord in range(2):
                    assert_equal(expected[step,coord],answer[step,coord])


