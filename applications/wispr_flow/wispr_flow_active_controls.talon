mode: sleep
tag: user.wispr_flow_active
-
memo:
    user.restart_dictation()

[memo] (done | wrap):
    user.stop_dictation()

scratch [that]:
    user.cancel_dictation()
