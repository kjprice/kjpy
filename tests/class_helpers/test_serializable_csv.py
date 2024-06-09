from src.kjpy.data.unit_test_handler import UnitTestWithTestData


from src.kjpy.class_helpers.serializable_csv import SerializableCsv

# TODO: Wrap unsafe cells with quotes

_TEST_DIRECTORY = "class_helpers"
_DEBUG = True


# TODO: Move to its own file
class TestSerializableCsv(UnitTestWithTestData):
    def setUp(self) -> None:
        return super().setUp(debug=_DEBUG, test_directory=_TEST_DIRECTORY)

    def test_serializable_csv(self):
        _input = [{"name": "kj", "age": 12}]
        serializable_csv = SerializableCsv(all_data=_input)
        self.assertEqualsTestData(
            serializable_csv.serialize(),
            "serializable_csv_simple_response.csv",
        )
