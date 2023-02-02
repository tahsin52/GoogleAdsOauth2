from google.ads.googleads.errors import GoogleAdsException

from ga_runner import create_client, handleGoogleAdsException

_VERSION = "v11"


def list_accessible_customers(token):
    client = create_client(token)
    try:
        customer_service = client.get_service("CustomerService", version=_VERSION)
        accessible_customers = customer_service.list_accessible_customers()
        resource_names = [resource_name for resource_name in accessible_customers.resource_names]
        return resource_names
    except GoogleAdsException as ex:
        handleGoogleAdsException(ex)