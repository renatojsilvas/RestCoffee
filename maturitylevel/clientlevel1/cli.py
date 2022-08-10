import argparse

from clientlevel0.core import place_order


def build_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    sp_create = subparsers.add_parser('create')
    sp_create.add_argument('coffee')
    sp_create.add_argument('size')
    sp_create.add_argument('milk')
    sp_create.add_argument('location')

    sp_update = subparsers.add_parser('update')
    sp_update.add_argument('id')
    sp_update.add_argument('coffee')
    sp_update.add_argument('size')
    sp_update.add_argument('milk')
    sp_update.add_argument('location')

    sp_delete = subparsers.add_parser('delete')
    sp_delete.add_argument('id')

    sp_read = subparsers.add_parser('read')
    sp_read.add_argument('id')


    return parser