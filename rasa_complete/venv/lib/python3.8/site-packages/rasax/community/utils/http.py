import logging
from typing import Optional, Text

logger = logging.getLogger(__name__)


def concat_url(base: Text, subpath: Optional[Text]) -> Text:
    """Append a subpath to a base url.

    Strips leading slashes from the subpath if necessary. This behaves
    differently than `urlparse.urljoin` and will not treat the subpath
    as a base url if it starts with `/` but will always append it to the
    `base`.

    Args:
        base: Base URL.
        subpath: Optional path to append to the base URL.

    Returns:
        Concatenated URL with base and subpath.
    """
    if not subpath:
        if base.endswith("/"):
            logger.debug(
                f"The URL '{base}' has a trailing slash. Please make sure the "
                f"target server supports trailing slashes for this endpoint."
            )
        return base

    url = base
    if not base.endswith("/"):
        url += "/"
    if subpath.startswith("/"):
        subpath = subpath[1:]
    return url + subpath
