from application import GraphStateDistribution

from squidasm.run.stack.config import StackNetworkConfig
from squidasm.run.stack.run import run

nodes = ["Alice", "Bob", "Charlie", "David", "Edna", "Frank"]

# import network configuration from file
cfg = StackNetworkConfig.from_file("config.yaml")

# Create instances of programs to run
alice_program = GraphStateDistribution(node_name="Alice", node_names=nodes)
bob_program = GraphStateDistribution(node_name="Bob", node_names=nodes)
charlie_program = GraphStateDistribution(node_name="Charlie", node_names=nodes)
david_program = GraphStateDistribution(node_name="David", node_names=nodes)
edna_program = GraphStateDistribution(node_name="Edna", node_names=nodes)
frank_program = GraphStateDistribution(node_name="Frank", node_names=nodes)

# Run the simulation. Programs argument is a mapping of network node labels to programs to run on that node
run(config=cfg, programs={"Alice": alice_program, "Bob": bob_program,
                          "Charlie": charlie_program, "David": david_program, 
                          "Edna": edna_program, "Frank": frank_program}, num_times=1)