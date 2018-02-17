import nose
import acp_times

start_time = "2017-01-01T00:00:00+00:00"

def test_open():
    assert acp_times.open_times(15, 200, start_time) == "2017-01-01T01:00:00+00:00"
    assert acp_times.open_times(30, 300, start_time) == "2017-01-01T02:00:00+00:00"
    assert acp_times.open_times(45, 400, start_time) == "2017-01-01T03:00:00+00:00"

def test_close():
    assert acp_times.close_times(34, 200, start_time) == "2017-01-01T01:00:00+00:00"
    assert acp_times.close_times(62, 400, start_time) == "2017-01-01T02:00:00+00:00"
    assert acp_times.close_times(90, 600, start_time) == "2017-01-01T03:00:00+00:00"