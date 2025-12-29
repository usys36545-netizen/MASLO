# Cooking Guide Application - Decomposed Structure

This application has been restructured into multiple modules for better maintainability and organization.

## File Structure

- `main_app.py` - Main application logic and entry point
- `ui_handler.py` - UI management and element interactions
- `config.py` - Configuration constants, recipes, and styles
- `MASLO.ui` - Original UI file (unchanged)
- `MASSSSLOO.py` - Original monolithic file (preserved)

## Modules

### main_app.py
Contains the main application class `CookingGuideApp` which orchestrates the application flow. It handles the logic for recipe selection and dark mode toggling.

### ui_handler.py
Handles all UI-related operations including loading the UI file, connecting signals, and updating UI elements. This separates the UI concerns from the application logic.

### config.py
Contains all configuration data including recipe texts and the dark mode stylesheet. This makes it easy to modify content without changing the application code.

## Benefits of Decomposition

1. **Separation of Concerns**: Each module has a specific responsibility
2. **Maintainability**: Easier to update individual components
3. **Reusability**: UI handler can potentially be reused in other applications
4. **Testability**: Individual modules can be tested separately
5. **Readability**: Code is more organized and easier to understand

## Running the Application

To run the decomposed application, use:
```
python main_app.py
```

The functionality remains exactly the same as the original monolithic version.