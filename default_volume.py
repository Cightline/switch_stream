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

def get_volumes():
    return get_default_sink().volume.values


def relative_volume(percentage):
    #volumes = get_volumes()
    #sum_    = sum(volumes)
    #avg     = sum_/len(volumes)

    #print(avg)

    sink = pulse.sink_list()[get_default_sink().index]
    pulse.volume_change_all_chans(sink, percentage)

def set_volume(percentage):
    sink = pulse.sink_list()[get_default_sink().index]
    pulse.volume_set_all_chans(sink, percentage)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
   
    parser.add_argument('--set-volume',      action='store',      type=int, help='example: --set-volume 50')
    parser.add_argument('--increase-volume', action='store',      type=int, help='example: --increase-volume 3')
    parser.add_argument('--decrease-volume', action='store',      type=int, help='example: --decrease-volume 3')
    parser.add_argument('--mute',            action='store_true',           help='mute the default sink, you can also just run --set-volume 0')

    args = parser.parse_args()

  
    if args.set_volume:
        set_volume(args.set_volume/100)

    elif args.increase_volume:
        relative_volume(args.increase_volume/100)

    elif args.decrease_volume:
        relative_volume(-args.decrease_volume/100)

    elif args.mute:
        set_volume(0)


    
    else:
        print('No arguments specified')


