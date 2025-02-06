from .models import StudyLog
import after_response
import logging
from datetime import datetime

logger = logging.getLogger("operations")
@after_response.enable
def log_event(request_method, event, message, timestamp):
    logger.info(f"Logging started.. {datetime.now()}")
    StudyLog.objects.create(request_method=request_method,event=event,message=message,timestamp=timestamp)