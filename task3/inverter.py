#! /usr/bin/env python3
def invert(S: str) -> str:
    """
    FIXME: dummy method, as the task is about testing
    uncomment the commented lines to have a wrong implementation of the
    function
    """
    if not S:
        # return None   # uncomment to have a wrong implementation
        return ""
    if len(S) == 1:
        return S
    # return S  # uncomment to have a wrong implementation
    return S[::-1]
