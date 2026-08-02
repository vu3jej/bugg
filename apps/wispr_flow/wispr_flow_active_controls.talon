mode: sleep
tag: user.wispr_flow_active
-
parrot(shush):
    user.stop_dictation()

[scribble] done:
    user.stop_dictation()

scratch [that]:
    user.cancel_dictation()
