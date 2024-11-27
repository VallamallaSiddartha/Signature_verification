# myapp/apps.py

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
    def ready(self):
        """
        This method is executed when the application is fully loaded. 
        It ensures imports or initializations are delayed until the app is ready, 
        preventing circular imports or reentrant errors.
        """
        try:
            # Import load_bi_rnn_model if it needs to run at startup
            from .views import load_bi_rnn_model
        except ImportError:
            # Handle any error if the module cannot be imported
            pass
        
        try:
            # Import signals if a signals.py file is used in the app
            from . import signals
        except ImportError:
            # Handle cases where signals.py doesn't exist or isn't needed
            pass
