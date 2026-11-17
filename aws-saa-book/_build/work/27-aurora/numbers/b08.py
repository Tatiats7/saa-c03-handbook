import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/numbers")
from mk import *
FAQ = "docs/rds/latest/auroraextendedcontent/"
fs = []
fs.append(F("aurora-global-mixed-provisioned-and-serverless-between-regions", "capability",
 "An Aurora global database can use a mixed configuration of provisioned or serverless instance class types between the primary and secondary Regions.",
 "Can an Aurora global database mix provisioned and serverless instances between Regions?",
 [("mixed", "mixed configuration of provisioned or serverless instance class types")],
 "per Aurora global database", "", False, FAQ + "aurora-faq-availability-and-durability",
 "You can use a mixed configuration of provisioned or serverless instance class types between your primary and secondary Regions.",
 exam="core", bullets=["3.3.S2", "4.3.S3"], note="d27-054."))
fs.append(F("aurora-global-mixed-io-optimized-and-standard-between-regions", "capability",
 "In an Aurora global database you can configure the primary Region as the Aurora I/O-Optimized cluster configuration and the secondary Regions as Aurora Standard, or the reverse.",
 "Can the primary and secondary Regions of an Aurora global database use different storage configurations?",
 [("mixed", "primary Region as the Aurora I/O-Optimized cluster configuration and your secondary Regions as Aurora Standard or the reverse")],
 "per Aurora global database", "", False, FAQ + "aurora-faq-availability-and-durability",
 "You can also configure your primary Region as the Aurora I/O-Optimized cluster configuration and your secondary Regions as Aurora Standard or the reverse.",
 exam="extended", bullets=["3.3.S2", "4.3.S3"], note="d27-054, d27-090."))
write("n08.json", fs)
