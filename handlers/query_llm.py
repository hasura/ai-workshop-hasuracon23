from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# GraphQL endpoint URL
GRAPHQL_ENDPOINT = "http://localhost:8080/v1/graphql"


def query_llm(request, headers):
    user_query = request['input']['user_query']

    # Add authenticated session variables as headers along with the admin secret
    gql_headers = request['session_variables']
    gql_headers['x-hasura-admin-secret'] = headers['x-hasura-admin-secret']

    # Create a GraphQL client with the request transport
    transport = RequestsHTTPTransport(url=GRAPHQL_ENDPOINT, headers=gql_headers)
    client = Client(transport=transport)

    # Send the GraphQL request
    gql_query = gql("""
            query getChunks($user_query: text!) {
                DocumentChunk(where: { vector: { near_text: $user_query}}) {
                    chunk_text
                }
            }
        """)
    result = client.execute(gql_query, variable_values={
                            'user_query': user_query})

    # TODO: Call LLM
    return str(result)
