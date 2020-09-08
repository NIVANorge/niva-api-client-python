from tests.testutils import create_niva_app
from url_utils import app_url, subdomain_for


def test_app_subdomain():
    app = create_niva_app(title="awesomeapp")
    url = app_url(app)
    assert url == "https://awesomeapp.test.niva.no"


def test_subdomain_for():
    subdomain_nrk = subdomain_for("tv", "https://nrk.no")
    assert subdomain_nrk == "https://tv.nrk.no"

    many_levels = subdomain_for("many.levels.with-dashes", "http://niva.no")
    assert many_levels == "http://many.levels.with-dashes.niva.no"
