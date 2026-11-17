GT = "docs/autoscaling/ec2/userguide/gracefully-handle-instance-termination"
FACTS = [
F("ec2-auto-scaling-no-visibility-into-applications", "behavior",
  "By default EC2 Auto Scaling has no visibility into the applications on its instances, so it can terminate an instance before the application shuts down gracefully or finishes its jobs.",
  "Does Auto Scaling wait for your application to finish before it terminates an instance?",
  ["no visibility into the applications", "able to gracefully shut down"],
  (GT, "By default, Auto Scaling has no visibility into the applications running on your instances. It can terminate instances before your application is able to gracefully shut down or complete its assigned jobs."),
  ["2.2.S4", "3.2.S1"]),
F("ec2-auto-scaling-stateful-drain-or-transfer", "behavior",
  "To shut down a stateful instance gracefully, its workload should be drained (finish its assigned jobs) or transferred to another active instance.",
  "How should a stateful instance's work be handled before Auto Scaling terminates it?",
  ["either drained (completing all currently assigned jobs)", "transferred (moving jobs, data, or configuration"],
  (GT, "To gracefully shut down a stateful instance, its workload should be either drained (completing all currently assigned jobs) or transferred (moving jobs, data, or configuration to another active instance)."),
  ["2.2.S4"], rel="extended"),
]
