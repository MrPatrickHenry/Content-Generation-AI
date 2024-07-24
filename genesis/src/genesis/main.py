#!/usr/bin/env python
from genesis.crew import GenesisCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    GenesisCrew().crew().kickoff(inputs=inputs)