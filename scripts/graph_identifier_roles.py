"""Separate header-declared identifiers from body references in graph scans."""
import re


def metadata_header(body, max_lines=40):
    """Return (header_text, line_count) for the document's own metadata region.

    The first level-2-or-deeper heading ends the header. For heading-less legacy
    files, cap the candidate metadata region at max_lines to avoid turning the
    whole document's index/reference body into declarations.
    """
    lines = body.splitlines()
    end = min(len(lines), max_lines)
    for index, line in enumerate(lines[1:], start=1):
        if re.match(r"^\s*#{2,}\s+", line):
            end = min(end, index)
            break
    return "\n".join(lines[:end]), end


def metadata_label_line(line):
    return bool(re.match(
        r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:"
        r"Stable ID(?:\s*/\s*شناسهٔ پایدار)?|Stable-ID|Canonical Stable ID|"
        r"Stable Reference ID|Stable Report ID|شناسهٔ پایدار(?: این نقطه)?|"
        r"شناسه پایدار(?: این نقطه)?|Production ID(?:\s*/\s*شناسهٔ تولید)?|"
        r"Production-ID|Production / Registration ID|شناسهٔ تولید|شناسه تولید|"
        r"شناسهٔ ثبت|Reference ID)(?:\*\*)?\s*:", line, re.I
    ))
