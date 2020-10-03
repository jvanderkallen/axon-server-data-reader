# Axon Server Data Reader
This is a small CLI application that allows you to read events or snapshots from an [Axon Server](https://github.com/AxonIQ/axon-server-se) segment.

Axon Server uses a custom file format for events and snapshots. This makes it difficult to read events and snapshots without spinning up Axon Server and using its API. Luckily the Standard Edition is open source and it turns out the file format isn't that complicated. The file format is the same for the Enterprise Edition (which is closed source).

You can either read events from an event segment or snapshots from a snapshot segment. Event segment files have .events as extension while snapshot segments have .snapshots as extension. The filename of an event segment may look like this: `00000000000000000000.events`. The filename of a snapshot segment may look like this: `00000000000000000000.snapshots`.

## Usage
```sh
usage: axon-server-data-reader.py [-h] -f FILE [-n NUMBER]

Read events from an Axon Server event segment file.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  path to the event segment file
  -n NUMBER, --number NUMBER
                        event number to read (default: read all events)
```

## Development
`event.proto` was compiled with [protoc](https://github.com/protocolbuffers/protobuf/releases): `protoc ./event.proto`.