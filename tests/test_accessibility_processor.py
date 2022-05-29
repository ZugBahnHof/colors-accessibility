import unittest

from colors_accessibility.accessibility_processor import AccessibilityProcessor
from colors_accessibility.color import Color
from colors_accessibility.data import TEST_DATA


class TestAccessibilityProcessor(unittest.TestCase):

    def setUp(self) -> None:
        self.foreground_color = Color('rgb', TEST_DATA.get('rgb').get('correct').get('raw'))
        self.background_color = Color('hex', TEST_DATA.get('hex').get('correct').get('short').get('with_hash'))
        self.processor = AccessibilityProcessor(foreground_color=self.foreground_color,
                                                background_color=self.background_color)

    def test_calculate_contrast(self):
        foreground_luminance = self.foreground_color.calculate_relative_luminance()
        background_luminance = self.background_color.calculate_relative_luminance()
        contrast = self.processor.calculate_contrast(foreground_luminance, background_luminance)
        self.assertEqual(contrast, TEST_DATA.get('numeric').get('contrast'))

    def test_calculate(self):
        self.assertEqual(self.processor.calculate(), TEST_DATA.get('numeric').get('contrast'))

    def test_get_luminance_values(self):
        foreground_luminance = self.foreground_color.calculate_relative_luminance()
        background_luminance = self.background_color.calculate_relative_luminance()
        self.assertEqual(self.processor.get_luminance_values(self.foreground_color, self.background_color),
                         (foreground_luminance, background_luminance))

    def test_get_parameter_signature(self):
        signature = self.processor.get_parameter_signature(
            TEST_DATA.get('signature').get('parameter'),
            TEST_DATA.get('signature').get('color_to_change')
        )
        self.assertEqual(signature, TEST_DATA.get('signature').get('signature_values').get('single'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test get_parameters_signatures

    def test_get_parameters_signatures(self):
        signatures = self.processor.get_parameters_signatures(
            TEST_DATA.get('signature').get('parameter'),
            TEST_DATA.get('signature').get('color_to_change')
        )
        expected_signatures = {
            int(key): value
            for key, value
            in TEST_DATA.get('signature').get('signature_values').get('multiple').items()
        }
        self.assertEqual(signatures, expected_signatures)



    def test_increment_color_hsl_values(self):
        incremented_color = self.processor.increment_color_hsl_values(
            self.foreground_color,
            TEST_DATA.get('signature').get('parameter'),
            TEST_DATA.get('signature').get('signature_values').get('multiple')
        )
        self.assertEqual(incremented_color.color_space,
                         TEST_DATA.get('signature').get('incremented_color').get('color_space'))
        self.assertEqual(incremented_color.color_values,
                         TEST_DATA.get('signature').get('incremented_color').get('color_values'))

    # ------------------------------------------------------------------------------------------------------------------
    # Test update_wcag_requirements
    # -> single

    def test_update_wcag_requirements_single_below_value(self):
        contrast = TEST_DATA.get('contrasts').get('below')
        color_values = self.foreground_color.to_hsl()
        wcag_requirements = self.processor.update_wcag_requirements(contrast, color_values)
        self.assertEqual(wcag_requirements, TEST_DATA.get('wcag_requirements').get('single').get('below'))

    def test_update_wcag_requirements_single_middle_value(self):
        contrast = TEST_DATA.get('contrasts').get('middle')
        color_values = self.foreground_color.to_hsl()
        wcag_requirements = self.processor.update_wcag_requirements(contrast, color_values)
        self.assertEqual(wcag_requirements, TEST_DATA.get('wcag_requirements').get('single').get('middle'))

    def test_update_wcag_requirements_single_above_value(self):
        contrast = TEST_DATA.get('contrasts').get('above')
        color_values = self.foreground_color.to_hsl()
        wcag_requirements = self.processor.update_wcag_requirements(contrast, color_values)
        self.assertEqual(wcag_requirements, TEST_DATA.get('wcag_requirements').get('single').get('above'))

    # -> multiple

    def test_update_wcag_requirements_multiple_below_value(self):
        contrast = TEST_DATA.get('contrasts').get('below')
        foreground_color_values = self.foreground_color.to_hsl()
        background_color_values = self.background_color.to_hsl()
        wcag_requirements = self.processor.update_wcag_requirements(contrast, foreground_color_values,
                                                                    background_color_values)
        self.assertEqual(wcag_requirements, TEST_DATA.get('wcag_requirements').get('multiple').get('below'))

    def test_update_wcag_requirements_multiple_middle_value(self):
        contrast = TEST_DATA.get('contrasts').get('middle')
        foreground_color_values = self.foreground_color.to_hsl()
        background_color_values = self.background_color.to_hsl()
        wcag_requirements = self.processor.update_wcag_requirements(contrast, foreground_color_values,
                                                                    background_color_values)
        self.assertEqual(wcag_requirements, TEST_DATA.get('wcag_requirements').get('multiple').get('middle'))

    def test_update_wcag_requirements_multiple_above_value(self):
        contrast = TEST_DATA.get('contrasts').get('above')
        foreground_color_values = self.foreground_color.to_hsl()
        background_color_values = self.background_color.to_hsl()
        wcag_requirements = self.processor.update_wcag_requirements(contrast, foreground_color_values,
                                                                    background_color_values)
        self.assertEqual(wcag_requirements, TEST_DATA.get('wcag_requirements').get('multiple').get('above'))


if __name__ == '__main__':
    unittest.main()
