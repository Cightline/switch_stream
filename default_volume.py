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

    sinks        = pulse.sink_list()
    default_sink = get_default_sink().index

    for sink in sinks:
        if sink.index == default_sink:
            pulse.volume_change_all_chans(sink, percentage)
            break

def set_volume(percentage):
    sink = pulse.sink_list()[get_default_sink().index]
    pulse.volume_set_all_chans(sink, percentage)


def mute_toggle():
    sink = pulse.sink_list()[get_default_sink().index]

    if sink.mute == 1:
        pulse.mute(sink, False)

    else:
        pulse.mute(sink)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
   
    parser.add_argument('--set-volume',      action='store',      type=int, help='example: --set-volume 50')
    parser.add_argument('--increase-volume', action='store',      type=int, help='example: --increase-volume 3')
    parser.add_argument('--decrease-volume', action='store',      type=int, help='example: --decrease-volume 3')
    parser.add_argument('--toggle-mute',     action='store_true',           help='toggles mute on the default sink')

    args = parser.parse_args()

  
    if args.set_volume:
        set_volume(args.set_volume/100)

    elif args.increase_volume:
        relative_volume(args.increase_volume/100)

    elif args.decrease_volume:
        relative_volume(-args.decrease_volume/100)

    elif args.toggle_mute:
        mute_toggle()


    
    else:
        print('No arguments specified')


