from time import sleep

from typing import Optional
from datetime import datetime


def log(message: str, when: Optional[datetime]=None):
    """Log a message with a timestamp

    Args:
        message: Message to print
        when: datetime of when the message occurred.
             Default to the present time
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log('hello')
sleep(0.2)
log('hello again')
