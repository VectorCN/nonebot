"""
This filter just log message to stdout.
"""

from filter import add_filter


def _log_message(ctx_msg):
    print(ctx_msg.get('sender', '')
          + (('@' + ctx_msg.get('group')) if ctx_msg.get('type') == 'group_message' else '')
          + (('@' + ctx_msg.get('discuss')) if ctx_msg.get('type') == 'discuss_message' else '')
          + ': ' + ctx_msg.get('content'))


add_filter(_log_message, 1000)