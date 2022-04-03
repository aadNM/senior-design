import argparse
import sys
import warnings
import webbrowser
import questionary
from typing import Any, NoReturn, Optional, Text, Type

from rasa.shared.exceptions import RasaXTermsError

import rasax.community.constants as constants
import rasax.community.utils.config as config_utils


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def wrap_with_color(*args: Any, color: Text):
    return color + " ".join(str(s) for s in args) + bcolors.ENDC


def print_color(*args: Any, color: Text):
    print(wrap_with_color(*args, color=color))


def print_success(*args: Any):
    print_color(*args, color=bcolors.OKGREEN)


def print_info(*args: Any):
    print_color(*args, color=bcolors.OKBLUE)


def print_warning(*args: Any):
    print_color(*args, color=bcolors.WARNING)


def print_error(*args: Any):
    print_color(*args, color=bcolors.FAIL)


def print_error_and_exit(message: Text, exit_code: int = 1) -> NoReturn:
    """Print error message and exit the application."""

    print_error(message)
    sys.exit(exit_code)


def raise_warning(
    message: Text,
    category: Optional[Type[Warning]] = None,
    docs: Optional[Text] = None,
    **kwargs: Any,
) -> None:
    """Emit a `warnings.warn` with sensible defaults and a colored warning msg."""

    original_formatter = warnings.formatwarning

    def formatwarning(
        message: Text,
        category: Optional[Type[Warning]],
        filename: Text,
        lineno: Optional[int],
        _line: Optional[Text] = None,
    ):
        """Function to format a warning the standard way."""

        formatted_message = original_formatter(
            message, category, filename, lineno, f"More info at {docs}" if docs else ""
        )
        return wrap_with_color(formatted_message, color=bcolors.WARNING)

    if "stacklevel" not in kwargs and category in (UserWarning, FutureWarning):
        kwargs["stacklevel"] = 2

    warnings.formatwarning = formatwarning
    warnings.warn(message, category=category, **kwargs)
    warnings.formatwarning = original_formatter


def accept_terms_or_raise(args: argparse.Namespace) -> None:
    """Prompt the user to accept the Rasa X terms.

    Args:
        args: Parsed command line arguments.

    Raises:
        RasaXTermsError: If the user has not agreed to the Rasa X terms of
            usage.
    """

    show_prompt = not getattr(args, "no_prompt", False)

    if not show_prompt:
        print(
            f"By adding the '--no_prompt' parameter you agreed to the Rasa "
            f"X license agreement ({constants.RASA_TERMS_URL})"
        )
        return

    print_success(
        "Before you can use Rasa X, you have to agree to its "
        "license agreement (you will only have to do this "
        "once)."
    )

    should_open_in_browser = questionary.confirm(
        "Would you like to view the license agreement in your web browser?"
    ).ask()

    if should_open_in_browser:
        webbrowser.open(constants.RASA_TERMS_URL)

    accepted_terms = questionary.confirm(
        "\nRasa X License Agreement\n"
        "===========================\n\n"
        "Do you agree to the Rasa X license agreement ({})?\n"
        "By typing 'y', you agree to the terms. "
        "If you are using this software for a company, by confirming, "
        "you acknowledge you have the authority to do so.\n"
        "If you do not agree, type 'n' to stop Rasa X."
        "".format(constants.RASA_TERMS_URL),
        default=False,
        qmark="",
    ).ask()

    if accepted_terms:
        config_utils.write_global_config_value(constants.CONFIG_FILE_TERMS_KEY, True)
    else:
        print_error(
            "Sorry, without accepting the terms, you cannot use Rasa X. "
            "You can of course still use the (Apache 2 licensed) Rasa Open Source "
            "framework: https://github.com/RasaHQ/rasa"
        )

        raise RasaXTermsError()
