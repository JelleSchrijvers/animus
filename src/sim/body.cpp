#include "include/body.hpp"

namespace animus {

Body::Body() : state_(6, 0.0) {}

std::vector<double> Body::reset() {
    state_.assign(6, 0.0);
    return state_;
}

std::vector<double> Body::step(const std::vector<double>& action, double dt) {
    // TODO: replace with real physics integration.
    // Placeholder: naive Euler integration on a fake state so the
    // Python <-> C++ pipeline can be tested end to end immediately.
    for (std::size_t i = 0; i < state_.size() && i < action.size(); ++i) {
        state_[i] += action[i] * dt;
    }
    return state_;
}

std::vector<double> Body::get_observation() const {
    return state_;
}

} // namespace animus
