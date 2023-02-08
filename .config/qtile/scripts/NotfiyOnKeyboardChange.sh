#!/bin/bash

# Set a flag for the initial state of the keyboard layout
layout_state=0

while true; do
  # Get the current keyboard layout
  current_layout=$(setxkbmap -query | awk '/layout/{print $2}')

  # Check if the keyboard layout has changed
  if [ "$layout_state" != "$current_layout" ]; then
    # Update the flag with the current keyboard layout
    layout_state="$current_layout"

    # Create a notification with the new keyboard layout
    notify-send "Keyboard layout switched to: $layout_state"
  fi

  # Sleep for a short period before checking the layout again
  sleep 1
done