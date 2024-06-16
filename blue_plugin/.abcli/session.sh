#! /usr/bin/env bash

function blue_plugin_session() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "start" ]; then
        abcli_log "blue-plugin: session started."

        # session code here

        abcli_log "blue-plugin: session ended."
        return
    fi

    abcli_log_error "-blue-plugin: session: $task: command not found."
    return 1
}
