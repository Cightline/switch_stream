#!/usr/bin/python

import pulsectl 
import argparse

pulse = pulsectl.Pulse()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--default-sink-toggle', action='store', nargs='+', help='--default-sink [index_of_the_sink]')
    parser.add_argument('--move-streams', action='store_true', help='move all streams to the new default sink')

    args = parser.parse_args()

    if args.default_sink_toggle:

        # Iterate through the index arguments given by the user 
        # and switch to the first non-default sink
        for index in args.default_sink_toggle:

            default_index = int(pulse.get_sink_by_name(pulse.server_info().default_sink_name).index)


            
            if int(index) != default_index:
                pulse.sink_default_set(index)
                print('default sink set to index: %s' % (index))
                break

    if args.move_streams:
        count         = 0
        streams       = pulse.sink_input_list()
        default_index = int(pulse.get_sink_by_name(pulse.server_info().default_sink_name).index)

        for stream in streams:
            #print('moved stream: %s to the default sink' % (stream.name))
            pulse.sink_input_move(stream.index, default_index)
            count += 1

        print('moved %s streams' % (count))



