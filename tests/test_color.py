import unittest

from colors_accessibility.color import Color
from colors_accessibility.data import TEST_DATA


class TestColor(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    # Test __str__
    def test_str(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        string_representation = \
            "Color(color_space='rgb', color_values='[0.23137254901960785, 0.12156862745098039, 0.34509803921568627]')"
        self.assertEqual(str(color), string_representation)

    # ------------------------------------------------------------------------------------------------------------------
    # Test format_hex
    def test_format_hex_correct(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('short').get('with_hash'))
        color.format_hex()
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))

    def test_format_hex_list(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('list'))
        color.format_hex()
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test process_rgb
    def test_process_rgb_correct(self):
        color = Color('RGb', TEST_DATA.get('rgb').get('correct').get('processed'))
        color.process_rgb()
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('raw'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test process_hex
    def test_process_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('short').get('with_hash'))
        color.process_hex()
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test process_hsl
    def test_process_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('raw'))
        color.process_hsl()
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('processed'))

    def test_process_hsl_normalized_hue(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('normalized_hue'))
        color.process_hsl()
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('normalized_hue_processed'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test process
    def test_process_values_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.process('rgb')
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('raw'))

    def test_process_values_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('short').get('with_hash'))
        color.process('hex')
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))

    def test_process_values_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('raw'))
        color.process('hsl')
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('processed'))

    def test_process_values_hsl_dictionary(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('dictionary'))
        color.process('hsl')
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('dictionary_processed'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test process_hsl_values
    def test_process_hsl_values(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        output_number = color.process_hsl_values(0)
        expected_output = TEST_DATA.get('numeric').get('number_for_processing_hsl').get('output')
        self.assertEqual(output_number, expected_output)

    # ------------------------------------------------------------------------------------------------------------------
    # Test rgb_to_hex

    def test_rgb_to_hex(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        hex_representation = color.rgb_to_hex()
        self.assertEqual(hex_representation, TEST_DATA.get('hex').get('correct').get('rgb_to_hex'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test hsl_to_hex
    def test_hsl_to_hex(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        hex_representation = color.hsl_to_hex()
        self.assertEqual(hex_representation, TEST_DATA.get('hex').get('correct').get('hsl_to_hex'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test hex_to_rgb
    def test_hex_to_rgb(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        rgb_representation = color.hex_to_rgb()
        self.assertEqual(rgb_representation, TEST_DATA.get('rgb').get('correct').get('hex_to_rgb'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test hsl_to_rgb
    def test_hsl_to_rgb(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        rgb_representation = color.hsl_to_rgb()
        self.assertEqual(rgb_representation, TEST_DATA.get('rgb').get('correct').get('hsl_to_rgb'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test rgb_to_hsl
    def test_rgb_to_hsl(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        hsl_representation = color.rgb_to_hsl()
        self.assertEqual(hsl_representation, TEST_DATA.get('hsl').get('correct').get('rgb_to_hsl'))

    def test_rgb_to_hsl_equal(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('equal'))
        hsl_representation = color.rgb_to_hsl()
        self.assertEqual(hsl_representation, TEST_DATA.get('hsl').get('correct').get('rgb_to_hsl_equal'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test hex_to_hsl
    def test_hex_to_hsl(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        hsl_representation = color.hex_to_hsl()
        self.assertEqual(hsl_representation, TEST_DATA.get('hsl').get('correct').get('hex_to_hsl'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test to_hex
    def test_to_hex_from_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        hex_representation = color.to_hex()
        self.assertEqual(hex_representation, TEST_DATA.get('hex').get('correct').get('rgb_to_hex'))

    def test_to_hex_from_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        hex_representation = color.to_hex()
        self.assertEqual(hex_representation, TEST_DATA.get('hex').get('correct').get('hsl_to_hex'))

    def test_to_hex_from_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        hex_representation = color.to_hex()
        self.assertEqual(hex_representation, TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test to_rgb
    def test_to_rgb_from_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        rgb_representation = color.to_rgb()
        self.assertEqual(rgb_representation, TEST_DATA.get('rgb').get('correct').get('hex_to_rgb_normalized'))

    def test_to_rgb_from_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        rgb_representation = color.to_rgb()
        self.assertEqual(rgb_representation, TEST_DATA.get('rgb').get('correct').get('hsl_to_rgb_normalized'))

    def test_to_rgb_from_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        rgb_representation = color.to_rgb()
        self.assertEqual(rgb_representation, TEST_DATA.get('rgb').get('correct').get('raw'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test to_hsl
    def test_to_hsl_from_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        hsl_representation = color.to_hsl()
        self.assertEqual(hsl_representation, TEST_DATA.get('hsl').get('correct').get('hex_to_hsl'))

    def test_to_hsl_from_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        hsl_representation = color.to_hsl()
        self.assertEqual(hsl_representation, TEST_DATA.get('hsl').get('correct').get('rgb_to_hsl'))

    def test_to_hsl_from_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        hsl_representation = color.to_hsl()
        self.assertEqual(hsl_representation, TEST_DATA.get('hsl').get('correct').get('processed'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test set_to_rgb
    def test_set_to_rgb_from_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.set_to_rgb()
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('hex_to_rgb_normalized'))

    def test_set_to_rgb_from_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.set_to_rgb()
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('hsl_to_rgb_normalized'))

    def test_set_to_rgb_from_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.set_to_rgb()
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('raw'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test set_to_hex
    def test_set_to_hex_from_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.set_to_hex()
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))

    def test_set_to_hex_from_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.set_to_hex()
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('hsl_to_hex'))

    def test_set_to_hex_from_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.set_to_hex()
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('rgb_to_hex'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test set_to_hsl
    def test_set_to_hsl_from_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.set_to_hsl()
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('hex_to_hsl'))

    def test_set_to_hsl_from_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.set_to_hsl()
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('processed'))

    def test_set_to_hsl_from_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.set_to_hsl()
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('rgb_to_hsl'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test set_to
    # -> HEX
    def test_set_to_from_hex_to_rgb(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.set_to('rgb')
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('hex_to_rgb_normalized'))

    def test_set_to_from_hex_to_hsl(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.set_to('hsl')
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('hex_to_hsl'))

    def test_set_to_from_hex_to_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.set_to('hex')
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))

    # -> HSL
    def test_set_to_from_hsl_to_rgb(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.set_to('rgb')
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('hsl_to_rgb_normalized'))

    def test_set_to_from_hsl_to_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.set_to('hsl')
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('processed'))

    def test_set_to_from_hsl_to_hex(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.set_to('hex')
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('hsl_to_hex'))

    # -> RGB
    def test_set_to_from_rgb_to_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.set_to('rgb')
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('raw'))

    def test_set_to_from_rgb_to_hsl(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.set_to('hsl')
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('rgb_to_hsl'))

    def test_set_to_from_rgb_to_hex(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.set_to('hex')
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('rgb_to_hex'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test calculate_relative_luminance
    def test_calculate_relative_luminance_from_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        self.assertEqual(color.calculate_relative_luminance(),
                         TEST_DATA.get('hex').get('correct').get('relative_luminance'))

    def test_calculate_relative_luminance_from_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        self.assertEqual(color.calculate_relative_luminance(),
                         TEST_DATA.get('hsl').get('correct').get('relative_luminance'))

    def test_calculate_relative_luminance_from_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        self.assertEqual(color.calculate_relative_luminance(),
                         TEST_DATA.get('rgb').get('correct').get('relative_luminance'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test convert
    # -> HEX
    def test_convert_from_hex_to_hex(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.convert('hex')
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))

    def test_convert_from_hex_to_hsl(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.convert('hsl')
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('hex_to_hsl'))

    def test_convert_from_hex_to_rgb(self):
        color = Color('hex', TEST_DATA.get('hex').get('correct').get('long').get('with_hash'))
        color.convert('rgb')
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('hex_to_rgb_normalized'))

    # -> HSL
    def test_convert_from_hsl_to_hex(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.convert('hex')
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('hsl_to_hex'))

    def test_convert_from_hsl_to_hsl(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.convert('hsl')
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('processed'))

    def test_convert_from_hsl_to_rgb(self):
        color = Color('hsl', TEST_DATA.get('hsl').get('correct').get('processed'))
        color.convert('rgb')
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('hsl_to_rgb_normalized'))

    # -> RGB
    def test_convert_from_rgb_to_hex(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.convert('hex')
        self.assertEqual(color.color_space, 'hex')
        self.assertEqual(color.color_values, TEST_DATA.get('hex').get('correct').get('rgb_to_hex'))

    def test_convert_from_rgb_to_hsl(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.convert('hsl')
        self.assertEqual(color.color_space, 'hsl')
        self.assertEqual(color.color_values, TEST_DATA.get('hsl').get('correct').get('rgb_to_hsl'))

    def test_convert_from_rgb_to_rgb(self):
        color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        color.convert('rgb')
        self.assertEqual(color.color_space, 'rgb')
        self.assertEqual(color.color_values, TEST_DATA.get('rgb').get('correct').get('raw'))


if __name__ == '__main__':
    unittest.main()
