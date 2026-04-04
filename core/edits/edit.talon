# go <user.repeatable_motion>+: user.execute_motions(repeatable_motion_list)

go <user.navigation_step>+:
    user.execute_navigation_steps(navigation_step_list)
<user.edit_action><user.edit_modifier>:
    user.dispatch_edit_command(edit_action,edit_modifier)

<user.delimiter_pair>:
    user.insert_delimiter_pair(delimiter_pair)
    key(left)

find that:
    edit.find()
find next:
    edit.find_next()
find previous:
    edit.find_previous()

scroll up:
    edit.page_up()
scroll down:
    edit.page_down()

go page up:
    edit.page_up()
go page down:
    edit.page_down()

go line start|head:
    edit.line_start()
go line end|tail:
    edit.line_end()

go way left:
    edit.line_start()
go way right:
    edit.line_end()
go way up:
    edit.file_start()
go way down:
    edit.file_end()

go top:
    edit.file_start()
go bottom:
    edit.file_end()

indent [more]:
    edit.indent_more()
indent less|out dent:
    edit.indent_less()

cut that:
    edit.cut()
copy that:
    edit.copy()
(pace|paste) that:
    edit.paste()
paste and match style:
    edit.paste_match_style()

clone that:
    edit.selection_clone()
clone line:
    edit.line_clone()

undo that:
    edit.undo()
redo that:
    edit.redo()

[insert] new line above:
    # edit.insert_line_up()
    edit.line_insert_up()
[insert] new line below|slap:
    # edit.insert_line_down()
    edit.line_insert_down()

save file:
    edit.save()
save all files:
    edit.save_all()

[go] line mid:
    user.line_middle()

zoom in:
    edit.zoom_in()
zoom out:
    edit.zoom_out()
reset zoom:
    edit.zoom_reset()
