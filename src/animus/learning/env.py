"""Gym-style environment wrapping the C++ physics core."""

from __future__ import annotations

from typing import Sequence

from animus import Body


class BackflipEnv:
    """Minimal Gym-like interface around animus.Body.

    Swap the reward function here per skill (backflip, walk, jump, ...)
    once the underlying physics in src/sim is more than a placeholder.
    """

    def __init__(self, dt: float = 0.01):
        self.body = Body()
        self.dt = dt

    def reset(self) -> list[float]:
        return self.body.reset()

    def step(self, action: Sequence[float]):
        obs = self.body.step(list(action), self.dt)
        reward = self._reward(obs)
        done = False
        info: dict = {}
        return obs, reward, done, info

    def _reward(self, obs: Sequence[float]) -> float:
        # TODO: define a real backflip reward (e.g. angular velocity,
        # rotation completed, landing stability).
        return 0.0
