facts card: 12 facts
ec2-auto-scaling-grace-period-console-300-cli-0
  claim: The default health check grace period is 300 seconds when you create a group in the console, and 0 seconds when you create it with the AWS CLI or an SDK.
  scope: per Auto Scaling group; default; adjustable; 300 seconds in the console; 0 seconds with the AWS CLI or an SDK.
  link: [300 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-console-300-cli-0)
  link: [0 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-console-300-cli-0)
  say: three hundred seconds | zero seconds
ec2-auto-scaling-grace-period-zero-turns-off
  claim: A health check grace period of 0 turns the grace period off.
  scope: per Auto Scaling group (health checks).
  link: [A value of 0 turns off](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-zero-turns-off)
  say: a value of zero turns it off
ec2-auto-scaling-grace-period-zero-with-launch-hooks
  claim: If you use lifecycle hooks for instance launch, you can set the health check grace period to 0, and a value set too high reduces the effectiveness of health checks.
  scope: per Auto Scaling group (health checks).
  link: [set the health check grace period to 0](../facts/ec2-auto-scaling.md#ec2-auto-scaling-grace-period-zero-with-launch-hooks)
  say: set the grace period to zero
ec2-auto-scaling-health-optional-checks-after-grace-period
  claim: EC2 Auto Scaling checks a new instance with the built-in EC2 status checks, and only after a grace period with the optional health checks enabled for the group.
  scope: per Auto Scaling group (health checks).
  link: [after a grace period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-optional-checks-after-grace-period)
  link: [any optional health checks that you enabled](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-optional-checks-after-grace-period)
ec2-auto-scaling-set-instance-health-respects-grace-period
  claim: By default, set-instance-health respects the health check grace period; the --no-should-respect-grace-period option overrides this.
  scope: per set-instance-health call; default; adjustable.
  link: [respects the health check grace period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-set-instance-health-respects-grace-period)
  link: [--no-should-respect-grace-period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-set-instance-health-respects-grace-period)
ec2-auto-scaling-cooldown-unhealthy-replacement-does-not-wait
  claim: Amazon EC2 Auto Scaling does not wait for the cooldown period to end before it replaces an unhealthy instance.
  scope: per Auto Scaling group (scaling cooldown).
  link: [does not wait for the cooldown period](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-unhealthy-replacement-does-not-wait)
  say: does not wait for the cooldown period
ec2-auto-scaling-health-ebs-check-must-be-turned-on
  claim: The Amazon EBS health check type checks whether EBS volumes are reachable and pass I/O status checks; you must turn it on for the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [Amazon EBS health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-check-must-be-turned-on)
  link: [passing I/O status checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-check-must-be-turned-on)
ec2-auto-scaling-lb-default-ec2-checks-only
  claim: By default EC2 Auto Scaling replaces only instances that are unhealthy or unreachable by the Amazon EC2 health checks; with Elastic Load Balancing health checks turned on it can also replace a running instance that an attached load balancer reports as unhealthy.
  scope: per Auto Scaling group; default; adjustable.
  link: [only replaces instances that are unhealthy or unreachable](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only)
  link: [report it as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only)
ec2-auto-scaling-unhealthy-terminated-replaced
  claim: An Auto Scaling group keeps a fixed number of instances even when one becomes unhealthy: it terminates the unhealthy instance and launches another to replace it.
  scope: per Auto Scaling group (health checks).
  link: [terminates the unhealthy instance and launches another](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-terminated-replaced)
  link: [maintain a fixed number of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-terminated-replaced)
ec2-auto-scaling-lifecycle-hook-lb-registration
  claim: A launch lifecycle hook is commonly used to make sure bootstrap scripts have finished and the application is ready before the instance is registered with the load balancer at the end of the hook.
  scope: per lifecycle hook.
  link: [ready to accept traffic](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-lb-registration)
  link: [control when instances are registered](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-lb-registration)
ec2-auto-scaling-health-check-type-ec2-default
  claim: Amazon EC2 status checks and scheduled events are the default health check type of an Auto Scaling group.
  scope: per Auto Scaling group; default; adjustable.
  link: [default health check type](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-check-type-ec2-default)
  say: default health check type
ec2-auto-scaling-ec2-status-checks-always-enabled
  claim: The Amazon EC2 status checks need no special configuration and are always enabled for an Auto Scaling group.
  scope: per Auto Scaling group (health checks).
  link: [always enabled](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ec2-status-checks-always-enabled)
  say: always enabled
