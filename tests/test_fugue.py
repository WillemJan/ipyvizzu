"""A module for testing the ipyvizzu.integrations.fugue module."""

import sys
import io
from contextlib import redirect_stdout
import pathlib
import pandas as pd  # type: ignore
import unittest

from tests.normalizer import Normalizer


# TODO: remove once support for Python 3.6 is dropped
if sys.version_info >= (3, 7):
    import fugue.api as fa  # type: ignore

    # register the extension, not needed in practical use
    import ipyvizzu.integrations.fugue  # pylint: disable-all


# TODO: remove once support for Python 3.6 is dropped
@unittest.skipUnless(sys.version_info >= (3, 7), "requires Python 3.7")
class TestFugue(unittest.TestCase):
    """
    A class for testing Fugue integration.
    """

    def test_fugue_extension_preset(self):
        """Test Fugue extension - preset"""
        ref = pathlib.Path(__file__).parent / "assets" / "fugue_preset.txt"
        with open(ref, "r") as f_ref:
            ref_content = f_ref.read()
        df = pd.DataFrame(dict(a=list("abcde"), b=range(5)))
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            fa.fugue_sql_flow(
                """
                SELECT * FROM df WHERE b<5

                OUTPUT USING vizzu:bar(x="a",y="b")
            """,
                df=df,
            ).run()
        self.assertEqual(
            Normalizer().normalize_id("\n".join(stdout.getvalue().split("\n")[1:])),
            ref_content,
        )

    def test_fugue_extension_timeline(self):
        """Test Fugue extension - timeline"""
        ref = pathlib.Path(__file__).parent / "assets" / "fugue_timeline.txt"
        with open(ref, "r") as f_ref:
            ref_content = f_ref.read()
        df = pd.DataFrame(dict(a=list("abcde"), b=range(5), c=[1, 1, 2, 2, 3]))
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            fa.fugue_sql_flow(
                """
                SELECT * FROM df WHERE b<5

                OUTPUT USING vizzu:timeline_bar(
                    by="c",
                    config={"x":"b","y":"a",title="x %s"},
                    duration=0.3
                )
            """,
                df=df,
            ).run()
        self.assertEqual(
            Normalizer().normalize_id("\n".join(stdout.getvalue().split("\n")[1:])),
            ref_content,
        )
