"""Tests the functionality of a 2-approximation to metric TSP."""
# CSC 349 Assignment 8
# Feel free to add additional tests
import pathlib
import re
import subprocess
import unittest

from typing import Tuple

from graph import Graph

OUTPUT_RE = re.compile(
    r'^Hamiltonian cycle of weight (?P<weight>\d+):\n'
    r'(?P<cycle>(?:\d+, )*\d+)\n?$')


class TestTSP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        set_execute_bits()
        compile_code()

    def test_in1(self):
        self.assertCorrectApproximation('test_files/in1.txt', 21)

    def test_in2(self):
        self.assertCorrectApproximation('test_files/in2.txt', 3)

    def test_in3(self):
        self.assertCorrectApproximation('test_files/in3.txt', 8)

    def assertCorrectApproximation(self, graph_file: str, optimal: int):  # noqa
        out, err = run_code(graph_file)

        self.assertEqual(err, '', 'Program printed to stderr')
        self.assertRegex(out, OUTPUT_RE, 'Output is in the wrong format.')

        try:
            weight, cycle = parse_cycle(out)
        except ValueError as e:
            self.fail(f'Failed to test {graph_file}: {e}')

        self.assertLessEqual(
            weight, 2 * optimal, 'Algorithm is not a 2-approximation.')

        self.assertHamiltonianCycleWithWeight(
            cycle, weight, Graph.from_file(graph_file))

    def assertHamiltonianCycleWithWeight(  # noqa
            self, cycle: Tuple[int, ...], weight: int, graph: Graph):
        self.assertEqual(cycle[0], cycle[-1], 'Cycle is not a cycle.')
        self.assertCountEqual(
            cycle[1:], graph, 'Cycle has missing or extra vertices.')

        actual_weight = sum(
            graph[cycle[i]][cycle[i + 1]] for i in range(len(cycle) - 1))

        self.assertEqual(
            weight, actual_weight, 'Cycle does not have specified weight.')


def set_execute_bits():
    """Set the execute bits on all local shell files."""
    for f in pathlib.Path().glob('*.sh'):
        f.chmod(f.stat().st_mode | 0o111)


def compile_code(timeout: int = 5):
    """Run the local file compile.sh if one exists.

    Args:
        timeout: Length of time (in seconds) to wait.
    """
    if not pathlib.Path('./compile.sh').is_file():
        return

    subprocess.run(
        './compile.sh',
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=timeout,
        check=True)


def run_code(graph_file: str, timeout: int = 1) -> Tuple[str, str]:
    """Runs the local file run.sh and returns the result.

    Args:
        graph_file: The name of the file to be passed as a command line
            argument.
        timeout: Length of time (in seconds) to wait.

    Returns:
        The stdout and stderr from running the script.
    """
    result = subprocess.run(
        ['./run.sh', graph_file],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        timeout=timeout,
        check=True,
        encoding='utf-8')

    return result.stdout, result.stderr


def parse_cycle(output: str) -> Tuple[int, Tuple[int, ...]]:
    """Parse the stdout into a weight and a cycle.

    Args:
        output: The stdout of the script.

    Returns:
        The weight of the cycle and the cycle itself.

    Raises:
        ValueError: The output cannot be read.
    """
    match = OUTPUT_RE.fullmatch(output)

    if not match:
        raise ValueError('Could not parse output.')

    weight = int(match['weight'])
    cycle = tuple(int(x) for x in match['cycle'].split(', '))

    return weight, cycle


if __name__ == '__main__':
    unittest.main()
