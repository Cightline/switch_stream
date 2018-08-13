#!/usr/bin/python

import pulsectl 
import argparse

pulse = pulsectl.Pulse()

def get_sink_indexes():
    sink_indexes = []

    for sink in pulse.sink_list():
        sink_indexes.append(str(sink.index))

    return sink_indexes


def get_default_sink():
    return pulse.get_sink_by_name(pulse.server_info().default_sink_name)


def sink_toggle(indexes):
     # Iterate through the index arguments given by the user 
     # and switch to the first non-default sink
     for index in indexes:
         index = index.strip()
         default_index = int(pulse.get_sink_by_name(pulse.server_info().default_sink_name).index)

         default_sink = get_default_sink()
        
         default_sink.mute = True
         #current_volume = default_sink.volume

         #current_volume.value_flat = 0.0
            
         #pulse.volume_set(default_sink, current_volume)

         #pulse.sink_input_volume_set(default_sink, current_volume)

            
         if int(index) != default_index:
             # Set the new default and mute the old sink
             pulse.sink_default_set(index)
             pulse.mute(default_sink, True)
               
             # Unmute the new sink
             new_sink  = pulse.get_sink_by_name(pulse.server_info().default_sink_name)
             pulse.mute(new_sink, False)



             print('the default sink has been set to index: %s, name: %s' % (index, get_default_sink().name))
             break


def move_streams():
    count         = 0
    streams       = pulse.sink_input_list()
    default_index = int(pulse.get_sink_by_name(pulse.server_info().default_sink_name).index)

    for stream in streams:
        #print('moved stream: %s to the default sink' % (stream.name))
        pulse.sink_input_move(stream.index, default_index)
        count += 1

        print('moved %s streams' % (count))

 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
   
    parser.add_argument('--manual-sink-toggle', action='store', nargs='+', type=str, help='example: --manual-sink-toggle 0 2', metavar='[sink index]')
    parser.add_argument('--move-streams',       action='store_true', help='this will move all streams to the new default sink')
    parser.add_argument('--auto',               action='store_true', help='automatically move all streams to the next sink')

    args = parser.parse_args()

    sinks = pulse.sink_list()

    if not args.auto and not args.manual_sink_toggle and not args.move_streams:
        print('No arguments specified')
        exit()

    # If they give no arguments, or only --auto
    if args.auto == True:
        sink_toggle(get_sink_indexes())

    # They manually specified the sinks to toggle between
    elif args.manual_sink_toggle:
        sink_toggle(args.manual_sink_toggle)

    
    # Take all the streams and move them to the (new) default sink. 
    if args.move_streams:
        move_streams()
   


