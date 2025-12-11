from typing import Dict, Callable, Any

class Plugin:
    def __init__(self, name: str, manifest: Dict[str, Any], handler: Callable[..., Any]):
        self.name = name
        self.manifest = manifest
        self.handler = handler
        self.enabled = False

class PluginManager:
    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}

    def register(self, plugin: Plugin):
        # manifest validation should happen before register
        self.plugins[plugin.name] = plugin

    def enable(self, name: str):
        if name in self.plugins:
            # In production, require human approval before enabling
            self.plugins[name].enabled = True

    def disable(self, name: str):
        if name in self.plugins:
            self.plugins[name].enabled = False

    def handle(self, name: str, *args, **kwargs):
        p = self.plugins.get(name)
        if p and p.enabled:
            return p.handler(*args, **kwargs)
        raise RuntimeError("plugin-not-enabled-or-missing")
