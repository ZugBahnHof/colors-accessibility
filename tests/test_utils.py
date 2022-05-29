import unittest

from colors_accessibility.utils import check_if_values_are_positive, NegativeNumberError, check_if_correct_hex_value, \
    check_if_values_are_numeric, check_if_correct_hsl_values, normalize_value, normalize_values, convert_integer_to_hex, \
    expand_values, associate_input_args_with_expected_types, update_non_empty_values
from colors_accessibility.utils import IncorrectHexValueError, IncorrectHslValueError, IncorrectValueTypeError
from colors_accessibility.data.test_data import TEST_DATA


class TestColor(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    # --> Test check_if_values_are_positive

    def test_check_if_values_are_positive_correct(self):
        self.assertTrue(check_if_values_are_positive(TEST_DATA.get('numeric').get('correct_numbers')))

    def test_check_if_values_are_positive_incorrect_negative(self):
        self.assertRaises(NegativeNumberError, check_if_values_are_positive,
                          TEST_DATA.get('numeric').get('negative'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test check_if_correct_hex_value

    def test_check_if_correct_hex_value_correct(self):
        self.assertTrue(
            check_if_correct_hex_value(TEST_DATA.get('hex').get('correct').get('short').get('without_hash')))

    def test_check_if_correct_hex_value_incorrect_characters(self):
        self.assertRaises(IncorrectHexValueError, check_if_correct_hex_value,
                          TEST_DATA.get('hex').get('incorrect').get('characters'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test check_if_correct_hsl_values

    def test_check_if_correct_hsl_values_correct(self):
        self.assertTrue(check_if_correct_hsl_values(TEST_DATA.get('hsl').get('correct').get('raw')))

    def test_check_if_correct_hsl_values_incorrect_negative(self):
        self.assertRaises(NegativeNumberError, check_if_correct_hsl_values,
                          TEST_DATA.get('hsl').get('incorrect').get('negative'))

    def test_check_if_correct_hsl_values_incorrect_exceeded_maximum(self):
        self.assertRaises(IncorrectHslValueError, check_if_correct_hsl_values,
                          TEST_DATA.get('hsl').get('incorrect').get('exceeded_maximum'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test check_if_values_are_numeric

    def test_check_if_values_are_numeric_correct(self):
        self.assertTrue(check_if_values_are_numeric(TEST_DATA.get('numeric').get('correct')))

    def test_check_if_values_are_numeric_incorrect(self):
        self.assertRaises(IncorrectValueTypeError, check_if_values_are_numeric,
                          TEST_DATA.get('numeric').get('incorrect'))

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test normalize_value

    def test_normalize_value_single_to_normalize(self):
        self.assertEqual(
            normalize_value(
                TEST_DATA.get('numeric').get('to_normalize').get('single_to_normalize'),
                TEST_DATA.get('numeric').get('to_normalize').get('normalize_factor')
            ),
            TEST_DATA.get('numeric').get('to_normalize').get('single_normalized')
        )

    def test_normalize_value_single_normalized(self):
        self.assertEqual(
            normalize_value(
                TEST_DATA.get('numeric').get('to_normalize').get('single_normalized'),
                TEST_DATA.get('numeric').get('to_normalize').get('normalize_factor')
            ),
            TEST_DATA.get('numeric').get('to_normalize').get('single_normalized')
        )

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test normalize_values

    def test_normalize_values_multiple_to_normalize(self):
        self.assertEqual(
            normalize_values(
                TEST_DATA.get('numeric').get('to_normalize').get('multiple_to_normalize'),
                TEST_DATA.get('numeric').get('to_normalize').get('normalize_factor')
            ),
            TEST_DATA.get('numeric').get('to_normalize').get('multiple_normalized')
        )

    def test_normalize_values_multiple_normalized(self):
        self.assertEqual(
            normalize_values(
                TEST_DATA.get('numeric').get('to_normalize').get('multiple_normalized'),
                TEST_DATA.get('numeric').get('to_normalize').get('normalize_factor')
            ),
            TEST_DATA.get('numeric').get('to_normalize').get('multiple_normalized')
        )

    def test_normalize_values_multiple_mixed(self):
        self.assertEqual(
            normalize_values(
                TEST_DATA.get('numeric').get('to_normalize').get('multiple_mixed'),
                TEST_DATA.get('numeric').get('to_normalize').get('normalize_factor')
            ),
            TEST_DATA.get('numeric').get('to_normalize').get('multiple_mixed_normalized')
        )

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test convert_integer_to_hex
    def test_convert_integer_to_hex(self):
        self.assertEqual(
            convert_integer_to_hex(TEST_DATA.get('numeric').get('decimal_to_hex')),
            TEST_DATA.get('numeric').get('hex_from_decimal')
        )

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test expand_values
    def test_expand_values(self):
        self.assertEqual(
            expand_values(TEST_DATA.get('numeric').get('to_expand')),
            TEST_DATA.get('numeric').get('expanded')
        )

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test associate_input_args_with_expected_types
    def test_associate_input_args_with_expected_types(self):
        argument_values = TEST_DATA.get('numeric').get('associate').get('arguments_values')
        argument_names = TEST_DATA.get('numeric').get('associate').get('arguments_names')
        expected_output = TEST_DATA.get('numeric').get('associate').get('expected_output')
        self.assertEqual(
            associate_input_args_with_expected_types(argument_values, argument_names),
            expected_output
        )

    # ------------------------------------------------------------------------------------------------------------------
    # --> Test update_non_empty_values
    def test_update_non_empty_values(self):
        updated_dictionary = update_non_empty_values(
            TEST_DATA.get('dictionaries').get('to_update_dictionary'),
            TEST_DATA.get('dictionaries').get('update_dictionary')
        )
        self.assertEqual(
            updated_dictionary,
            TEST_DATA.get('dictionaries').get('result')
        )


if __name__ == '__main__':
    unittest.main()
