"""Training entry point: `python -m animus.learning.train`."""

from animus.learning.env import BackflipEnv


def main() -> None:
    env = BackflipEnv()
    obs = env.reset()
    print("Initial observation:", obs)

    # TODO: plug in a real RL loop (PPO/SAC) here.
    for step in range(5):
        action = [0.0] * len(obs)  # placeholder no-op action
        obs, reward, done, info = env.step(action)
        print(f"step={step} obs={obs} reward={reward}")


if __name__ == "__main__":
    main()
