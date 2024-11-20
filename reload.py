
#! Run this script in Blender's Python console to reload the addon.
### Reloads an addon in Blender without restarting the application.
import bpy # type: ignore
import importlib
import os
import sys

# Path to your addon folder
ADDON_PATH = r"C:\Users\marti\OneDrive\Desktop\pythonShit"
ADDON_NAME = "microZoomer"  # Your addon folder/module name

# List of additional files (without .py extension) to reload
FILES_TO_RELOAD = [
    "editRR",  # Add other files here, e.g., "other_module"
]

def force_reload_addon():
    print(f"Force reloading addon: {ADDON_NAME} from {ADDON_PATH}")
    
    # Ensure the addon path is in sys.path
    if ADDON_PATH not in sys.path:
        sys.path.append(ADDON_PATH)
    
    # Add microZoomer path to sys.path if not already present
    microZoomer_path = os.path.join(ADDON_PATH, ADDON_NAME)
    if microZoomer_path not in sys.path:
        sys.path.append(microZoomer_path)
    
    # Get all modules related to the addon
    to_reload = [name for name in sys.modules if name.startswith(ADDON_NAME)]
    
    # Add the files listed in FILES_TO_RELOAD
    for file_name in FILES_TO_RELOAD:
        to_reload.append(f"{ADDON_NAME}.{file_name}")
    
    # Unload all related modules
    for module_name in to_reload:
        if module_name in sys.modules:
            module = sys.modules[module_name]
            if hasattr(module, "unregister"):
                try:
                    module.unregister()
                    print(f"Unregistered module: {module_name}")
                except Exception as e:
                    print(f"Error during unregister for {module_name}: {e}")
            del sys.modules[module_name]
            print(f"Unloaded module: {module_name}")

    # Reload the main addon module and additional files
    try:
        # Reload each file in FILES_TO_RELOAD
        for file_name in FILES_TO_RELOAD:
            try:
                submodule = __import__(f"{ADDON_NAME}.{file_name}")
                importlib.reload(submodule)
                print(f"Reloaded {file_name} successfully!")
            except Exception as e:
                print(f"Error reloading {file_name}: {e}")

        # Reload the main addon module
        addon = __import__(ADDON_NAME)
        importlib.reload(addon)

        # Register the main addon again
        if hasattr(addon, "register"):
            addon.register()
        print(f"Addon '{ADDON_NAME}' reloaded successfully!")

    except Exception as e:
        print(f"Error reloading addon: {e}")

# Run the reload function
force_reload_addon()
