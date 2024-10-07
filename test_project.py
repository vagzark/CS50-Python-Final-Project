import pytest
from unittest.mock import patch
from io import StringIO
from project import weather, time, jokes, search_wikipedia, notebook, read_notes

@pytest.mark.parametrize("city_name", ["London", "New York", "Paris"])
def test_weather(city_name):
    with patch("builtins.input", return_value=city_name):
        captured_output = StringIO()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            weather()
            captured_output.write(mock_stdout.getvalue())
    assert captured_output.getvalue() != "Error Occurred\n"

def test_time(capsys):
    time()
    captured_output = capsys.readouterr()
    assert "The current time is:" in captured_output.out


def test_jokes(capsys):
    with patch('pyjokes.get_joke', return_value="This is a funny joke"):
        jokes()
        captured_output = capsys.readouterr()
        assert "I hope you liked it!" in captured_output.out

@pytest.mark.parametrize("user_input, expected_substrings", [
    ("Python programming", ["Python", "programming"]),
    ("Nonexistent_page", ["Sorry, no information found"]),
])
def test_search_wikipedia(user_input, expected_substrings):
    with patch("builtins.input", return_value=user_input), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        search_wikipedia()
        result = mock_stdout.getvalue().strip()

    for substring in expected_substrings:
        assert substring in result

@pytest.mark.parametrize("user_input, expected_output", [
    ("First note", "Note saved successfully."),
    ("Second note", "Note saved successfully."),
])
def test_notebook(user_input, expected_output):
    with patch("builtins.input", return_value=user_input), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        notebook()
        result = mock_stdout.getvalue().strip()

    assert result == expected_output

def test_read_notes():
    try:
        # Mock the current date to a specific value for testing
        mock_current_date = "03_03_2024"
        expected_file_name = f"note_{mock_current_date}.txt"

        # Prepare the test input
        test_file_contents = "First note\nSecond note"
        expected_output = "Notes:\nFirst note\nSecond note"

        # Patch 'datetime.now()' to return the mock current date
        with patch("project.datetime") as mock_datetime:
            mock_datetime.now().strftime.return_value = mock_current_date

            # Patch 'os.path.exists()' to return True for the test file
            with patch("project.os.path.exists", return_value=True):

                # Patch 'open()' to return a StringIO with the test file contents
                with patch("builtins.open", side_effect=lambda f, m: StringIO(test_file_contents)):

                    # Redirect stdout to capture the print output
                    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                        read_notes()

                        # Get the captured print output
                        result = mock_stdout.getvalue().strip()

        # Assert that the expected output is in the result
        assert expected_output in result, f"Expected output not found in the result:\n{result}"

    except Exception as e:
        pytest.fail(f"An unexpected error occurred during testing: {e}")
