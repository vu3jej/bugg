# VoiceOver
os: mac
-

voiceover activate | voiceover press:
    key(ctrl-alt-space)
voiceover interact | voiceover drill in:
    key(ctrl-alt-shift-down)
voiceover read all:
    key(ctrl-alt-a)
voiceover next heading:
    key(ctrl-alt-cmd-h)
voiceover next link:
    key(ctrl-alt-cmd-l)
voiceover previous heading:
    key(ctrl-alt-shift-cmd-h)
voiceover previous link:
    key(ctrl-alt-shift-cmd-l)
voiceover find [text]:
    key(ctrl-alt-f)
voiceover find [text] backward:
    key(ctrl-alt-shift-g)
voiceover find [text] forward:
    key(ctrl-alt-g)
voiceover select next item:
    key(ctrl-alt-right)
voiceover select previous item:
    key(ctrl-alt-left)
voiceover actions:
    key(ctrl-alt-cmd-space)
voiceover applications:
    key(ctrl-alt-fn-f1)
    sleep(0.2)
    key(ctrl-alt-fn-f1)
voiceover commands:
    key(ctrl-alt-h)
    sleep(0.2)
    key(ctrl-alt-h)
voiceover contextual menu:
    key(ctrl-alt-shift-m)
voiceover [show] item chooser:
    key(ctrl-alt-i)
voiceover notification menu:
    key(ctrl-alt-n)
voiceover rotor:
    key(ctrl-alt-u)
voiceover verbosity [rotor]:
    key(ctrl-alt-v)
voiceover help:
    key(ctrl-alt-shift-h)
voiceover hint | voiceover give me a hint:
    key(ctrl-alt-shift-n)
voiceover describe image:
    key(ctrl-alt-shift-l)
voiceover where am i | voiceover orientation:
    key(ctrl-alt-fn-f3)
voiceover stop interacting | voiceover stop interact | voiceover drill out:
    key(ctrl-alt-shift-up)
