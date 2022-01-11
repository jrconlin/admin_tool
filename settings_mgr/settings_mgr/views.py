from django.http import HttpResponse
from typing import List, Dict
from collections.abc import Iterable, Mapping

def index(request):
    """Stub function to handle incoming requests to the main index page.

    See

    """
    return HttpResponse(
        """Hi, this isn't what you wanted. You probably want <a href="/admin/">/admin/</a>""")

"""
TODO: this is basically glorified prototype code just to capture thoughts.
Feel free to toss it all.
"""

class Advertiser_Paths:
    value:str
    matching:str # either "prefix" or "strict"

    def render():
        """Render self as Django editable object"""

    def validate(request):
        """Validate the data in request, returning errors for display"""

class Advertiser_Urls:
    host:str
    paths:List[Advertiser_Paths] # Optional

    def render():
        """Render self as Django editable object"""

    def validate(request):
        """Validate the data in request, returning errors for display"""

class ADM_Setting:
    advertiser_urls:List[Advertiser_Urls]
    impression_hosts:List[str]  # Optional
    click_hosts:List[str]       # Optional
    include_regions:List[str]   # Optional, defaults to all

    def render():
        """Render self as Django editable object"""

    def validate(request):
        """Validate the data in request, returning errors for display"""


def fetch_bucket(bucket_name:str) -> Dict[str, ADM_Setting]:
    """Fetch the contents of `bucket_name` from GCP storage

    This will be triggered by the GET request for the page.
    """

def write_bucket(bucket_name:str, content:ADM_Setting):
    """Write the content of `bucket_name` as JSON to GCP storage.

    This will be triggered by the "Save" action of the page.
    """

def render_view(request):
    """Fetch bucket from request and render the content as editable

    Request would contain the bucket to pull (defaulting to the main
    ADM Settings bucket entry). The view would be rendered according
    to the various renderers. NOTE: make sure that the special case
    DEFAULT object is rendered first and contains the default values.

    This should probably be a URL endpoint.
    """

def update_from(request):
    """Update from the POST content supplied by the request

    Call the various `validate()` functions to validate and update self.

    This should probably be a URL endpoint.
    """