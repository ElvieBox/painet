import painet as pn

brain = pn.Brain()

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


# maybe make the af's seperate from the brain
# -- also think about reliance issues