from remind.scripts.rmind import cli
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
    print(result.output)


if __name__ == "__main__":
    test_add()
    test_delete()