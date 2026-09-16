#pragma once

#include <vector>

namespace animus {

// Minimal placeholder for a physically simulated agent (e.g. a ragdoll).
// Replace internals with your real physics engine (Bullet, MuJoCo-like
// custom integrator, etc). This class is the single thing bindings.cpp
// exposes to Python.
class Body {
public:
    Body();

    // Advance the simulation by dt seconds, applying the given joint
    // torques/actions. Returns the new observation vector.
    std::vector<double> step(const std::vector<double>& action, double dt);

    // Reset the simulation to a starting pose. Returns the initial observation.
    std::vector<double> reset();

    // Current observation (e.g. joint angles, velocities, orientation).
    std::vector<double> get_observation() const;

private:
    std::vector<double> state_;
};

} // namespace animus
