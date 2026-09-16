from animus import Body


def test_reset_returns_zero_state():
    body = Body()
    obs = body.reset()
    assert obs == [0.0] * 6


def test_step_changes_state():
    body = Body()
    body.reset()
    obs = body.step([1.0, 0, 0, 0, 0, 0], 0.1)
    assert obs[0] == 0.1
