from django.db.models import Q

from earth.base import timestamp_to_datetime


def default_build_query_hook(action, request, *args, **kwargs):
    action.query = Q()

    query_keys = action._query_keys

    for query_key in query_keys:

        query_key_dict = {
            query_key: query_key,
            query_key + '_gt': query_key + '__gt',
            query_key + '_gte': query_key + '__gte',
            query_key + '_lt': query_key + '__lt',
            query_key + '_lte': query_key + '__lte',
        }

        for key, value in query_key_dict.items():
            query_value = getattr(action, key, None)

            if query_value:
                if 'timestamp' in key:
                    query_value = timestamp_to_datetime(
                        int(query_value)
                    )

                q_params = {
                    value: query_value
                }

                action.query.add(
                    Q(**q_params),
                    Q.AND
                )

    if '_valid_order_by' in action.__dict__:
        if 'order_by' in action.__dict__:
            if action.order_by not in action._valid_order_by:
                action.ret('016').msg('invalid_order_by')
                return False

    return True
