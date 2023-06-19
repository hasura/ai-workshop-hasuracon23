def handle_event(event):
    event = event['event']
    op = event['op']
    if op == 'INSERT':
        row = event['data']['new']
        # TODO: Do something
    elif op == 'UPDATE':
        old_row = event['data']['old']
        new_row = event['data']['new']
        # TODO: Do something
    elif op == 'DELETE':
        old_row = event['data']['old']
        # TODO: Do something
    else:
        print(str(event))
    return "Success"