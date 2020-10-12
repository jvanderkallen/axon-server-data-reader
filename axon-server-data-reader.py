#!/usr/bin/env python3
import argparse

import event_segment_reader
from event_pb2 import Event

EVENT_FIELDS = ['message_identifier', 'aggregate_identifier', 'aggregate_sequence_number', 'aggregate_type', 'timestamp', 'payload', 'meta_data', 'snapshot']


def print_event(event: Event, fields: list):
    sorted_fields = fields.copy()
    sorted_fields.sort()

    for field in sorted_fields:
        print('{}: {}'.format(field, event.__getattribute__(field)))


def parse_args():
    parser = argparse.ArgumentParser(description='Read events from an Axon Server event segment file.')
    parser.add_argument('-f', '--file', required=True, help='path to the event segment file', type=str)
    parser.add_argument('-n', '--number', help='event number to read (default: read all events)', type=int, required=False)
    parser.add_argument('--fields', help='fields to display', nargs='*', choices=EVENT_FIELDS, type=str, required=False, default=EVENT_FIELDS)
    return parser.parse_args()


def main():
    args = parse_args()

    segment = event_segment_reader.EventSegmentReader(args.file)

    if args.number is None:
        for event in segment.read_events():
            print_event(event, args.fields)
    else:
        print_event(segment.read_event(args.number), args.fields)


if __name__ == '__main__':
    main()
