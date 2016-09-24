


def post_here(context):
    data = context.request.parent_request.get('data')
    raise "got here"
    for addon in data:
        db.add(id=addon['id'], version=addon['installedVersion'],
               title=addon['title'], site=site, user=user)