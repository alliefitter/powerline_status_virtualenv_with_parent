from os.path import basename
from pathlib import PurePath

from powerline.theme import requires_segment_info


@requires_segment_info
def virtualenv(pl, segment_info):
    venv = segment_info['environ'].get('VIRTUAL_ENV', '')
    path = PurePath(venv)
    if len(path.parts) > 1:
        name = '/'.join(path.parts[-2:])
    else:
        name = basename(venv)
    return name or None
