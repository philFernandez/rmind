import os
import dotenv


def set_test_env(env: str):
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    os.environ["APP_MODE"] = env
    dotenv.set_key(dotenv_file, "APP_MODE", os.environ["APP_MODE"])  # type: ignore


def test():
    from click.testing import CliRunner
    from remind.scripts import cli, add, delete

    # Need setup test db with ENV VAR trigger
    def test_add():
        runner = CliRunner()
        result = runner.invoke(add, ["--add", "This is a thing"])
        assert result.exit_code == 0

    def test_delete():
        runner = CliRunner()
        result = runner.invoke(delete, ["1"])
        assert result.exit_code == 0
        print(result.exc_info)

    test_add()
    test_delete()


if __name__ == "__main__":
    set_test_env("debug")
    test()
    set_test_env("")
