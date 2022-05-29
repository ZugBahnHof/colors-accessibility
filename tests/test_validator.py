import unittest

from colors_accessibility.utils import ExceededMaximumValueError, IncorrectArgumentsTypingError, IncorrectColorSpaceError, \
    IncorrectHexValueError, IncorrectHslValueError, IncorrectInputLengthError, NegativeNumberError, \
    IncorrectHexLengthError
from colors_accessibility.validator import Validator
from colors_accessibility.data import TEST_DATA


class TestValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = Validator()

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test validate_color_space
    def test_validate_color_space_correct_lower(self):
        self.assertTrue(self.validator.validate_color_space(TEST_DATA.get('color_space').get('correct').get('lower')))

    def test_validate_color_space_correct_upper(self):
        self.assertTrue(self.validator.validate_color_space(TEST_DATA.get('color_space').get('correct').get('upper')))

    def test_validate_color_space_incorrect(self):
        self.assertRaises(IncorrectColorSpaceError, self.validator.validate_color_space,
                          TEST_DATA.get('color_space').get('incorrect'))

    def test_validate_color_space_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate_color_space, None)

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test validate_input_length
    # -> RGB
    def test_validate_input_length_rgb_correct(self):
        self.assertTrue(self.validator.validate_input_length(
            'rgb', TEST_DATA.get('rgb').get('length').get('correct')))

    def test_validate_input_length_rgb_incorrect(self):
        self.assertRaises(IncorrectInputLengthError, self.validator.validate_input_length, 'rgb',
                          TEST_DATA.get('rgb').get('length').get('incorrect'))

    def test_validate_input_length_rgb_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate_input_length, 'rgb',
                          TEST_DATA.get('rgb').get('empty'))

    # -> HEX
    def test_validate_input_length_hex_correct(self):
        self.assertTrue(self.validator.validate_input_length(
            'hex', [TEST_DATA.get('hex').get('length').get('correct')]))

    def test_validate_input_length_hex_incorrect(self):
        self.assertRaises(IncorrectInputLengthError, self.validator.validate_input_length, 'hex',
                          TEST_DATA.get('hex').get('length').get('incorrect'))

    def test_validate_input_length_hex_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate, 'hex',
                          TEST_DATA.get('hex').get('empty'))

    # -> HSL
    def test_validate_input_length_hsl_correct(self):
        self.assertTrue(self.validator.validate_input_length(
            'hsl', TEST_DATA.get('hsl').get('length').get('correct')))

    def test_validate_input_length_hsl_incorrect(self):
        self.assertRaises(IncorrectInputLengthError, self.validator.validate_input_length, 'hsl',
                          TEST_DATA.get('hsl').get('length').get('incorrect'))

    def test_validate_input_length_hsl_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate_input_length, 'hsl',
                          TEST_DATA.get('hsl').get('empty'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test validate_rgb_values

    def test_validate_rgb_values_correct(self):
        self.assertTrue(self.validator.validate_rgb_values(TEST_DATA.get("rgb").get("correct").get("raw")))

    def test_validate_rgb_values_incorrect_negative(self):
        self.assertRaises(NegativeNumberError, self.validator.validate_rgb_values,
                          TEST_DATA.get('rgb').get('incorrect').get('negative'))

    def test_validate_rgb_values_incorrect_exceeded_maximum(self):
        self.assertRaises(ExceededMaximumValueError, self.validator.validate_rgb_values,
                          TEST_DATA.get('rgb').get('incorrect').get('exceeded_maximum'))

    def test_validate_rgb_values_incorrect_empty(self):
        self.assertRaises(IncorrectInputLengthError, self.validator.validate_rgb_values,
                          TEST_DATA.get('rgb').get('empty'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test validate_hex_values

    def test_validate_hex_values_correct_short_with_hash(self):
        self.assertTrue(
            self.validator.validate_hex_values(TEST_DATA.get('hex').get('correct').get('short').get('with_hash')))

    def test_validate_hex_values_correct_short_without_hash(self):
        self.assertTrue(self.validator.validate_hex_values(
            TEST_DATA.get('hex').get('correct').get('short').get('without_hash')))

    def test_validate_hex_values_correct_long_with_hash(self):
        self.assertTrue(
            self.validator.validate_hex_values(TEST_DATA.get('hex').get('correct').get('long').get('with_hash')))

    def test_validate_hex_values_correct_long_without_hash(self):
        self.assertTrue(self.validator.validate_hex_values(
            TEST_DATA.get('hex').get('correct').get('long').get('without_hash')))

    def test_validate_hex_values_correct_list(self):
        self.assertTrue(self.validator.validate_hex_values(
            TEST_DATA.get('hex').get('correct').get('list')))

    def test_validate_hex_incorrect_characters(self):
        self.assertRaises(IncorrectHexValueError, self.validator.validate_hex_values,
                          TEST_DATA.get('hex').get('incorrect').get('characters'))

    def test_validate_hex_incorrect_value_length(self):
        self.assertRaises(IncorrectHexLengthError, self.validator.validate_hex_values,
                          TEST_DATA.get('hex').get('incorrect').get('value_length'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test validate_hsl_values

    def test_validate_hsl_values_correct(self):
        self.assertTrue(self.validator.validate_hsl_values(TEST_DATA.get('hsl').get('correct').get('raw')))

    def test_validate_hsl_values_incorrect_negative(self):
        self.assertRaises(NegativeNumberError, self.validator.validate_hsl_values,
                          TEST_DATA.get('hsl').get('incorrect').get('negative'))

    def test_validate_hsl_values_incorrect_exceeded_maximum(self):
        self.assertRaises(IncorrectHslValueError, self.validator.validate_hsl_values,
                          TEST_DATA.get('hsl').get('incorrect').get('exceeded_maximum'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test validate_values
    # RGB
    def test_validate_values_rgb_correct(self):
        self.assertTrue(self.validator.validate_values('rgb', TEST_DATA.get('rgb').get('correct').get('raw')))

    def test_validate_values_rgb_incorrect_negative(self):
        self.assertRaises(NegativeNumberError, self.validator.validate_values, 'rgb',
                          TEST_DATA.get('rgb').get('incorrect').get('negative'))

    def test_validate_values_rgb_incorrect_exceeded_maximum(self):
        self.assertRaises(ExceededMaximumValueError, self.validator.validate_values, 'rgb',
                          TEST_DATA.get('rgb').get('incorrect').get('exceeded_maximum'))

    def test_validate_values_rgb_incorrect_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate_values, 'rgb',
                          TEST_DATA.get('rgb').get('empty'))

    # HEX
    def test_validate_values_hex_correct(self):
        self.assertTrue(self.validator.validate_values('hex', TEST_DATA.get('hex').get('correct').get('short').get(
            'with_hash')))

    def test_validate_values_hex_incorrect(self):
        self.assertRaises(IncorrectHexValueError, self.validator.validate_values, 'hex',
                          TEST_DATA.get('hex').get('incorrect').get('characters'))

    def test_validate_values_hex_incorrect_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate_values, 'hex',
                          TEST_DATA.get('hex').get('empty'))

    # HSL
    def test_validate_values_hsl_correct(self):
        self.assertTrue(self.validator.validate_values('hsl', TEST_DATA.get('hsl').get('correct').get('raw')))

    def test_validate_values_hsl_incorrect_negative(self):
        self.assertRaises(NegativeNumberError, self.validator.validate_values, 'hsl',
                          TEST_DATA.get('hsl').get('incorrect').get('negative'))

    def test_validate_values_hsl_incorrect_exceeded_maximum(self):
        self.assertRaises(IncorrectHslValueError, self.validator.validate_values, 'hsl',
                          TEST_DATA.get('hsl').get('incorrect').get('exceeded_maximum'))

    def test_validate_values_hsl_incorrect_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate_values, 'hsl',
                          TEST_DATA.get('hsl').get('empty'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test validate
    # -> RGB
    def test_validate_rgb_correct(self):
        self.assertTrue(self.validator.validate('rgb', TEST_DATA.get('rgb').get('correct').get('raw')))

    def test_validate_rgb_incorrect_negative(self):
        self.assertRaises(NegativeNumberError, self.validator.validate, 'rgb',
                          TEST_DATA.get('rgb').get('incorrect').get('negative'))

    def test_validate_rgb_incorrect_exceeded_maximum(self):
        self.assertRaises(ExceededMaximumValueError, self.validator.validate, 'rgb',
                          TEST_DATA.get('rgb').get('incorrect').get('exceeded_maximum'))

    def test_validate_rgb_incorrect_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate, 'rgb',
                          TEST_DATA.get('rgb').get('empty'))

    # -> HEX
    def test_validate_hex_correct_short_with_hash(self):
        self.assertTrue(
            self.validator.validate('hex', TEST_DATA.get('hex').get('correct').get('short').get('with_hash')))

    def test_validate_hex_correct_short_without_hash(self):
        self.assertTrue(
            self.validator.validate('hex', TEST_DATA.get('hex').get('correct').get('short').get('without_hash')))

    def test_validate_hex_correct_long_with_hash(self):
        self.assertTrue(
            self.validator.validate('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash')))

    def test_validate_hex_correct_long_without_hash(self):
        self.assertTrue(
            self.validator.validate('hex', TEST_DATA.get('hex').get('correct').get('long').get('without_hash')))

    def test_validate_hex_incorrect_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate, 'hex',
                          TEST_DATA.get('hex').get('empty'))

    # -> HSL
    def test_validate_hsl_correct(self):
        self.assertTrue(self.validator.validate('hsl', TEST_DATA.get('hsl').get('correct').get('raw')))

    def test_validate_hsl_incorrect_negative(self):
        self.assertRaises(NegativeNumberError, self.validator.validate, 'hsl',
                          TEST_DATA.get('hsl').get('incorrect').get('negative'))

    def test_validate_hsl_incorrect_exceeded_maximum(self):
        self.assertRaises(IncorrectHslValueError, self.validator.validate, 'hsl',
                          TEST_DATA.get('hsl').get('incorrect').get('exceeded_maximum'))

    def test_validate_hsl_incorrect_empty(self):
        self.assertRaises(IncorrectArgumentsTypingError, self.validator.validate, 'hsl',
                          TEST_DATA.get('hsl').get('empty'))


if __name__ == '__main__':
    unittest.main()
