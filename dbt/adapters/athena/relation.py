from dbt.adapters.base.relation import BaseRelation


class AthenaRelation(BaseRelation):
    DEFAULTS = {
        'metadata': {
            'type': 'AthenaRelation'
        },
        'quote_character': '',
        'quote_policy': {
            'database': False,
            'schema': False,
            'identifier': False,
        },
        'include_policy': {
            'database': False,
            'schema': True,
            'identifier': True,
        },
        'dbt_created': False,

    }

    SCHEMA = {
        'type': 'object',
        'properties': {
            'metadata': {
                'type': 'object',
                'properties': {
                    'type': {
                        'type': 'string',
                        'const': 'AthenaRelation',
                    },
                },
            },
            'type': {
                'enum': BaseRelation.RelationTypes + [None]
            },
            'path': BaseRelation.PATH_SCHEMA,
            'include_policy': BaseRelation.POLICY_SCHEMA,
            'quote_policy': BaseRelation.POLICY_SCHEMA,
            'quote_character': {'type': 'string'},
            'dbt_created': {'type': 'boolean'},
        },
        'required': ['metadata', 'type', 'path', 'include_policy',
                     'quote_policy', 'quote_character', 'dbt_created']
    }
