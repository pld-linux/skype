#!/bin/sh

# Legacy dir
SKYPE_DIR="$HOME/.Skype"

# XDG path
if [ ! -d "$SKYPE_DIR" ]; then
	SKYPE_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/Skype"
fi

if [ ! -d "$SKYPE_DIR" ]; then
	install -d "$SKYPE_DIR"
fi

if [ -f "$SKYPE_DIR/env" ]; then
	. "$SKYPE_DIR/env"
fi

exec /usr/lib/skype --dbpath="$SKYPE_DIR" "$@"
