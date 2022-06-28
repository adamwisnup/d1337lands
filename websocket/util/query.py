from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

graphql_endpoint_url = "http://localhost:3333/v1/graphql"
hasura_admin_secret = "hSK6kPeZN2zTLsvd2grPNtapLbeNzD9QU9aPd38f894JsmxM7Ecpb9hkAxeX"


def call_request(query, variable_data, token=hasura_admin_secret):
    if token == hasura_admin_secret:
        transport = RequestsHTTPTransport(
            url=graphql_endpoint_url,
            verify=True,
            retries=3,
            headers={
                "content-type": "application/json",
                "x-hasura-admin-secret": hasura_admin_secret,
                "Authorization": "Bearer {}".format(token),
            },
        )
    else:
        transport = RequestsHTTPTransport(
            url=graphql_endpoint_url,
            verify=True,
            retries=3,
            headers={
                "content-type": "application/json",
                "x-hasura-admin-secret": hasura_admin_secret,
                "Authorization": "Bearer {}".format(token),
            },
        )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    return client.execute(gql(query), variable_values=variable_data)