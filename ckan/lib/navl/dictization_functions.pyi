"""
This type stub file was generated by pyright.
"""

import json

class Missing(object):
    def __unicode__(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __int__(self) -> int:
        ...
    
    def __complex__(self):
        ...
    
    def __long__(self):
        ...
    
    def __float__(self):
        ...
    
    def __oct__(self):
        ...
    
    def __hex__(self):
        ...
    
    def __len__(self):
        ...
    


missing = Missing()
class State(object):
    ...


class DictizationError(Exception):
    def __str__(self) -> str:
        ...
    
    def __unicode__(self):
        ...
    
    def __repr__(self):
        ...
    


class Invalid(DictizationError):
    '''Exception raised by some validator, converter and dictization functions
    when the given value is invalid.

    '''
    def __init__(self, error, key=...) -> None:
        ...
    


class DataError(DictizationError):
    def __init__(self, error) -> None:
        ...
    


class StopOnError(DictizationError):
    '''error to stop validations for a particualar key'''
    ...


def flattened_order_key(key):
    '''order by key length first then values'''
    ...

def flatten_schema(schema, flattened=..., key=...):
    '''convert schema into flat dict, where the keys become tuples

    e.g.
    {
      "toplevel": [validators],
      "parent": {
        "child1": [validators],
        "child2": [validators],
        }
    }
    becomes:
    {
      ('toplevel',): [validators],
      ('parent', 'child1'): [validators],
      ('parent', 'child2'): [validators],
    }
    See also: test_flatten_schema()
    '''
    ...

def get_all_key_combinations(data, flattened_schema):
    '''Compare the schema against the given data and get all valid tuples that
    match the schema ignoring the last value in the tuple.

    '''
    ...

def make_full_schema(data, schema):
    '''make schema by getting all valid combinations and making sure that all
    keys are available'''
    ...

def augment_data(data, schema):
    '''Takes 'flattened' data, compares it with the schema, and returns it with
    any problems marked, as follows:

    * keys in the data not in the schema are moved into a list under new key
      ('__junk')
    * keys in the schema but not data are added as keys with value 'missing'

    '''
    ...

def convert(converter, key, converted_data, errors, context):
    ...

def validate(data, schema, context=...):
    '''Validate an unflattened nested dict against a schema.'''
    ...

def flatten_list(data, flattened=..., old_key=...):
    '''flatten a list of dicts'''
    ...

def flatten_dict(data, flattened=..., old_key=...):
    '''Flatten a dict'''
    ...

def unflatten(data):
    '''Unflatten a simple dict whose keys are tuples.

    e.g.
    >>> unflatten(
      {('name',): u'testgrp4',
       ('title',): u'',
       ('description',): u'',
       ('packages', 0, 'name'): u'testpkg',
       ('packages', 1, 'name'): u'testpkg',
       ('extras', 0, 'key'): u'packages',
       ('extras', 0, 'value'): u'["testpkg"]',
       ('extras', 1, 'key'): u'',
       ('extras', 1, 'value'): u'',
       ('state',): u'active'
       ('save',): u'Save Changes',
       ('cancel',): u'Cancel'})
    {'name': u'testgrp4',
     'title': u'',
     'description': u'',
     'packages': [{'name': u'testpkg'}, {'name': u'testpkg'}],
     'extras': [{'key': u'packages', 'value': u'["testpkg"]'},
                {'key': u'', 'value': u''}],
     'state': u'active',
     'save': u'Save Changes',
     'cancel': u'Cancel'}
    '''
    ...

class MissingNullEncoder(json.JSONEncoder):
    '''json encoder that treats missing objects as null'''
    def default(self, obj):
        ...
    


def check_dict(data_dict, select_dict, parent_path=...):
    """
    return list of key tuples from select_dict whose values don't match
    corresponding values in data_dict.
    """
    ...

def check_list(data_list, select_list, parent_path=...):
    """
    return list of key tuples from select_list whose values don't match
    corresponding values in data_list.
    """
    ...

def resolve_string_key(data, string_key):
    """
    return (child, parent_path) if string_key is found in data
    raise DataError on incompatible types or key not found.

    supports partial-id keys for lists of dicts (minimum 5 hex digits)
    e.g. `resources__1492a` would select the first matching resource
    with an id field matching "1492a..."
    """
    ...

def check_string_key(data_dict, string_key, value):
    """
    return list of key tuples from string_key whose values don't match
    corresponding values in data_dict.

    raise DataError on incompatible types such as checking for dict values
    in a list value.
    """
    ...

def filter_glob_match(data_dict, glob_patterns):
    """
    remove keys and values from data_dict in-place based on glob patterns.

    glob patterns are string_keys with optional '*' keys matching everything
    at that level. a '+' prefix on the glob pattern indicates values to
    protect from deletion, where the first matching pattern "wins".
    """
    ...

def update_merge_dict(data_dict, update_dict, parent_path=...):
    """
    update data_dict keys and values in-place based on update_dict.

    raise DataError on incompatible types such as replacing a dict with a list
    """
    ...

def update_merge_list(data_list, update_list, parent_path=...):
    """
    update data_list entries in-place based on update_list.

    raise DataError on incompatible types such as replacing a dict with a list
    """
    ...

def update_merge_string_key(data_dict, string_key, value):
    """
    update data_dict entries in-place based on string_key and value.
    Also supports extending existing lists with `__extend` suffix.

    raise DataError on incompatible types such as replacing a dict with a list
    """
    ...
