# switch_stream
A Python script to switch all of your Pulseaudio streams 


Example usage:

This will toggle between the 2 sinks specified (1 and 2). After switching the default sink the script will move all of the channels to the new sink. 
```
python switch.py --default-sink-toggle 1 2 --move-streams
```

Installation:

``` 
pip install pulsectl

cp switch_stream.py /usr/bin/switch_stream
chmod +x /usr/bin/switch_stream

```

Usage:

This is what I have in my i3 configuration file. 

```
bindsym Control+XF86AudioMute exec "switch_stream --auto --move-streams; polybar-msg hook show_sink 1"
```

Polybar module
```
[module/show_sink]
type     = custom/ipc
hook-0 = /usr/bin/switch_stream --show-short
initial = 1
format = <output>
format-prefix-foreground = ${colors.foreground-alt}
format-prefix = "SINK: "
```




