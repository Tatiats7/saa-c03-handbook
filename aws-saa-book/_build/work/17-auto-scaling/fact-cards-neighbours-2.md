facts card: 6 facts
ec2-spot-interruption-notice-channels
  claim: Spot interruption notices are delivered as an EventBridge event and as items in the instance metadata of the Spot Instance; AWS recommends checking for them every 5 seconds.
  scope: per Spot Instance.
  link: [as an EventBridge event](../facts/ec2.md#ec2-spot-interruption-notice-channels)
  link: [every 5 seconds](../facts/ec2.md#ec2-spot-interruption-notice-channels)
  link: [as items in the instance metadata](../facts/ec2.md#ec2-spot-interruption-notice-channels)
  say: an EventBridge event and the instance metadata | every five seconds | and in the instance metadata
ec2-spot-rebalance-recommendation-channels
  claim: Rebalance recommendations are made available as an EventBridge event and as an item in the instance metadata of the Spot Instance, and events are emitted on a best effort basis.
  scope: Spot Instance rebalance recommendations.
  link: [made available as a EventBridge event](../facts/ec2.md#ec2-spot-rebalance-recommendation-channels)
  link: [as an item in the instance metadata](../facts/ec2.md#ec2-spot-rebalance-recommendation-channels)
  link: [emitted on a best effort basis](../facts/ec2.md#ec2-spot-rebalance-recommendation-channels)
  say: you get it as an EventBridge event | and in the instance metadata
ec2-alarm-reboot-instance-check-recover-system-check
  claim: The CloudWatch reboot alarm action is recommended for instance status check failures, and the recover alarm action is suited for system status check failures.
  scope: CloudWatch alarm actions on an EC2 instance.
  link: [recommended for Instance Health Check failures](../facts/ec2.md#ec2-alarm-reboot-instance-check-recover-system-check)
  link: [suited for System Health Check failures](../facts/ec2.md#ec2-alarm-reboot-instance-check-recover-system-check)
  say: reboot for an instance check failure | recover for a system check failure
ec2-ami-definition-and-contents
  claim: An AMI is an image that provides the software needed to set up and boot an EC2 instance and contains a block device mapping of the volumes to attach; you must specify an AMI at launch and it must be compatible with the instance type.
  scope: Amazon Machine Images.
  link: [an image that provides the software](../facts/ec2.md#ec2-ami-definition-and-contents)
  link: [a block device mapping](../facts/ec2.md#ec2-ami-definition-and-contents)
  link: [You must specify an AMI](../facts/ec2.md#ec2-ami-definition-and-contents)
  say: an AMI is the image that sets up and boots an instance
ec2-metadata-user-data-not-protected
  claim: Instance metadata and user data can be accessed only from within the instance, but they are not protected by authentication or cryptographic methods, so you should not store sensitive data such as passwords or long-lived encryption keys as user data.
  scope: instance metadata and user data.
  link: [from within the instance itself](../facts/ec2.md#ec2-metadata-user-data-not-protected)
  link: [not protected by authentication or cryptographic methods](../facts/ec2.md#ec2-metadata-user-data-not-protected)
  link: [you should not store sensitive data](../facts/ec2.md#ec2-metadata-user-data-not-protected)
  say: only from inside the instance | but it is not protected | do not store secrets in user data
ec2-stop-start-new-billing-period-one-minute-minimum
  claim: Charges stop as soon as an instance enters the stopping state (for hibernation, only when it reaches stopped); each transition from stopped to running starts a new billing period with a minimum of one minute, and a reboot does not change the billing hour.
  scope: per instance; minimum; Amazon EBS-backed instances for stop/start and hibernate.
  link: [a minimum of one minute](../facts/ec2.md#ec2-stop-start-new-billing-period-one-minute-minimum)
  link: [as soon as its state changes to stopping](../facts/ec2.md#ec2-stop-start-new-billing-period-one-minute-minimum)
  link: [The instance billing hour doesn't change](../facts/ec2.md#ec2-stop-start-new-billing-period-one-minute-minimum)
  say: a one-minute minimum on every start | charges stop at stopping | a reboot does not change the billing hour
