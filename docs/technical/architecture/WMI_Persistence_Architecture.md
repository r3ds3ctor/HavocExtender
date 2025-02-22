# WMI Persistence Module Architecture

## Overview
The WMI Persistence module creates persistence using Windows Management Instrumentation (WMI) event subscriptions.

## Components
- **Event Filter**: Defines the event that triggers the persistence.
- **Event Consumer**: Defines the action to take when the event is triggered.
- **Binding**: Links the filter and consumer.

## Workflow
1. The module creates an event filter.
2. It creates an event consumer.
3. It binds the filter and consumer.

## Dependencies
- **Python**: The module is written in Python.
- **WMI**: Used to interact with WMI.

## Limitations
- Only works on Windows systems.
- Requires administrative privileges for some operations.