import painet as pn

brain = pn.Brain(pn.exampleNetwork)

blankNetwork = [
    {
        "inputs": [],
        "hiddenAF": "step",
        "outputAF": "mirroredStep",
    },
    [
        # Hidden Neurons (anything between the header and the possible outputs)
    ],
    [
        # Output Neurons 
    ],
    [
        # Possible Outputs
    ]
]

print(brain.Network)


# maybe make the af's seperate from the brain
# -- also think about reliance issues


# BIG NOTE: Brain init now uses blank network, which is not included in Brain
# This makes it reliant on the rest
# Might be able to fix by having a "generate blank" function
