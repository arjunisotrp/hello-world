# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2022 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------


"""Tools for the APY skill."""

from typing import Iterator, Optional


def gen_unix_timestamps(start: int, interval_in_unix: int, end: int) -> Iterator[int]:
    """Generate the Unix timestamps from start to end with the given interval.

    :param start: the start date for the generated timestamps.
    :param interval_in_unix: the interval to use in order to generate the timestamps.
    :param end: the end date for the generated timestamps.
    :yields: the UNIX timestamps.
    """
    if interval_in_unix <= 0:
        raise ValueError(
            f"Interval cannot be less than 1. {interval_in_unix} was given."
        )

    for timestamp in range(start, end, interval_in_unix):
        yield timestamp





def filter_out_numbers(string: str) -> Optional[int]:
    """Filter out all the numbers from a string.

    :param string: the string to filter.
    :return: a filtered out integer.
    """
    numeric_filter = filter(str.isdigit, string)
    numeric_string = "".join(numeric_filter)

    if numeric_string == "":
        filtered_result = None
    else:
        filtered_result = int(numeric_string)
        # Get only the first 9 digits, because the seed cannot be > 2**32 -1
        filtered_result = int(str(filtered_result)[:9])

    return filtered_result
