import dmsh
from helpers import assert_norm_equality


def test_rectangle_hole():
    r = dmsh.Rectangle(60, 330, 380, 650)
    h = dmsh.Rectangle(143, 245, 440, 543)
    geo = dmsh.Difference(r, h)

    X, cells = dmsh.generate(geo, 20, tol=1.0e-5, show=False)

    ref_norms = [1.2901184909133780e05, 7.6243606395500592e03, 6.5000000000000000e02]
    assert_norm_equality(X.flatten(), ref_norms, 1.0e-10)
