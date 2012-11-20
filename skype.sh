#!/bin/sh

# parses --dbpath argument from skype args ignores everything else
parse_args() {
	local arg
	while [ $# -gt 0 ]; do
		case "$1" in
		--dbpath)
			SKYPE_DIR=$2
			return
		;;
		--dbpath=*)
			SKYPE_DIR=${1#--dbpath=}
			return
		;;
		esac
		shift
	done
}

# Legacy dir
SKYPE_DIR="$HOME/.Skype"

# XDG path
if [ ! -d "$SKYPE_DIR" ]; then
	SKYPE_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/Skype"
fi

parse_args "$@"

if [ ! -d "$SKYPE_DIR" ]; then
	install -d "$SKYPE_DIR"
fi

if [ -f "$SKYPE_DIR/env" ]; then
	. "$SKYPE_DIR/env"
fi

exec /usr/lib/skype --dbpath="$SKYPE_DIR" "$@"
