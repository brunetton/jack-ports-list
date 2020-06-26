# jack-ports-list

Simple (Python) script to list Jack ports by:
- inputs
- outputs
- midi ports
- audio ports

## Example

```sh
$ ./jack-ports-list
** INPUTS
system:playback_1
system:playback_2
setBfree DSP Tonewheel Organ:control
PulseAudio JACK Source:front-left
MIDI monitor:midi_in
jack-keyboard:midi_in
a2j:Midi Through [14] (playback): Midi Through Port-0
a2j:openstage [131] (playback): midi_in
PulseAudio JACK Source:front-right

** OUTPUTS
setBfree DSP Tonewheel Organ:outL
setBfree DSP Tonewheel Organ:outR
setBfree DSP Tonewheel Organ:notify
PulseAudio JACK Sink:front-left
PulseAudio JACK Sink:front-right
jack-keyboard:midi_out
a2j:Midi Through [14] (capture): Midi Through Port-0
a2j:openstage [132] (capture): midi_out

$ ./jack-ports-list --midi --inputs
** MIDI INPUTS
setBfree DSP Tonewheel Organ:control
MIDI monitor:midi_in
jack-keyboard:midi_in
a2j:Midi Through [14] (playback): Midi Through Port-0
a2j:openstage [131] (playback): midi_in
```

## Installation

```
pip install -r requirements.txt
```

## TODO

- make it globally installable (via pip)
