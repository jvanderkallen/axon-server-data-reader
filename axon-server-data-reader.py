#!/usr/bin/env python3
import argparse
import event_segment


def main():
    parser = argparse.ArgumentParser(description='Read events from an Axon Server event segment file.')
    parser.add_argument('-f', '--file', required=True, help='path to the event segment file', type=str)
    parser.add_argument('-n', '--number', help='event number to read (default: read all events)', type=int, default=-1)
    args = parser.parse_args()

    segment = event_segment.EventSegment(args.file)

    if args.number == -1:
        for event in segment.read_events():
            print(event)
    else:
        print(segment.read_event(args.number))


if __name__ == '__main__':
    main()
