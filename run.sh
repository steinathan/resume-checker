#!/bin/bash

while true; do
    # Your command goes here
    fly deploy --local-only

    
    # Check the exit status of the last command
    if [ $? -eq 0 ]; then
        echo "Command executed successfully. Exiting."
        break
    else
        echo "Command failed. Restarting..."
    fi

    # You can add a delay between retries if needed
    sleep 1
done
