from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# GraphQL endpoint URL
GRAPHQL_ENDPOINT = "http://graphql-engine:8080/v1/graphql"


def handle_insert(row, client):
    id = str(row['id'])
    # In reality you would follow the URL from row['url']
    content = "dummy content"
    gql_query = gql("""
            mutation insertItem($id: text!, $content: text!) {
                insert_Resume_one(object: { application_id: $id, content: $content }) {
                    id
                }
            }
        """)
    print(client.execute(gql_query, variable_values={
        'id': id, 'content': content}))


def handle_delete(row, client):
    id = row['id']
    gql_query = gql("""
            mutation deleteItem($id: text!) {
                delete_Resume(where: {application_id: { _eq: $id } }) {
                    affected_rows
                }
            }
        """)
    print(client.execute(gql_query, variable_values={
        'id': id}))


def handle_event(event):
    gql_headers = {'x-hasura-admin-secret': 'secret'}
    # Create a GraphQL client with the request transport
    transport = RequestsHTTPTransport(
        url=GRAPHQL_ENDPOINT, headers=gql_headers)
    client = Client(transport=transport)

    event = event['event']
    op = event['op']
    if op == 'INSERT':
        row = event['data']['new']
        handle_insert(row, client)
    elif op == 'UPDATE':
        old_row = event['data']['old']
        new_row = event['data']['new']
        # TODO: Do something
    elif op == 'DELETE':
        old_row = event['data']['old']
        handle_delete(old_row, client)
    else:
        print(str(event))
    return "Success"
