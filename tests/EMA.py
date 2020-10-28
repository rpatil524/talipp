import unittest

from talipp.indicators import EMA

from talippTest import ITAITest


class Test(ITAITest):
    def setUp(self) -> None:
        self.input_values = list(ITAITest.CLOSE_TMPL)

    def test_init(self):
        ind = EMA(20, self.input_values)

        print(ind)

        self.assertAlmostEqual(ind[-3], 9.319374, places = 5)
        self.assertAlmostEqual(ind[-2], 9.406100, places = 5)
        self.assertAlmostEqual(ind[-1], 9.462662, places = 5)

    def test_update(self):
        self.assertIndicatorUpdate(EMA(20, self.input_values))

    def test_delete(self):
        self.assertIndicatorDelete(EMA(20, self.input_values))


if __name__ == '__main__':
    unittest.main()
