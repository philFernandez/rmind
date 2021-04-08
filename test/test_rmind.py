import os
import dotenv
from rich.console import Console

rich_console = Console()


def pre_test(mode: str):
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    os.environ["APP_MODE"] = mode
    dotenv.set_key(dotenv_file, "APP_MODE", os.environ["APP_MODE"])  # type: ignore


def post_test(exit_code):
    # Reset APP_MODE="" (take out of test mode)
    pre_test("")
    os.remove(os.path.join(".", ".test.db"))
    if exit_code != 0:
        exit(exit_code)


# test func names go here after being defined nested inside test()
tests = ["test_add()", "test_rmind()", "test_update()", "test_delete()"]


# test funcs are nested in test so that pre_test() can be run in separate scope.
# The reason is so that APP_MODE is set to "test" before the main program is run
def test():
    from click.testing import CliRunner
    from remind.scripts import cli, add, delete, update

    def test_rmind():
        runner = CliRunner()
        result = runner.invoke(cli)
        try:
            assert result.exit_code == 0
        except AssertionError:
            rich_console.print_exception()
            post_test(1)
        rich_console.print(":white_heavy_check_mark: [green b]test_rmind[/green b]")

    # Need setup test db with ENV VAR trigger
    def test_add():
        runner = CliRunner()
        result = runner.invoke(add, ["--add", "This is a thing"])
        try:
            assert result.exit_code == 0
        except AssertionError:
            rich_console.print_exception()
            post_test(1)
        rich_console.print(":white_heavy_check_mark: [green b]test_add[/green b]")

    def test_delete():
        runner = CliRunner()
        result = runner.invoke(delete, ["1"])
        try:
            assert result.exit_code == 0
        except AssertionError:
            rich_console.print_exception()
            post_test(1)
        rich_console.print(":white_heavy_check_mark: [green b]test_delete[/green b]")

    def test_update():
        runner = CliRunner()
        result = runner.invoke(update, ["1", "--update", "This is a new thing"])
        try:
            assert result.exit_code == 0
        except AssertionError:
            rich_console.print_exception()
            post_test(1)
        rich_console.print(":white_heavy_check_mark: [green b]test_update[/green b]")

    for test in tests:
        eval(test)


if __name__ == "__main__":
    pre_test("test")
    test()
    post_test(0)
    rich_console.rule(style="green")
    rich_console.print(f":white_heavy_check_mark: [green]{len(tests)} tests passed.")
