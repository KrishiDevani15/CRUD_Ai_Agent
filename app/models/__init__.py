# app/models/__init__.py
import importlib
import pkgutil
# Dynamically import all model modules to register them with SQLAlchemy
for _, module_name, _ in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{module_name}")