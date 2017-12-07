# switch_stream
A Python script to switch all of your Pulseaudio streams 


Example usage:

This will toggle between the 2 sinks specified (1 and 2). After switching the default sink the script will move all of the channels to the new sink. 
```
python switch.py --default-sink-toggle 1 2 --move-streams
```

