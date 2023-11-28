module Code

function newton_update(; state_n1, state_n)
    println("state_n1=$state_n1, state_n=$state_n")

    # Oh no, there are arguments passed from the main script ito this function,
    # like "newton_epsilon" This is really bad, why are some arguemnts passed
    # as functions arguments and why as "global" variables in the python template?
    # We first hav to fix the Python template!
    residual_norm = 1e5
    # while residual_norm >= newton_epsilon
    #     residual, tangent_matrix = compute(state_n1, state_n, integrator)
    #     state_delta = -np.linalg.inv(tangent_matrix) @ residual
    #     state_n1 = state_n1 + state_delta
    #     residual_norm = np.linalg.norm(residual)
    # end

    return state_n1
end

end # module Code
