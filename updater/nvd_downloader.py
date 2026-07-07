import requests


NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def download_cves(results_per_page=2000):
    """
    Download CVEs from the NVD API.
    """

    params = {
        "resultsPerPage": results_per_page
    }

    response = requests.get(NVD_API, params=params, timeout=30)

    response.raise_for_status()

    return response.json()

