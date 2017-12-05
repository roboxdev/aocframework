from pathlib import Path
from pprint import pprint
import requests


class AoCFramework(object):
    session_token = ''
    raw_puzzle_input = ''
    test_cases = ('test case placeholder', 0),
    known_result = None
    tests_ok = True
    _is_test_case = False
    result = ''

    def get_session_token(self, token_path):
        with open(token_path) as f:
            self.session_token = f.read()

    def get_puzzle_input(self, puzzle_input_path):
        try:
            with open(puzzle_input_path) as f:
                self.raw_puzzle_input = f.read()
        except FileNotFoundError:
            with open(puzzle_input_path, 'w') as f:
                res = requests.get(
                    url='http://adventofcode.com/{}/day/{}/input'.format(self.year, self.day),
                    cookies={'session': self.session_token}
                )
                if res.ok:
                    f.write(res.text)
                    self.raw_puzzle_input = res.text
                else:
                    print(res.status_code, res.text)
                    exit()

    @property
    def test(self):
        return self._is_test_case

    @property
    def puzzle_input(self):
        return self.raw_puzzle_input

    @property
    def linesplitted(self):
        return self.raw_puzzle_input.splitlines()

    def __init__(self, puzzle_input=None):
        # p = Path(sys.argv[0])
        p = Path(__import__(type(self).__module__).__file__)
        *root, aoc_year, d_day, _ = p.parts
        self.year = aoc_year[-4:]
        self.day = d_day[1:]
        self._is_test_case = puzzle_input is not None

        if not self.test:
            self.get_session_token(p.joinpath(*root, 'session_token'))
            self.get_puzzle_input(p.joinpath(*p.parts[:-1], 'raw_input.txt'))
        else:
            self.raw_puzzle_input = puzzle_input
        if not self.test:
            pprint(self.linesplitted)
            print('***')
            self.run_tests()
        if self.tests_ok or self.known_result:
            self.result = self.go()
        if not self.test:
            print('Answer:', self.result)
            if self.known_result is not None:
                if self.result == self.known_result:
                    print('You are right!')
                else:
                    print('You are wrong (answer must be {})'.format(self.known_result))

    def run_tests(self):
        for case, result in self.test_cases:
            day = type(self)(case)
            try:
                assert day.result == result
                print('[Test OK] {}: {}'.format(case, result))
            except AssertionError:
                print('[Test fail] {}: {} != {}'.format(case, day.result, result))
                self.tests_ok = False

    def go(self):
        raise NotImplementedError
