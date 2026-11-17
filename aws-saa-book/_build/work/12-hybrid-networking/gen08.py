import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
D="direct-connect"
FAQ="www/directconnect/faqs"
PP="www/directconnect/pricing/pay-as-you-go"
def pd(id,claim,q,disp,evid,exam="extended",note="d12-055",tier=2,cond="",scope="per account",**kw):
    return fact(id,D,"pricing-dimension",claim,q,[("v",disp,"")] if disp else [("v",claim.split(",")[0][:40],"")],scope,"",False,evid,cond=cond,tier=tier,exam=exam,bullets=["4.4.S2"],note=note,**kw)
F=[]
F.append(fact("direct-connect-pricing-two-charges-port-hours-data-transfer",D,"pricing-dimension",
 "Direct Connect has two separate charges, port hours and data transfer; pricing is per port-hour for each port type, partial port hours are billed as full hours, and the account that owns the port pays the port hour charges.",
 "Which charges make up Direct Connect pricing, and who pays the port hours?",
 [("v","two separate charges: port hours and data transfer","")],"per port","",False,
 [ev(FAQ,"AWS Direct Connect has two separate charges: port hours and data transfer. Pricing is per port-hour consumed for each port type. Partial port hours consumed are billed as full hours. The account that owns the port will be charged the port hour charges.")],
 tier=2,exam="core",bullets=["4.4.S2"],note="d12-055. FAQ 78."))
F.append(fact("direct-connect-pricing-three-factors",D,"pricing-dimension",
 "For connections to any AWS Region or Local Zone, three factors determine Direct Connect pricing: capacity, port hours, and data transfer out (DTO) through your Direct Connect location.",
 "What three factors determine Direct Connect pricing?",
 [("v","capacity, port hours, and data transfer out","")],"per connection","",False,
 [ev(PP,"When connecting to resources running in any AWS Region (such as an Amazon Virtual Private Cloud or AWS Transit Gateway) or Local Zone, there are three factors that determine pricing: capacity, port hours, and data transfer out (DTO) through your AWS Direct Connect location.")],
 tier=2,exam="core",bullets=["4.4.S2"],note="d12-055"))
F.append(fact("direct-connect-pricing-port-hours-even-when-idle",D,"pricing-dimension",
 "You are charged Direct Connect port hours even when no data is passing through the port.",
 "Do you pay Direct Connect port hours when no data is passing through the port?",
 [("v","Even when no data is passing through the port","")],"per port","",False,
 [ev(PP,"Even when no data is passing through the port, you are charged for port hours.")],
 tier=2,exam="core",bullets=["4.4.S2"],note="d12-055"))
F.append(fact("direct-connect-pricing-no-setup-no-minimum-term",D,"pricing-dimension",
 "Direct Connect has no setup charges and you may cancel at any time, although services from AWS Direct Connect Partners may have other terms or restrictions.",
 "Are there setup charges or a minimum service term for Direct Connect?",
 [("v","no setup charges","")],"per account","",False,
 [ev(FAQ,"There are no setup charges, and you may cancel at any time. Services provided by AWS Direct Connect Partners may have other terms or restrictions that apply.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-055. FAQ 77."))
F.append(fact("direct-connect-pricing-data-transfer-in-free",D,"pricing-dimension",
 "Data transfer in over Direct Connect is $0.00 per gigabyte at all Direct Connect locations.",
 "What does data transfer in over Direct Connect cost?",
 [("v","$0.00 per gigabyte","zero dollars per gigabyte")],"per gigabyte, per location","",False,
 [ev(PP,"Data transfer in is $0.00 per gigabyte at all AWS Direct Connect locations.")],
 tier=2,exam="core",bullets=["4.4.S2"],note="d12-055. Zero amount, not a price."))
F.append(fact("direct-connect-pricing-dto-by-region-and-location",D,"pricing-dimension",
 "Direct Connect data transfer out (DTO) pricing depends on the source AWS Region or Local Zone and the Direct Connect location.",
 "What does Direct Connect data transfer out pricing depend on?",
 [("v","source AWS Region or Local Zone and AWS Direct Connect location","")],"per gigabyte","",False,
 [ev(PP,"DTO pricing is dependent on the source AWS Region or Local Zone and AWS Direct Connect location.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-055"))
F.append(fact("direct-connect-pricing-hosted-port-hours-after-accept",D,"pricing-dimension",
 "Port hours for a hosted connection are billed once you have accepted it, and keep being billed as long as it is provisioned for your use; to stop charges, work with your Direct Connect Partner to cancel it.",
 "When do port-hour charges for a hosted connection start and stop?",
 [("v","billed once you have accepted the Hosted Connection","")],"per hosted connection","",False,
 [ev(FAQ,"Port hours are billed once you have accepted the Hosted Connection. Port charges will continue to be billed as long as the Hosted Connection is provisioned for your use. If you no longer want to be charged for your Hosted Connection, work with your AWS Direct Connect Partner to cancel the Hosted Connection.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-055. FAQ 80."))
F.append(fact("direct-connect-pricing-dedicated-port-hours-while-provisioned",D,"pricing-dimension",
 "Dedicated connection port hours are billed as long as the port is provisioned for your use.",
 "How long are dedicated Direct Connect port hours billed?",
 [("v","billed as long as that port is provisioned","")],"per dedicated connection","",False,
 [ev(PP,"Dedicated port hours are billed as long as that port is provisioned for your use.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-055"))
F.append(fact("direct-connect-pricing-dto-account-private-vif",D,"pricing-dimension",
 "For a private virtual interface, the AWS account that owns the AWS resources responsible for the data transfer out is charged.",
 "Which account is charged data transfer out over a private virtual interface?",
 [("v","the AWS account that owns the AWS resources","")],"per private virtual interface","",False,
 [ev(FAQ,"In the case of the private virtual interface, the AWS account that owns the AWS resources responsible for the Data Transfer Out will be charged.")],
 tier=2,exam="reference",bullets=["4.4.S2"],note="d12-055. FAQ 83."))
F.append(fact("direct-connect-pricing-dto-not-internet",D,"pricing-dimension",
 "Direct Connect data transfer out is the data sent out of AWS through your Direct Connect location; it does not transfer data over the internet, which the EC2 pricing page covers.",
 "Does Direct Connect data transfer out include transfers to the internet?",
 [("v","does not transfer data over the internet","")],"per gigabyte","",False,
 [ev(FAQ,"AWS Direct Connect transfers data out of AWS through the connections made at your AWS Direct Connect location. It does not transfer data over the internet. For information on data transfer over the internet, refer to the EC2 pricing page.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-055. FAQ 84."))
F.append(fact("direct-connect-pricing-az-transfer-not-dx-rate",D,"pricing-dimension",
 "Data transfer between Availability Zones in a Region is billed at the regular Regional data transfer rate, not at the Direct Connect rate.",
 "Is Regional data transfer billed at the Direct Connect rate?",
 [("v","regular Regional data transfer rate","")],"per gigabyte","",False,
 [ev(FAQ,"No, data transfer between Availability Zones in a Region will be billed at the regular Regional data transfer rate in the same month in which the usage occurred.")],
 tier=2,exam="reference",bullets=["4.4.S2"],note="FAQ 79."))
F.append(fact("direct-connect-pricing-macsec-no-extra-charge",D,"pricing-dimension",
 "There is no additional charge for MACsec on Direct Connect.",
 "Is there an additional charge for MACsec?",
 [("v","no additional charge for MACsec","")],"per connection","",False,
 [ev(FAQ,"No, there is no additional charge for MACsec.")],
 tier=2,exam="extended",bullets=["1.2.S4"],note="FAQ 185."))
dump(F,"facts-numbers-08.json")
